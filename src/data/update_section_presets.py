import json
import re

presets_file = r"D:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app\src\data\sectionPresets.js"
with open(presets_file, "r", encoding="utf-8") as f:
    content = f.read()

# Extract JSON portion between "export const SECTION_PRESETS = " and "];"
prefix = "import { getQuestionsByLesson } from './index.js';\n\nexport const SECTION_PRESETS = "
suffix_start = content.find("];\n\n/**")
if suffix_start == -1:
    suffix_start = content.find("];\n/**")

json_str = content[len(prefix):suffix_start + 1]
presets_data = json.loads(json_str)

new_1c_1d = [
    {
        "id": "sec-1C",
        "code": "Đề 1C",
        "title": "Bài 1 & 2 - Đề 1C (Memory Model, String Pool, Immutability & GC)",
        "questionIds": [f"L1_Q{i:02d}" for i in range(31, 46)]
    },
    {
        "id": "sec-1D",
        "code": "Đề 1D",
        "title": "Bài 1 & 2 - Đề 1D (Access Modifiers, Overloading & Constructor)",
        "questionIds": [f"L1_Q{i:02d}" for i in range(46, 61)]
    }
]

new_3d_3e = [
    {
        "id": "sec-3D",
        "code": "Đề 3D",
        "title": "Bài 3 - Đề 3D (Covariant Returns, Overriding Exceptions & Super)",
        "questionIds": [f"L3_Q{i:02d}" for i in range(46, 61)]
    },
    {
        "id": "sec-3E",
        "code": "Đề 3E",
        "title": "Bài 3 - Đề 3E (Dynamic Method Dispatch, Downcasting & Instanceof)",
        "questionIds": [f"L3_Q{i:02d}" for i in range(61, 76)]
    }
]

new_4d_4e = [
    {
        "id": "sec-4D",
        "code": "Đề 4D",
        "title": "Bài 4 - Đề 4D (Interface Default/Static/Private Methods & Conflicts)",
        "questionIds": [f"L4_Q{i:02d}" for i in range(46, 61)]
    },
    {
        "id": "sec-4E",
        "code": "Đề 4E",
        "title": "Bài 4 - Đề 4E (Advanced Generics, PECS & Type Erasure Traps)",
        "questionIds": [f"L4_Q{i:02d}" for i in range(61, 76)]
    }
]

for section in presets_data:
    if section["lessonId"] == 1:
        existing_ids = {p["id"] for p in section["presets"]}
        for p in new_1c_1d:
            if p["id"] not in existing_ids:
                section["presets"].append(p)
    elif section["lessonId"] == 3:
        existing_ids = {p["id"] for p in section["presets"]}
        for p in new_3d_3e:
            if p["id"] not in existing_ids:
                section["presets"].append(p)
    elif section["lessonId"] == 4:
        existing_ids = {p["id"] for p in section["presets"]}
        for p in new_4d_4e:
            if p["id"] not in existing_ids:
                section["presets"].append(p)

functions_code = content[suffix_start + 1:]

new_content = prefix + json.dumps(presets_data, ensure_ascii=False, indent=2) + functions_code

with open(presets_file, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully updated sectionPresets.js with 6 new presets!")
