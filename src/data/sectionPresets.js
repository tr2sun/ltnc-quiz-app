import { getQuestionsByLesson } from './index.js';

export const SECTION_PRESETS = [
  {
    "lessonId": 1,
    "title": "Bài 1 & 2: Cơ bản Java & OOP",
    "presets": [
      {
        "id": "sec-1A",
        "code": "Đề 1A",
        "title": "Bài 1 & 2 - Đề 1A (Cơ bản cú pháp, JVM, Modifiers & OOP)",
        "questionIds": [
          "L1_Q01",
          "L1_Q02",
          "L1_Q03",
          "L1_Q04",
          "L1_Q05",
          "L1_Q06",
          "L1_Q07",
          "L1_Q08",
          "L1_Q09",
          "L1_Q10",
          "L1_Q11",
          "L1_Q12",
          "L1_Q13",
          "L1_Q14",
          "L1_Q15"
        ]
      },
      {
        "id": "sec-1B",
        "code": "Đề 1B",
        "title": "Bài 1 & 2 - Đề 1B (Stack/Heap, GC, Constructor Chaining & Static)",
        "questionIds": [
          "L1_Q16",
          "L1_Q17",
          "L1_Q18",
          "L1_Q19",
          "L1_Q20",
          "L1_Q21",
          "L1_Q22",
          "L1_Q23",
          "L1_Q24",
          "L1_Q25",
          "L1_Q26",
          "L1_Q27",
          "L1_Q28",
          "L1_Q29",
          "L1_Q30"
        ]
      },
      {
        "id": "sec-1C",
        "code": "Đề 1C",
        "title": "Bài 1 & 2 - Đề 1C (Memory Model, String Pool, Immutability & GC)",
        "questionIds": [
          "L1_Q31",
          "L1_Q32",
          "L1_Q33",
          "L1_Q34",
          "L1_Q35",
          "L1_Q36",
          "L1_Q37",
          "L1_Q38",
          "L1_Q39",
          "L1_Q40",
          "L1_Q41",
          "L1_Q42",
          "L1_Q43",
          "L1_Q44",
          "L1_Q45"
        ]
      },
      {
        "id": "sec-1D",
        "code": "Đề 1D",
        "title": "Bài 1 & 2 - Đề 1D (Access Modifiers, Overloading & Constructor)",
        "questionIds": [
          "L1_Q46",
          "L1_Q47",
          "L1_Q48",
          "L1_Q49",
          "L1_Q50",
          "L1_Q51",
          "L1_Q52",
          "L1_Q53",
          "L1_Q54",
          "L1_Q55",
          "L1_Q56",
          "L1_Q57",
          "L1_Q58",
          "L1_Q59",
          "L1_Q60"
        ]
      }
    ]
  },
  {
    "lessonId": 3,
    "title": "Bài 3: Thừa kế & Đa hình",
    "presets": [
      {
        "id": "sec-3A",
        "code": "Đề 3A",
        "title": "Bài 3 - Đề 3A (Inheritance, Constructor Chaining & Super)",
        "questionIds": [
          "L3_Q01",
          "L3_Q02",
          "L3_Q03",
          "L3_Q04",
          "L3_Q05",
          "L3_Q06",
          "L3_Q07",
          "L3_Q08",
          "L3_Q09",
          "L3_Q10",
          "L3_Q11",
          "L3_Q12",
          "L3_Q13",
          "L3_Q14",
          "L3_Q15"
        ]
      },
      {
        "id": "sec-3B",
        "code": "Đề 3B",
        "title": "Bài 3 - Đề 3B (Polymorphism, Dynamic Binding & Static Hiding)",
        "questionIds": [
          "L3_Q16",
          "L3_Q17",
          "L3_Q18",
          "L3_Q19",
          "L3_Q20",
          "L3_Q21",
          "L3_Q22",
          "L3_Q23",
          "L3_Q24",
          "L3_Q25",
          "L3_Q26",
          "L3_Q27",
          "L3_Q28",
          "L3_Q29",
          "L3_Q30"
        ]
      },
      {
        "id": "sec-3C",
        "code": "Đề 3C",
        "title": "Bài 3 - Đề 3C (Casting, instanceof, Object Slicing & Tricky Code)",
        "questionIds": [
          "L3_Q31",
          "L3_Q32",
          "L3_Q33",
          "L3_Q34",
          "L3_Q35",
          "L3_Q36",
          "L3_Q37",
          "L3_Q38",
          "L3_Q39",
          "L3_Q40",
          "L3_Q41",
          "L3_Q42",
          "L3_Q43",
          "L3_Q44",
          "L3_Q45"
        ]
      },
      {
        "id": "sec-3D",
        "code": "Đề 3D",
        "title": "Bài 3 - Đề 3D (Covariant Returns, Overriding Exceptions & Super)",
        "questionIds": [
          "L3_Q46",
          "L3_Q47",
          "L3_Q48",
          "L3_Q49",
          "L3_Q50",
          "L3_Q51",
          "L3_Q52",
          "L3_Q53",
          "L3_Q54",
          "L3_Q55",
          "L3_Q56",
          "L3_Q57",
          "L3_Q58",
          "L3_Q59",
          "L3_Q60"
        ]
      },
      {
        "id": "sec-3E",
        "code": "Đề 3E",
        "title": "Bài 3 - Đề 3E (Dynamic Method Dispatch, Downcasting & Instanceof)",
        "questionIds": [
          "L3_Q61",
          "L3_Q62",
          "L3_Q63",
          "L3_Q64",
          "L3_Q65",
          "L3_Q66",
          "L3_Q67",
          "L3_Q68",
          "L3_Q69",
          "L3_Q70",
          "L3_Q71",
          "L3_Q72",
          "L3_Q73",
          "L3_Q74",
          "L3_Q75"
        ]
      }
    ]
  },
  {
    "lessonId": 4,
    "title": "Bài 4: Interface & Generics",
    "presets": [
      {
        "id": "sec-4A",
        "code": "Đề 4A",
        "title": "Bài 4 - Đề 4A (Abstract Class & Interface Rules)",
        "questionIds": [
          "L4_Q01",
          "L4_Q02",
          "L4_Q03",
          "L4_Q04",
          "L4_Q05",
          "L4_Q06",
          "L4_Q07",
          "L4_Q08",
          "L4_Q09",
          "L4_Q10",
          "L4_Q11",
          "L4_Q12",
          "L4_Q13",
          "L4_Q14",
          "L4_Q15"
        ]
      },
      {
        "id": "sec-4B",
        "code": "Đề 4B",
        "title": "Bài 4 - Đề 4B (Default/Static/Private Methods in Interface)",
        "questionIds": [
          "L4_Q16",
          "L4_Q17",
          "L4_Q18",
          "L4_Q19",
          "L4_Q20",
          "L4_Q21",
          "L4_Q22",
          "L4_Q23",
          "L4_Q24",
          "L4_Q25",
          "L4_Q26",
          "L4_Q27",
          "L4_Q28",
          "L4_Q29",
          "L4_Q30"
        ]
      },
      {
        "id": "sec-4C",
        "code": "Đề 4C",
        "title": "Bài 4 - Đề 4C (Generics, Type Erasure & PECS Principle)",
        "questionIds": [
          "L4_Q31",
          "L4_Q32",
          "L4_Q33",
          "L4_Q34",
          "L4_Q35",
          "L4_Q36",
          "L4_Q37",
          "L4_Q38",
          "L4_Q39",
          "L4_Q40",
          "L4_Q41",
          "L4_Q42",
          "L4_Q43",
          "L4_Q44",
          "L4_Q45"
        ]
      },
      {
        "id": "sec-4D",
        "code": "Đề 4D",
        "title": "Bài 4 - Đề 4D (Interface Default/Static/Private Methods & Conflicts)",
        "questionIds": [
          "L4_Q46",
          "L4_Q47",
          "L4_Q48",
          "L4_Q49",
          "L4_Q50",
          "L4_Q51",
          "L4_Q52",
          "L4_Q53",
          "L4_Q54",
          "L4_Q55",
          "L4_Q56",
          "L4_Q57",
          "L4_Q58",
          "L4_Q59",
          "L4_Q60"
        ]
      },
      {
        "id": "sec-4E",
        "code": "Đề 4E",
        "title": "Bài 4 - Đề 4E (Advanced Generics, PECS & Type Erasure Traps)",
        "questionIds": [
          "L4_Q61",
          "L4_Q62",
          "L4_Q63",
          "L4_Q64",
          "L4_Q65",
          "L4_Q66",
          "L4_Q67",
          "L4_Q68",
          "L4_Q69",
          "L4_Q70",
          "L4_Q71",
          "L4_Q72",
          "L4_Q73",
          "L4_Q74",
          "L4_Q75"
        ]
      }
    ]
  },
  {
    "lessonId": 5,
    "title": "Bài 5: Collections, Exception & I/O",
    "presets": [
      {
        "id": "sec-5A",
        "code": "Đề 5A",
        "title": "Bài 5 - Đề 5A (Collections, List, Set, Map, equals & hashCode)",
        "questionIds": [
          "L5_Q01",
          "L5_Q02",
          "L5_Q03",
          "L5_Q04",
          "L5_Q05",
          "L5_Q06",
          "L5_Q07",
          "L5_Q08",
          "L5_Q09",
          "L5_Q10",
          "L5_Q11",
          "L5_Q12",
          "L5_Q13",
          "L5_Q14",
          "L5_Q15"
        ]
      },
      {
        "id": "sec-5B",
        "code": "Đề 5B",
        "title": "Bài 5 - Đề 5B (Exceptions Hierarchy, try-catch-finally, AutoCloseable)",
        "questionIds": [
          "L5_Q16",
          "L5_Q17",
          "L5_Q18",
          "L5_Q19",
          "L5_Q20",
          "L5_Q21",
          "L5_Q22",
          "L5_Q23",
          "L5_Q24",
          "L5_Q25",
          "L5_Q26",
          "L5_Q27",
          "L5_Q28",
          "L5_Q29",
          "L5_Q30"
        ]
      },
      {
        "id": "sec-5C",
        "code": "Đề 5C",
        "title": "Bài 5 - Đề 5C (I/O Streams, Serialization, transient, File Handling)",
        "questionIds": [
          "L5_Q31",
          "L5_Q32",
          "L5_Q33",
          "L5_Q34",
          "L5_Q35",
          "L5_Q36",
          "L5_Q37",
          "L5_Q38",
          "L5_Q39",
          "L5_Q40",
          "L5_Q41",
          "L5_Q42",
          "L5_Q43",
          "L5_Q44",
          "L5_Q45"
        ]
      }
    ]
  },
  {
    "lessonId": 6,
    "title": "Bài 6: Mẫu thiết kế (Design Patterns)",
    "presets": [
      {
        "id": "sec-6A",
        "code": "Đề 6A",
        "title": "Bài 6 - Đề 6A (Creational & Structural Patterns: Singleton, Factory, Adapter, Decorator)",
        "questionIds": [
          "L6_Q01",
          "L6_Q02",
          "L6_Q03",
          "L6_Q04",
          "L6_Q05",
          "L6_Q06",
          "L6_Q07",
          "L6_Q08",
          "L6_Q09",
          "L6_Q10",
          "L6_Q11",
          "L6_Q12",
          "L6_Q13",
          "L6_Q14",
          "L6_Q15"
        ]
      },
      {
        "id": "sec-6B",
        "code": "Đề 6B",
        "title": "Bài 6 - Đề 6B (Behavioral Patterns & MVC: Strategy, Observer, Composite, SOLID)",
        "questionIds": [
          "L6_Q16",
          "L6_Q17",
          "L6_Q18",
          "L6_Q19",
          "L6_Q20",
          "L6_Q21",
          "L6_Q22",
          "L6_Q23",
          "L6_Q24",
          "L6_Q25",
          "L6_Q26",
          "L6_Q27",
          "L6_Q28",
          "L6_Q29",
          "L6_Q30"
        ]
      }
    ]
  },
  {
    "lessonId": 7,
    "title": "Bài 7: Đa luồng (Multithreading)",
    "presets": [
      {
        "id": "sec-7A",
        "code": "Đề 7A",
        "title": "Bài 7 - Đề 7A (Thread Lifecycle, Runnable vs Callable, Daemon)",
        "questionIds": [
          "L7_Q01",
          "L7_Q02",
          "L7_Q03",
          "L7_Q04",
          "L7_Q05",
          "L7_Q06",
          "L7_Q07",
          "L7_Q08",
          "L7_Q09",
          "L7_Q10",
          "L7_Q11",
          "L7_Q12",
          "L7_Q13",
          "L7_Q14",
          "L7_Q15"
        ]
      },
      {
        "id": "sec-7B",
        "code": "Đề 7B",
        "title": "Bài 7 - Đề 7B (Synchronization, Monitor Lock, Deadlock & Thread Pools)",
        "questionIds": [
          "L7_Q16",
          "L7_Q17",
          "L7_Q18",
          "L7_Q19",
          "L7_Q20",
          "L7_Q21",
          "L7_Q22",
          "L7_Q23",
          "L7_Q24",
          "L7_Q25",
          "L7_Q26",
          "L7_Q27",
          "L7_Q28",
          "L7_Q29",
          "L7_Q30"
        ]
      }
    ]
  },
  {
    "lessonId": 8,
    "title": "Bài 8: Kiểm thử & Tái cấu trúc",
    "presets": [
      {
        "id": "sec-8A",
        "code": "Đề 8A",
        "title": "Bài 8 - Đề 8A (JUnit 5, Black-box Testing, BVA, Equivalence Partitioning)",
        "questionIds": [
          "L8_Q01",
          "L8_Q02",
          "L8_Q03",
          "L8_Q04",
          "L8_Q05",
          "L8_Q06",
          "L8_Q07",
          "L8_Q08",
          "L8_Q09",
          "L8_Q10",
          "L8_Q11",
          "L8_Q12",
          "L8_Q13",
          "L8_Q14",
          "L8_Q15"
        ]
      },
      {
        "id": "sec-8B",
        "code": "Đề 8B",
        "title": "Bài 8 - Đề 8B (Code Smells, Refactoring Techniques & Best Practices)",
        "questionIds": [
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
      }
    ]
  },
  {
    "lessonId": 9,
    "title": "Bài 9: Tích hợp & Triển khai (CI/CD)",
    "presets": [
      {
        "id": "sec-9A",
        "code": "Đề 9A",
        "title": "Bài 9 - Đề 9A (Maven Lifecycle, Dependency Scopes, Checkstyle & Static Analysis)",
        "questionIds": [
          "L9_Q01",
          "L9_Q02",
          "L9_Q03",
          "L9_Q04",
          "L9_Q05",
          "L9_Q06",
          "L9_Q07",
          "L9_Q08",
          "L9_Q09",
          "L9_Q10",
          "L9_Q11",
          "L9_Q12",
          "L9_Q13",
          "L9_Q14",
          "L9_Q15"
        ]
      },
      {
        "id": "sec-9B",
        "code": "Đề 9B",
        "title": "Bài 9 - Đề 9B (Git Workflows, Branching, CI/CD Pipeline & GitHub Actions)",
        "questionIds": [
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
      }
    ]
  }
];

/**
 * Get presets for a specific lesson
 */
export function getPresetsForLesson(lessonId) {
  const numId = Number(lessonId);
  const found = SECTION_PRESETS.find(s => s.lessonId === numId);
  return found ? found.presets : [];
}

/**
 * Get 15 questions for a section preset (or random 15 questions for that lesson)
 */
export function getSectionQuestions(lessonId, presetId = 'random') {
  const lessonQuestions = getQuestionsByLesson(lessonId);
  if (!lessonQuestions || lessonQuestions.length === 0) return [];

  if (presetId && presetId !== 'random') {
    // Look up preset in SECTION_PRESETS
    for (const group of SECTION_PRESETS) {
      const match = group.presets.find(p => p.id === presetId);
      if (match && match.questionIds && match.questionIds.length > 0) {
        const found = match.questionIds.map(qid => lessonQuestions.find(q => q.id === qid)).filter(Boolean);
        if (found.length >= 15) return found.slice(0, 15);
      }
    }
  }

  // Fallback or random: shuffle and take 15
  const shuffled = [...lessonQuestions].sort(() => 0.5 - Math.random());
  return shuffled.slice(0, Math.min(15, shuffled.length));
}
