# -*- coding: utf-8 -*-
import json
import os
import re

data_dir = r"d:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app\src\data"

# 1. Load questions
all_questions = {}
for i in range(1, 10):
    fpath = os.path.join(data_dir, "questions", f"lesson{i}.json")
    assert os.path.exists(fpath), f"Missing {fpath}"
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Lesson {i}: {len(data)} questions")
    assert len(data) == 20, f"Lesson {i} count != 20"
    theory = sum(1 for q in data if q["code"] is None)
    code = sum(1 for q in data if q["code"] is not None)
    assert theory == 10 and code == 10, f"Lesson {i} ratio not 50/50: theory={theory}, code={code}"
    for q in data:
        assert q["id"] not in all_questions, f"Duplicate id {q['id']}"
        assert len(q["options"]) == 4, f"{q['id']} options != 4"
        assert 0 <= q["correctAnswer"] <= 3, f"{q['id']} invalid correctAnswer"
        assert q["title"], f"{q['id']} empty title"
        assert q["explanation"], f"{q['id']} empty explanation"
        all_questions[q["id"]] = q

print(f"Total questions across all lessons: {len(all_questions)}")

# 2. Check examPresets.js
with open(os.path.join(data_dir, "examPresets.js"), "r", encoding="utf-8") as f:
    text = f.read()

presets = re.findall(r'id:\s*"([^"]+)".*?code:\s*"([^"]+)".*?questionIds:\s*\[(.*?)\]', text, re.DOTALL)
print(f"Found {len(presets)} exam presets")
for pid, code, qids_str in presets:
    qids = re.findall(r'"([^"]+)"', qids_str)
    print(f"Preset {code} ({pid}): {len(qids)} questions")
    assert len(qids) == 30, f"Preset {code} does not have exactly 30 questions! (has {len(qids)})"
    lessons_covered = set()
    for qid in qids:
        assert qid in all_questions, f"Question {qid} in preset {code} not found in questions!"
        lessons_covered.add(all_questions[qid]["lessonId"])
    print(f"  Lessons covered ({len(lessons_covered)}): {sorted(list(lessons_covered))}")
    assert len(lessons_covered) == 9, f"Preset {code} does not cover all 9 lessons!"

# 3. Check cheatSheetData.js
with open(os.path.join(data_dir, "cheatSheetData.js"), "r", encoding="utf-8") as f:
    cs_text = f.read()
cs_cards = re.findall(r'id:\s*"([^"]+)"', cs_text)
print(f"Cheat Sheet Cards ({len(cs_cards)}): {cs_cards}")
assert len(cs_cards) >= 6, "Cheat sheet cards count < 6"

# 4. Check lessonsMetadata.js
with open(os.path.join(data_dir, "lessonsMetadata.js"), "r", encoding="utf-8") as f:
    lm_text = f.read()
lm_ids = re.findall(r'id:\s*(\d+)', lm_text)
print(f"Lessons in metadata ({len(lm_ids)}): {lm_ids}")
assert len(lm_ids) == 9, "Metadata does not contain 9 lessons!"

print("\n>>> ALL VALIDATION CHECKS PASSED 100% SUCCESSFULLY! <<<")
