import json
import re

presets_path = r'D:\STUDY_HK1_NAM2\LTNC\ltnc-quiz-app\src\data\sectionPresets.js'

with open(presets_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define the presets to add
new_presets_8 = [
    {
        "id": "sec-8C",
        "code": "Đề 8C",
        "title": "Bài 8 - Đề 8C (Kiểm Thử JUnit 5 Chuyên Sâu, Vòng Đời Test & BVA)",
        "questionIds": [f"L8_Q{i:02d}" for i in range(31, 46)]
    },
    {
        "id": "sec-8D",
        "code": "Đề 8D",
        "title": "Bài 8 - Đề 8D (Nhận Diện Code Smells & Kỹ Thuật Tái Cấu Trúc Chuẩn Fowler)",
        "questionIds": [f"L8_Q{i:02d}" for i in range(46, 61)]
    }
]

new_presets_9 = [
    {
        "id": "sec-9C",
        "code": "Đề 9C",
        "title": "Bài 9 - Đề 9C (Vòng Đời Xây Dựng Maven/Gradle & Quản Lý Dependencies)",
        "questionIds": [f"L9_Q{i:02d}" for i in range(31, 46)]
    },
    {
        "id": "sec-9D",
        "code": "Đề 9D",
        "title": "Bài 9 - Đề 9D (Git Workflows, Checkstyle & Tự Động Hóa CI/CD Pipeline)",
        "questionIds": [f"L9_Q{i:02d}" for i in range(46, 61)]
    }
]

def format_preset(p):
    q_str = ",\n".join(f'          "{qid}"' for qid in p["questionIds"])
    return f'''      {{
        "id": "{p["id"]}",
        "code": "{p["code"]}",
        "title": "{p["title"]}",
        "questionIds": [
{q_str}
        ]
      }}'''

formatted_8 = ",\n" + ",\n".join(format_preset(p) for p in new_presets_8)
formatted_9 = ",\n" + ",\n".join(format_preset(p) for p in new_presets_9)

# Insert formatted_8 right after sec-8B
target_8B_end = '''        "questionIds": [
          "L8_Q16",
          "L8_Q17",
          "L8_Q18",
          "L8_Q19",
          "L8_Q20",
          "L8_Q21",
          "L8_Q22",
          "L8_Q23",
          "L8_Q24",
          "L8_Q25",
          "L8_Q26",
          "L8_Q27",
          "L8_Q28",
          "L8_Q29",
          "L8_Q30"
        ]
      }'''

if target_8B_end not in content:
    raise Exception("Target 8B not found!")

content = content.replace(target_8B_end, target_8B_end + formatted_8, 1)

# Insert formatted_9 right after sec-9B
target_9B_end = '''        "questionIds": [
          "L9_Q16",
          "L9_Q17",
          "L9_Q18",
          "L9_Q19",
          "L9_Q20",
          "L9_Q21",
          "L9_Q22",
          "L9_Q23",
          "L9_Q24",
          "L9_Q25",
          "L9_Q26",
          "L9_Q27",
          "L9_Q28",
          "L9_Q29",
          "L9_Q30"
        ]
      }'''

if target_9B_end not in content:
    raise Exception("Target 9B not found!")

content = content.replace(target_9B_end, target_9B_end + formatted_9, 1)

with open(presets_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated sectionPresets.js with sec-8C, sec-8D, sec-9C, sec-9D!")
