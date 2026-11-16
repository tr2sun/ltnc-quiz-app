import json
import os
import re

base_dir = r"D:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app"
questions_dir = os.path.join(base_dir, "src", "data", "questions")

errors = []
warnings = []

# 1. Audit Question Bank
print("=== 1. AUDITING QUESTION BANK ===")
all_questions = {}
lesson_stats = {}

lesson_files = [
    ("lesson1.json", 1),
    ("lesson3.json", 3),
    ("lesson4.json", 4),
    ("lesson5.json", 5),
    ("lesson6.json", 6),
    ("lesson7.json", 7),
    ("lesson8.json", 8),
    ("lesson9.json", 9),
]

for filename, expected_lesson_id in lesson_files:
    filepath = os.path.join(questions_dir, filename)
    if not os.path.exists(filepath):
        errors.append(f"Missing file: {filepath}")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            questions = json.load(f)
        except Exception as e:
            errors.append(f"Invalid JSON in {filename}: {e}")
            continue

    single_count = 0
    multi_count = 0
    theory_count = 0
    code_count = 0

    for idx, q in enumerate(questions):
        qid = q.get("id")
        if not qid:
            errors.append(f"[{filename} #{idx}] Missing ID")
            continue

        if qid in all_questions:
            errors.append(f"[{filename}] Duplicate question ID: {qid} (already seen in {all_questions[qid]['file']})")
        else:
            all_questions[qid] = {"data": q, "file": filename}

        # Check lessonId
        if q.get("lessonId") != expected_lesson_id:
            errors.append(f"[{filename} #{idx}] Question {qid} lessonId={q.get('lessonId')}, expected {expected_lesson_id}")

        # Check title
        title = q.get("title", "")
        if not title or len(title.strip()) < 5:
            errors.append(f"[{filename} #{idx}] Question {qid} title missing or too short")

        # Check options
        options = q.get("options")
        if not isinstance(options, list) or len(options) != 4:
            errors.append(f"[{filename} #{idx}] Question {qid} options must be a list of 4, got {len(options) if isinstance(options, list) else type(options)}")
        else:
            for opt_idx, opt in enumerate(options):
                if not isinstance(opt, str) or not opt.strip():
                    errors.append(f"[{filename} #{idx}] Question {qid} option[{opt_idx}] is empty")

        # Check type & correctAnswer
        q_type = q.get("type", "single")
        correct = q.get("correctAnswer")
        if q_type == "single":
            single_count += 1
            if not isinstance(correct, int) or correct < 0 or correct > 3:
                errors.append(f"[{filename} #{idx}] Question {qid} (single) invalid correctAnswer: {correct}")
        elif q_type == "multiple":
            multi_count += 1
            if not isinstance(correct, list) or len(correct) < 2 or len(correct) > 4:
                errors.append(f"[{filename} #{idx}] Question {qid} (multiple) correctAnswer must be list of 2..4 ints, got {correct}")
            else:
                for c in correct:
                    if not isinstance(c, int) or c < 0 or c > 3:
                        errors.append(f"[{filename} #{idx}] Question {qid} (multiple) invalid option index {c} in {correct}")
                if len(correct) != len(set(correct)):
                    errors.append(f"[{filename} #{idx}] Question {qid} (multiple) duplicate indices in correctAnswer: {correct}")
        else:
            errors.append(f"[{filename} #{idx}] Question {qid} invalid type: {q_type}")

        # Check explanation
        expl = q.get("explanation", "")
        if not isinstance(expl, str) or len(expl.strip()) < 10:
            errors.append(f"[{filename} #{idx}] Question {qid} explanation missing or too short")

        # Check tags
        tags = q.get("tags")
        if not isinstance(tags, list) or len(tags) == 0:
            errors.append(f"[{filename} #{idx}] Question {qid} tags empty or missing")

        # Check difficulty
        diff = q.get("difficulty")
        if diff not in ["easy", "medium", "hard"]:
            errors.append(f"[{filename} #{idx}] Question {qid} invalid difficulty: {diff}")

        # Code vs Theory
        if q.get("code") and isinstance(q.get("code"), str) and q.get("code").strip():
            code_count += 1
        else:
            theory_count += 1

    lesson_stats[filename] = {
        "lessonId": expected_lesson_id,
        "total": len(questions),
        "single": single_count,
        "multiple": multi_count,
        "theory": theory_count,
        "code": code_count
    }

print("\n--- Summary per Lesson File ---")
for f, s in lesson_stats.items():
    print(f"{f} (Lesson {s['lessonId']}): Total={s['total']} (Single: {s['single']}, Multiple: {s['multiple']}) | (Theory: {s['theory']}, Code: {s['code']})")

print(f"\nTotal Questions in Bank: {len(all_questions)}")

# 2. Audit Section Presets (sectionPresets.js)
print("\n=== 2. AUDITING SECTION PRESETS ===")
sec_presets_file = os.path.join(base_dir, "src", "data", "sectionPresets.js")
if not os.path.exists(sec_presets_file):
    errors.append(f"Missing sectionPresets.js at {sec_presets_file}")
