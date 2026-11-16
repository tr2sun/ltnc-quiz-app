# -*- coding: utf-8 -*-
"""
Curriculum and Question Bank Generator for LTNC (UET.CS2043)
Generates 20 questions per lesson (10 theory + 10 code) for all 9 lessons (180 questions total).
"""

import json
import os

OUTPUT_DIR = r"d:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app\src\data\questions"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Helper function to save question file
def save_lesson(lesson_id, questions):
    filepath = os.path.join(OUTPUT_DIR, f"lesson{lesson_id}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved lesson{lesson_id}.json: {len(questions)} questions")
