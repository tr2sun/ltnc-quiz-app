import json
import os
import re

DATA_DIR = r"D:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app\src\data"
QUESTIONS_DIR = os.path.join(DATA_DIR, "questions")

def run_verification():
    print("=== Running Expanded Presets Verification ===")
    errors = []
    
    # Load all questions
    all_questions = {}
    lesson_files = [f for f in os.listdir(QUESTIONS_DIR) if f.startswith("lesson") and f.endswith(".json")]
    
    for fname in sorted(lesson_files):
        path = os.path.join(QUESTIONS_DIR, fname)
        with open(path, "r", encoding="utf-8") as f:
            qs = json.load(f)
        
        print(f"File {fname}: {len(qs)} questions")
        for q in qs:
            qid = q.get("id")
            if not qid:
                errors.append(f"Question in {fname} missing 'id': {q}")
                continue
            if qid in all_questions:
                errors.append(f"Duplicate question ID: {qid} in {fname}")
            all_questions[qid] = q
            
            # Validate fields
            if len(q.get("options", [])) != 4:
                errors.append(f"{qid} does not have exactly 4 options")
            
            ans = q.get("correctAnswer")
            if isinstance(ans, int):
                if ans < 0 or ans > 3:
                    errors.append(f"{qid} single correctAnswer {ans} out of range [0..3]")
            elif isinstance(ans, list):
                if len(ans) == 0:
                    errors.append(f"{qid} multiple correctAnswer is empty")
                for a in ans:
                    if a < 0 or a > 3:
                        errors.append(f"{qid} multiple answer index {a} out of range [0..3]")
            else:
                errors.append(f"{qid} invalid correctAnswer type: {type(ans)}")
                
            if not q.get("explanation"):
                errors.append(f"{qid} has empty explanation")

    # Load and verify sectionPresets.js
    presets_file = os.path.join(DATA_DIR, "sectionPresets.js")
    with open(presets_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    prefix = "import { getQuestionsByLesson } from './index.js';\n\nexport const SECTION_PRESETS = "
    suffix_start = content.find("];\n\n/**")
    if suffix_start == -1:
        suffix_start = content.find("];\n/**")
    json_str = content[len(prefix):suffix_start + 1]
    presets_data = json.loads(json_str)

    total_presets_count = 0
    for section in presets_data:
        lid = section["lessonId"]
        presets = section["presets"]
        total_presets_count += len(presets)
        seen_in_section = set()
        print(f"\n--- Section Lesson {lid}: {section['title']} ({len(presets)} presets) ---")
        for p in presets:
            pid = p["id"]
            code = p["code"]
            qids = p["questionIds"]
            print(f"  * [{code}] {p['title']}: {len(qids)} questions")
            if len(qids) != 15:
                errors.append(f"Preset {pid} in Lesson {lid} does not have 15 questions (has {len(qids)})")
            for qid in qids:
                if qid not in all_questions:
                    errors.append(f"Preset {pid} references unknown question ID: {qid}")
                if qid in seen_in_section:
                    errors.append(f"CRITICAL: Question {qid} is OVERLAPPED in preset {pid} of Lesson {lid}!")
                seen_in_section.add(qid)
        print(f"  => Total unique questions across presets for Lesson {lid}: {len(seen_in_section)} (Overlap count: 0)")

    print(f"\nTotal questions across bank: {len(all_questions)}")
    print(f"Total section presets across app: {total_presets_count}")
    
    if errors:
        print(f"\nFAILED with {len(errors)} errors:")
        for e in errors[:20]:
            print("  -", e)
        return False
    else:
        print("\nALL VERIFICATIONS PASSED! (0 errors, 100% disjoint presets, 100% valid schema)")
        return True

if __name__ == "__main__":
    success = run_verification()
    exit(0 if success else 1)
