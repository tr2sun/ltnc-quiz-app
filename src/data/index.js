import { LESSONS_METADATA } from './lessonsMetadata.js';
import { CHEAT_SHEETS } from './cheatSheetData.js';
import { EXAM_PRESETS } from './examPresets.js';

import lesson1 from './questions/lesson1.json';
import lesson2 from './questions/lesson2.json';
import lesson3 from './questions/lesson3.json';
import lesson4 from './questions/lesson4.json';
import lesson5 from './questions/lesson5.json';
import lesson6 from './questions/lesson6.json';
import lesson7 from './questions/lesson7.json';
import lesson8 from './questions/lesson8.json';
import lesson9 from './questions/lesson9.json';

const ALL_LESSON_FILES = {
  1: lesson1,
  2: lesson2,
  3: lesson3,
  4: lesson4,
  5: lesson5,
  6: lesson6,
  7: lesson7,
  8: lesson8,
  9: lesson9
};

export { LESSONS_METADATA, CHEAT_SHEETS, EXAM_PRESETS };

/**
 * Get all questions across all lessons
 */
export function getAllQuestions() {
  const all = [];
  for (let i = 1; i <= 9; i++) {
    const list = ALL_LESSON_FILES[i] || [];
    all.push(...list);
  }
  return all;
}

/**
 * Get questions by lesson ID (1 to 9)
 */
export function getQuestionsByLesson(lessonId) {
  const numId = Number(lessonId);
  return ALL_LESSON_FILES[numId] || [];
}

/**
 * Find question by unique ID
 */
export function getQuestionById(id) {
  const all = getAllQuestions();
  return all.find(q => q.id === id) || null;
}

/**
 * Get questions for an exam preset (or fallback balanced selection of 30 questions)
 */
export function getExamQuestions(presetId, count = 30) {
  const all = getAllQuestions();
  const preset = EXAM_PRESETS.find(p => p.id === presetId);

  if (preset && preset.questionIds && preset.questionIds.length > 0) {
    const matched = [];
    for (const qid of preset.questionIds) {
      const q = all.find(item => item.id === qid);
      if (q) matched.push(q);
    }
    if (matched.length >= count) {
      return matched.slice(0, count);
    }
    // If some ids are missing, fill up from remaining pool
    const remaining = all.filter(q => !matched.some(m => m.id === q.id));
    const shuffledRemaining = [...remaining].sort(() => 0.5 - Math.random());
    return [...matched, ...shuffledRemaining].slice(0, count);
  }

  // Otherwise, construct a balanced random 30-question mock exam
  // Aim for ~3-4 questions per lesson
  const selected = [];
  const perLesson = Math.max(1, Math.floor(count / 9));

  for (let i = 1; i <= 9; i++) {
    const lessonList = [...(ALL_LESSON_FILES[i] || [])].sort(() => 0.5 - Math.random());
    selected.push(...lessonList.slice(0, perLesson));
  }

  // Fill up if we have less than count
  if (selected.length < count && all.length > selected.length) {
    const selectedIds = new Set(selected.map(q => q.id));
    const rest = all.filter(q => !selectedIds.has(q.id)).sort(() => 0.5 - Math.random());
    selected.push(...rest.slice(0, count - selected.length));
  }

  return selected.sort(() => 0.5 - Math.random());
}
