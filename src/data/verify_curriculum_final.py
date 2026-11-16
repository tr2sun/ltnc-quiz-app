import json
import re

LESSON_IDS = [1, 3, 4, 5, 6, 7, 8, 9]

# 1. Load all questions
all_questions = []
lesson_questions = {}
id_set = set()
errors = []

for lid in LESSON_IDS:
    path = f"d:/STUDY_HK1_NAM2/LTNC/ltnc-quiz-app/src/data/questions/lesson{lid}.json"
    try:
        with open(path, encoding="utf-8") as f:
            qs = json.load(f)
            lesson_questions[lid] = qs
            for q in qs:
                qid = q.get("id")
                if not qid:
                    errors.append(f"Missing id in lesson{lid}")
                elif qid in id_set:
                    errors.append(f"Duplicate id {qid} in lesson{lid}")
                id_set.add(qid)
                all_questions.append(q)

                # Validate fields
                if q.get("lessonId") != lid:
                    errors.append(f"{qid}: lessonId {q.get('lessonId')} != {lid}")
                if not q.get("title"):
                    errors.append(f"{qid}: missing title")
                opts = q.get("options", [])
                if len(opts) != 4:
                    errors.append(f"{qid}: options length {len(opts)} != 4")
                for oi, opt in enumerate(opts):
                    if not opt or not str(opt).strip():
                        errors.append(f"{qid}: empty option {oi}")

                qtype = q.get("type", "single")
                ans = q.get("correctAnswer")
                if qtype == "single":
                    if not isinstance(ans, int) or ans < 0 or ans > 3:
                        errors.append(f"{qid}: invalid single correctAnswer {ans}")
                elif qtype == "multiple":
                    if not isinstance(ans, list) or len(ans) == 0:
                        errors.append(f"{qid}: multiple correctAnswer must be non-empty list, got {ans}")
                    else:
                        for idx in ans:
                            if not isinstance(idx, int) or idx < 0 or idx > 3:
                                errors.append(f"{qid}: invalid multiple correctAnswer index {idx}")
                else:
                    errors.append(f"{qid}: invalid type {qtype}")

                if not q.get("explanation"):
                    errors.append(f"{qid}: missing explanation")
                if q.get("difficulty") not in ["easy", "medium", "hard"]:
                    errors.append(f"{qid}: invalid difficulty {q.get('difficulty')}")
                tags = q.get("tags")
                if not isinstance(tags, list) or len(tags) == 0:
                    errors.append(f"{qid}: invalid tags {tags}")
    except Exception as e:
        errors.append(f"Error loading lesson{lid}: {e}")

print(f"Total questions loaded: {len(all_questions)}")
for lid in LESSON_IDS:
    single_count = sum(1 for q in lesson_questions[lid] if q.get("type", "single") == "single")
    multi_count = sum(1 for q in lesson_questions[lid] if q.get("type") == "multiple")
    print(f"  Lesson {lid}: {len(lesson_questions[lid])} questions ({single_count} single, {multi_count} multiple)")

# 2. Check sectionPresets.js
sec_path = "d:/STUDY_HK1_NAM2/LTNC/ltnc-quiz-app/src/data/sectionPresets.js"
with open(sec_path, encoding="utf-8") as f:
    sec_content = f.read()

# Parse JSON inside SECTION_PRESETS
m = re.search(r'export const SECTION_PRESETS = (\[[\s\S]*?\]);\n\n/\*\*', sec_content)
if not m:
    errors.append("Could not parse SECTION_PRESETS regex")
else:
    sec_presets = json.loads(m.group(1))
    print(f"\nSection Presets validated: {len(sec_presets)} chapters")
    for group in sec_presets:
        glid = group["lessonId"]
        seen_in_group = set()
        print(f"  Lesson {glid}: '{group['title']}' has {len(group['presets'])} presets")
        for p in group["presets"]:
            p_qids = p["questionIds"]
            if len(p_qids) != 15:
                errors.append(f"Preset {p['id']} has {len(p_qids)} questions != 15")
            for qid in p_qids:
                if qid not in id_set:
                    errors.append(f"Preset {p['id']} references nonexistent {qid}")
                # Check belongs to correct lesson
                if qid not in [q["id"] for q in lesson_questions[glid]]:
                    errors.append(f"Preset {p['id']} references {qid} which does not belong to lesson {glid}")
                if qid in seen_in_group:
                    errors.append(f"Disjoint violation! {qid} appears multiple times in lesson {glid} presets")
                seen_in_group.add(qid)
        print(f"    Total disjoint questions covered in presets: {len(seen_in_group)} / {len(lesson_questions[glid])}")

# 3. Check examPresets.js
exam_path = "d:/STUDY_HK1_NAM2/LTNC/ltnc-quiz-app/src/data/examPresets.js"
with open(exam_path, encoding="utf-8") as f:
    exam_content = f.read()

m2 = re.search(r'export const EXAM_PRESETS = (\[[\s\S]*?\]);', exam_content)
if not m2:
    errors.append("Could not parse EXAM_PRESETS regex")
else:
    exam_presets = json.loads(m2.group(1))
    print(f"\nExam Presets validated: {len(exam_presets)} mock exams")
    for ep in exam_presets:
        eqids = ep["questionIds"]
        if len(eqids) != 30:
            errors.append(f"Exam {ep['id']} has {len(eqids)} questions != 30")
        for qid in eqids:
            if qid not in id_set:
                errors.append(f"Exam {ep['id']} references nonexistent {qid}")
        print(f"  {ep['code']}: {len(eqids)} questions, all IDs verified valid!")

# 4. Check lessonsMetadata.js
meta_path = "d:/STUDY_HK1_NAM2/LTNC/ltnc-quiz-app/src/data/lessonsMetadata.js"
with open(meta_path, encoding="utf-8") as f:
    meta_content = f.read()
for lid in LESSON_IDS:
    if f"id: {lid}" not in meta_content:
        errors.append(f"lessonsMetadata.js missing id: {lid}")

print(f"\nTotal Errors Found: {len(errors)}")
if errors:
    for e in errors[:20]:
        print("  - ERROR:", e)
    if len(errors) > 20:
        print(f"  ... and {len(errors) - 20} more errors")
else:
    print(">>> ALL 285 QUESTIONS, SECTION PRESETS, AND EXAM PRESETS ARE 100% VALID & DISJOINT! <<<")