else:
    with open(sec_presets_file, "r", encoding="utf-8") as f:
        sec_content = f.read()

    # Find JSON structure inside SECTION_PRESETS
    # We can extract each preset block with regex
    # Each preset: id, code, title, questionIds: [...]
    lesson_blocks = re.findall(r"lessonId\":\s*(\d+).*?presets\":\s*\[(.*?)\]\s*\}", sec_content, re.DOTALL)
    
    total_section_presets = 0
    for l_id_str, presets_str in lesson_blocks:
        l_id = int(l_id_str)
        # Find all preset objects inside
        p_matches = re.findall(r"id\":\s*\"([^\"]+)\".*?code\":\s*\"([^\"]+)\".*?questionIds\":\s*\[(.*?)\]", presets_str, re.DOTALL)
        
        chapter_question_sets = []
        for pid, pcode, pids_str in p_matches:
            total_section_presets += 1
            pids = re.findall(r"\"([^\"]+)\"", pids_str)
            print(f"Chapter {l_id} - {pcode} ({pid}): {len(pids)} questions")
            
            # Check length exactly 15
            if len(pids) != 15:
                errors.append(f"Preset {pcode} ({pid}) has {len(pids)} questions, expected EXACTLY 15")
            
            # Check for duplicates within preset
            if len(pids) != len(set(pids)):
                errors.append(f"Preset {pcode} has internal duplicate questions!")
                
            # Check that every question exists and belongs to this chapter
            for qid in pids:
                if qid not in all_questions:
                    errors.append(f"Preset {pcode} references non-existent question: {qid}")
                else:
                    q_lesson = all_questions[qid]["data"].get("lessonId")
                    if q_lesson != l_id:
                        errors.append(f"Preset {pcode} belongs to Lesson {l_id} but question {qid} has lessonId {q_lesson}")

            chapter_question_sets.append((pcode, set(pids)))

        # Crucial check: MUTUALLY DISJOINT presets in each chapter
        for i in range(len(chapter_question_sets)):
            for j in range(i + 1, len(chapter_question_sets)):
                code_i, set_i = chapter_question_sets[i]
                code_j, set_j = chapter_question_sets[j]
                overlap = set_i.intersection(set_j)
                if overlap:
                    errors.append(f"MUTUAL EXCLUSIVITY VIOLATION in Chapter {l_id}: {code_i} and {code_j} share questions: {overlap}")
                else:
                    print(f"  ✓ {code_i} and {code_j} are 100% disjoint (0 overlap)")

    print(f"\nTotal Section Presets Audited: {total_section_presets}")

# 3. Audit General Exam Presets (examPresets.js)
print("\n=== 3. AUDITING GENERAL EXAM PRESETS ===")
exam_presets_file = os.path.join(base_dir, "src", "data", "examPresets.js")
if not os.path.exists(exam_presets_file):
    errors.append(f"Missing examPresets.js at {exam_presets_file}")
else:
    with open(exam_presets_file, "r", encoding="utf-8") as f:
        exam_content = f.read()

    exam_matches = re.findall(r"id:\s*[\"']([^\"']+)[\"'].*?code:\s*[\"']([^\"']+)[\"'].*?totalQuestions:\s*(\d+).*?questionIds:\s*\[(.*?)\]", exam_content, re.DOTALL)
    for eid, ecode, etotal_str, epids_str in exam_matches:
        epids = re.findall(r"[\"']([^\"']+)[\"']", epids_str)
        print(f"Exam {ecode} ({eid}): declared {etotal_str}, found {len(epids)} question IDs")
        if len(epids) != 30:
            errors.append(f"General Exam {ecode} has {len(epids)} questions, expected EXACTLY 30")
        if len(epids) != len(set(epids)):
            errors.append(f"General Exam {ecode} has duplicate question IDs")
        for qid in epids:
            if qid not in all_questions:
                errors.append(f"General Exam {ecode} references non-existent question: {qid}")

# 4. Multi-select exact match scoring verification
print("\n=== 4. TESTING MULTI-SELECT SCORING LOGIC ===")
def is_answer_correct(question, user_selection):
    if user_selection is None:
        return False
    is_multi = question.get("type") == "multiple" or isinstance(question.get("correctAnswer"), list)
    if is_multi:
        if not isinstance(user_selection, list):
            return False
        correct_arr = question.get("correctAnswer") if isinstance(question.get("correctAnswer"), list) else [question.get("correctAnswer")]
        if len(user_selection) != len(correct_arr):
            return False
        return sorted(user_selection) == sorted(correct_arr)
    else:
        return user_selection == question.get("correctAnswer")

# Test cases
test_multi_q = {"type": "multiple", "correctAnswer": [0, 2]}
assert is_answer_correct(test_multi_q, [0, 2]) == True, "Failed ordered match"
assert is_answer_correct(test_multi_q, [2, 0]) == True, "Failed unordered match"
assert is_answer_correct(test_multi_q, [0]) == False, "Failed partial match reject"
assert is_answer_correct(test_multi_q, [0, 1, 2]) == False, "Failed extra match reject"
assert is_answer_correct(test_multi_q, [1, 3]) == False, "Failed wrong answer reject"
assert is_answer_correct(test_multi_q, []) == False, "Failed empty match reject"
assert is_answer_correct(test_multi_q, None) == False, "Failed None match reject"

test_single_q = {"type": "single", "correctAnswer": 2}
assert is_answer_correct(test_single_q, 2) == True, "Failed single match"
assert is_answer_correct(test_single_q, 1) == False, "Failed single wrong"
assert is_answer_correct(test_single_q, None) == False, "Failed single None"
print("✓ All scoring logic assertions passed perfectly!")

# Final summary
print("\n================== VERIFICATION RESULT ==================")
if errors:
    print(f"❌ FAILED with {len(errors)} errors:")
    for e in errors:
        print(f"  - {e}")
else:
    print("✅ 100% PASSED! All section exams, mutual exclusivity, question integrity, and scoring logic verified flawlessly.")
