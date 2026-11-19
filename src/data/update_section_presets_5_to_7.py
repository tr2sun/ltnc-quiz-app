import json
import os

presets_file = r"D:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app\src\data\sectionPresets.js"
with open(presets_file, "r", encoding="utf-8") as f:
    content = f.read()

prefix = "import { getQuestionsByLesson } from './index.js';\n\nexport const SECTION_PRESETS = "
suffix_start = content.find("];\n\n/**")
if suffix_start == -1:
    suffix_start = content.find("];\n/**")

json_str = content[len(prefix):suffix_start + 1]
presets_data = json.loads(json_str)

new_5d_5e = [
    {
        "id": "sec-5D",
        "code": "Đề 5D",
        "title": "Bài 5 - Đề 5D (Hợp đồng equals & hashCode, Phân loại Map/Set & Fail-Fast)",
        "questionIds": [f"L5_Q{i:02d}" for i in range(46, 61)]
    },
    {
        "id": "sec-5E",
        "code": "Đề 5E",
        "title": "Bài 5 - Đề 5E (Ngoại lệ chuyên sâu, Exception Masking & Serialization)",
        "questionIds": [f"L5_Q{i:02d}" for i in range(61, 76)]
    }
]

new_6c_6d = [
    {
        "id": "sec-6C",
        "code": "Đề 6C",
        "title": "Bài 6 - Đề 6C (Creational & Structural Patterns Nâng Cao: Singleton, Factory, Builder)",
        "questionIds": [f"L6_Q{i:02d}" for i in range(31, 46)]
    },
    {
        "id": "sec-6D",
        "code": "Đề 6D",
        "title": "Bài 6 - Đề 6D (Behavioral Patterns, Kiến Trúc MVC & Nguyên Lý SOLID)",
        "questionIds": [f"L6_Q{i:02d}" for i in range(46, 61)]
    }
]

new_7c_7d = [
    {
        "id": "sec-7C",
        "code": "Đề 7C",
        "title": "Bài 7 - Đề 7C (Đồng Bộ Hóa, Monitor Lock, Giao Tiếp Luồng & volatile)",
        "questionIds": [f"L7_Q{i:02d}" for i in range(31, 46)]
    },
    {
        "id": "sec-7D",
        "code": "Đề 7D",
        "title": "Bài 7 - Đề 7D (Deadlock, ReentrantLock, ExecutorService & Concurrency)",
        "questionIds": [f"L7_Q{i:02d}" for i in range(46, 61)]
    }
]

for section in presets_data:
    if section["lessonId"] == 5:
        existing_ids = {p["id"] for p in section["presets"]}
        for p in new_5d_5e:
            if p["id"] not in existing_ids:
                section["presets"].append(p)
    elif section["lessonId"] == 6:
        existing_ids = {p["id"] for p in section["presets"]}
        for p in new_6c_6d:
            if p["id"] not in existing_ids:
                section["presets"].append(p)
    elif section["lessonId"] == 7:
        existing_ids = {p["id"] for p in section["presets"]}
        for p in new_7c_7d:
            if p["id"] not in existing_ids:
                section["presets"].append(p)

functions_code = content[suffix_start + 1:]

new_content = prefix + json.dumps(presets_data, ensure_ascii=False, indent=2) + functions_code

with open(presets_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully updated sectionPresets.js with 6 new presets for Lessons 5, 6, 7!")
