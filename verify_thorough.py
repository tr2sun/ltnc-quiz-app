import json
import os
import re

base_dir = r"D:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app"
questions_dir = os.path.join(base_dir, "src", "data", "questions")

errors = []
warnings = []
stats = {}

all_questions_by_id = {}

print("=== STARTING JSON QUESTION AUDIT ===")

expected_lessons = [f"lesson{i}" for i in range(1, 10)]

for lesson in expected_lessons:
    filename = f"{lesson}.json"
    filepath = os.path.join(questions_dir, filename)
    if not os.path.exists(filepath):
        errors.append(f"Missing file: {filepath}")
        continue
    
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except Exception as e:
            errors.append(f"Failed to parse JSON {filename}: {e}")
            continue

    if not isinstance(data, list):
        errors.append(f"{filename} does not contain a JSON list")
        continue

    lesson_num = int(lesson.replace("lesson", ""))
    theory_count = 0
    code_count = 0
    
    for idx, q in enumerate(data):
        qid = q.get("id")
        if not qid or not isinstance(qid, str):
            errors.append(f"[{filename} #{idx}] Missing or invalid id")
        elif qid in all_questions_by_id:
            errors.append(f"[{filename} #{idx}] Duplicate question id '{qid}' (already in {all_questions_by_id[qid]['file']})")
        else:
            all_questions_by_id[qid] = {"data": q, "file": filename}

        # Check lessonId
        if q.get("lessonId") != lesson_num:
            errors.append(f"[{filename} #{idx}] question {qid} has lessonId {q.get('lessonId')}, expected {lesson_num}")

        # Check title
        title = q.get("title", "")
        if not title or not isinstance(title, str) or len(title.strip()) < 5:
            errors.append(f"[{filename} #{idx}] question {qid} has missing or too short title")

        # Check options
        options = q.get("options")
        if not isinstance(options, list) or len(options) != 4:
            errors.append(f"[{filename} #{idx}] question {qid} must have exactly 4 options, got {len(options) if isinstance(options, list) else type(options)}")
        else:
            for opt_idx, opt in enumerate(options):
                if not isinstance(opt, str) or not opt.strip():
                    errors.append(f"[{filename} #{idx}] question {qid} option[{opt_idx}] is empty or non-string")

        # Check correctAnswer
        correct = q.get("correctAnswer")
        if not isinstance(correct, int) or correct < 0 or correct > 3:
            errors.append(f"[{filename} #{idx}] question {qid} has invalid correctAnswer: {correct}")

        # Check explanation
        expl = q.get("explanation", "")
        if not isinstance(expl, str) or len(expl.strip()) < 10:
            errors.append(f"[{filename} #{idx}] question {qid} has empty or trivial explanation")

        # Check tags
        tags = q.get("tags")
        if not isinstance(tags, list) or len(tags) == 0:
            errors.append(f"[{filename} #{idx}] question {qid} has empty or missing tags")

        # Check difficulty
        diff = q.get("difficulty")
        if diff not in ["easy", "medium", "hard"]:
            errors.append(f"[{filename} #{idx}] question {qid} invalid difficulty: {diff}")

        # Code vs Theory ratio check
        code = q.get("code")
        if code is not None and isinstance(code, str) and code.strip():
            code_count += 1
        else:
            theory_count += 1

    stats[lesson] = {
        "total": len(data),
        "theory": theory_count,
        "code": code_count,
        "ratio": f"{theory_count}/{code_count}"
    }

print("\n--- Question Breakdown per Lesson ---")
for lesson, s in stats.items():
    print(f"{lesson}: Total={s['total']}, Theory={s['theory']}, Code={s['code']} (Ratio: {s['ratio']})")
    if s['total'] == 0:
        errors.append(f"{lesson} has 0 questions")
    if s['theory'] != s['code']:
        warnings.append(f"{lesson} theory vs code is not exactly 50/50: {s['theory']} theory vs {s['code']} code")

print(f"\nTotal Questions Loaded: {len(all_questions_by_id)}")

# Check Exam Presets
print("\n=== AUDITING EXAM PRESETS ===")
presets_file = os.path.join(base_dir, "src", "data", "examPresets.js")
if not os.path.exists(presets_file):
    errors.append(f"Missing examPresets.js at {presets_file}")
else:
    with open(presets_file, "r", encoding="utf-8") as f:
        presets_content = f.read()
    
    # Parse exam presets using regex
    # Match preset blocks
    preset_blocks = re.findall(r"id:\s*[\"']([^\"']+)[\"'].*?code:\s*[\"']([^\"']+)[\"'].*?totalQuestions:\s*(\d+).*?questionIds:\s*\[(.*?)\]", presets_content, re.DOTALL)
    if not preset_blocks:
        errors.append("Could not parse exam presets from examPresets.js")
    else:
        for pid, pcode, ptotal, pids_str in preset_blocks:
            expected_total = int(ptotal)
            # extract string ids
            pids = re.findall(r"[\"']([^\"']+)[\"']", pids_str)
            print(f"Exam '{pcode}' ({pid}): declared {expected_total} questions, found {len(pids)} ids")
            
            if len(pids) != 30 or expected_total != 30:
                errors.append(f"Exam preset {pcode} does not have exactly 30 questions (found {len(pids)}, declared {expected_total})")
            
            # Check duplicate question IDs inside preset
            if len(pids) != len(set(pids)):
                errors.append(f"Exam preset {pcode} contains duplicate question IDs!")
            
            # Check if all question IDs exist in question bank
            missing_q = [qid for qid in pids if qid not in all_questions_by_id]
            if missing_q:
                errors.append(f"Exam preset {pcode} references non-existent questions: {missing_q}")

print("\n=== SUMMARY OF VERIFICATION ===")
if errors:
    print(f"FAILED with {len(errors)} errors:")
    for err in errors:
        print(f"  ❌ {err}")
else:
    print("✅ All integrity checks passed with 0 errors!")

if warnings:
    print(f"\nWarnings ({len(warnings)}):")
    for w in warnings:
        print(f"  ⚠️ {w}")
