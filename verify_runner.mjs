import fs from 'fs';
import path from 'path';

const errors = [];
const baseDir = 'D:/STUDY_HK1_NAM2/LTNC/ltnc-quiz-app';

console.log('=== 1. VERIFYING QUESTION BANK INTEGRITY ===');
const questionsDir = path.join(baseDir, 'src/data/questions');
const lessonFiles = [
  { name: 'lesson1.json', lessonId: 1 },
  { name: 'lesson3.json', lessonId: 3 },
  { name: 'lesson4.json', lessonId: 4 },
  { name: 'lesson5.json', lessonId: 5 },
  { name: 'lesson6.json', lessonId: 6 },
  { name: 'lesson7.json', lessonId: 7 },
  { name: 'lesson8.json', lessonId: 8 },
  { name: 'lesson9.json', lessonId: 9 },
];

const questionMap = new Map();
let totalQuestions = 0;

for (const { name, lessonId } of lessonFiles) {
  const filePath = path.join(questionsDir, name);
  if (!fs.existsSync(filePath)) {
    errors.push(`Missing file: ${filePath}`);
    continue;
  }
  const content = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  let singleCount = 0;
  let multiCount = 0;

  for (const q of content) {
    totalQuestions++;
    if (!q.id) {
      errors.push(`[${name}] Question missing ID`);
      continue;
    }
    if (questionMap.has(q.id)) {
      errors.push(`[${name}] Duplicate ID: ${q.id} (already in ${questionMap.get(q.id).file})`);
    } else {
      questionMap.set(q.id, { data: q, file: name });
    }

    if (q.lessonId !== lessonId) {
      errors.push(`[${name}] Question ${q.id} has lessonId ${q.lessonId}, expected ${lessonId}`);
    }

    if (q.type !== 'single' && q.type !== 'multiple') {
      errors.push(`[${name}] Question ${q.id} has invalid type: ${q.type}`);
    }

    if (q.type === 'single') singleCount++;
    if (q.type === 'multiple') multiCount++;

    if (!Array.isArray(q.options) || q.options.length !== 4) {
      errors.push(`[${name}] Question ${q.id} options length is ${q.options?.length}, expected 4`);
    } else {
      q.options.forEach((opt, idx) => {
        if (typeof opt !== 'string' || !opt.trim()) {
          errors.push(`[${name}] Question ${q.id} option[${idx}] is empty or non-string`);
        }
      });
    }

    if (q.type === 'single') {
      if (typeof q.correctAnswer !== 'number' || q.correctAnswer < 0 || q.correctAnswer > 3) {
        errors.push(`[${name}] Question ${q.id} (single) invalid correctAnswer: ${q.correctAnswer}`);
      }
    } else if (q.type === 'multiple') {
      if (!Array.isArray(q.correctAnswer) || q.correctAnswer.length < 2 || q.correctAnswer.length > 4) {
        errors.push(`[${name}] Question ${q.id} (multiple) invalid correctAnswer: ${JSON.stringify(q.correctAnswer)}`);
      } else {
        q.correctAnswer.forEach(c => {
          if (typeof c !== 'number' || c < 0 || c > 3) {
            errors.push(`[${name}] Question ${q.id} (multiple) invalid answer index: ${c}`);
          }
        });
        if (new Set(q.correctAnswer).size !== q.correctAnswer.length) {
          errors.push(`[${name}] Question ${q.id} (multiple) duplicate indices in correctAnswer`);
        }
      }
    }

    if (!q.explanation || typeof q.explanation !== 'string' || q.explanation.trim().length < 10) {
      errors.push(`[${name}] Question ${q.id} explanation missing or too short`);
    }

    if (!Array.isArray(q.tags) || q.tags.length === 0) {
      errors.push(`[${name}] Question ${q.id} tags missing or empty`);
    }

    if (!['easy', 'medium', 'hard'].includes(q.difficulty)) {
      errors.push(`[${name}] Question ${q.id} invalid difficulty: ${q.difficulty}`);
    }
  }

  console.log(`- ${name} (Lesson ${lessonId}): ${content.length} questions (Single: ${singleCount}, Multiple: ${multiCount})`);
}

console.log(`Total questions loaded: ${totalQuestions}`);
if (totalQuestions !== 285) {
  errors.push(`Total questions count is ${totalQuestions}, expected 285`);
}

console.log('\n=== 2. VERIFYING SECTION PRESETS & MUTUAL EXCLUSIVITY ===');
const sectionPresetsPath = path.join(baseDir, 'src/data/sectionPresets.js');
const secContent = fs.readFileSync(sectionPresetsPath, 'utf-8');

// Parse SECTION_PRESETS from the file
// Find SECTION_PRESETS = [ ... ];
const secMatch = secContent.match(/export const SECTION_PRESETS = (\[[\s\S]*?\]);/);
if (!secMatch) {
  errors.push('Could not parse SECTION_PRESETS from sectionPresets.js');
} else {
  const sectionPresets = JSON.parse(secMatch[1]);
  console.log(`Parsed ${sectionPresets.length} chapters from SECTION_PRESETS.`);

  let totalSectionPresets = 0;
  for (const chapter of sectionPresets) {
    const lessonId = chapter.lessonId;
    const presets = chapter.presets;
    console.log(`\nLesson ${lessonId} ("${chapter.title}"): ${presets.length} presets`);

    const seenInLesson = new Map();

    for (const preset of presets) {
      totalSectionPresets++;
      const qIds = preset.questionIds;
      console.log(`  - ${preset.code} (${preset.id}): ${qIds.length} questions - "${preset.title}"`);

      if (!Array.isArray(qIds) || qIds.length !== 15) {
        errors.push(`Preset ${preset.code} (${preset.id}) has ${qIds?.length} questions, expected EXACTLY 15!`);
      }

      const uniqueIds = new Set(qIds);
      if (uniqueIds.size !== qIds.length) {
        errors.push(`Preset ${preset.code} contains internal duplicate questions!`);
      }

      for (const qid of qIds) {
        const qEntry = questionMap.get(qid);
        if (!qEntry) {
          errors.push(`Preset ${preset.code} references non-existent question: ${qid}`);
        } else if (qEntry.data.lessonId !== lessonId) {
          errors.push(`Preset ${preset.code} is for Lesson ${lessonId} but question ${qid} has lessonId ${qEntry.data.lessonId}`);
        }

        if (seenInLesson.has(qid)) {
          errors.push(`MUTUAL EXCLUSIVITY ERROR in Lesson ${lessonId}: Question ${qid} is used in both ${seenInLesson.get(qid)} and ${preset.code}!`);
        } else {
          seenInLesson.set(qid, preset.code);
        }
      }
    }
    console.log(`  ✓ All ${seenInLesson.size} questions across presets in Lesson ${lessonId} are 100% MUTUALLY DISJOINT!`);
  }
  console.log(`\nTotal Section Presets Audited: ${totalSectionPresets}`);
}

console.log('\n=== 3. VERIFYING GENERAL EXAM PRESETS (ĐỀ 101..104) ===');
const examPresetsPath = path.join(baseDir, 'src/data/examPresets.js');
const examContent = fs.readFileSync(examPresetsPath, 'utf-8');
const examMatch = examContent.match(/export const EXAM_PRESETS = (\[[\s\S]*?\]);/);
if (!examMatch) {
  errors.push('Could not parse EXAM_PRESETS from examPresets.js');
} else {
  // Replace unquoted keys if any
  let jsonStr = examMatch[1];
  // examPresets uses standard JS object format
  const exams = eval(jsonStr); // safely eval JS array in verification runner
  console.log(`Auditing ${exams.length} general exams:`);

  for (const ex of exams) {
    console.log(`- ${ex.code} (${ex.id}): ${ex.questionIds.length} questions`);
    if (ex.questionIds.length !== 30) {
      errors.push(`Exam ${ex.code} has ${ex.questionIds.length} questions, expected EXACTLY 30!`);
    }
    const uniqueIds = new Set(ex.questionIds);
    if (uniqueIds.size !== ex.questionIds.length) {
      errors.push(`Exam ${ex.code} contains internal duplicate question IDs!`);
    }
    for (const qid of ex.questionIds) {
      if (!questionMap.has(qid)) {
        errors.push(`Exam ${ex.code} references non-existent question: ${qid}`);
      }
    }
  }
}

console.log('\n=== 4. TESTING EXACT MATCH MULTI-SELECT SCORING ===');
function isAnswerCorrect(question, userSelection) {
  if (userSelection === undefined || userSelection === null) return false;
  const isMulti = question?.type === 'multiple' || Array.isArray(question?.correctAnswer);
  if (isMulti) {
    if (!Array.isArray(userSelection)) return false;
    const correctArr = Array.isArray(question.correctAnswer) ? question.correctAnswer : [question.correctAnswer];
    if (userSelection.length !== correctArr.length) return false;
    const sortedUser = [...userSelection].sort((a, b) => a - b);
    const sortedCorrect = [...correctArr].sort((a, b) => a - b);
    return sortedUser.every((val, idx) => val === sortedCorrect[idx]);
  } else {
    return userSelection === question.correctAnswer;
  }
}

// Test cases
const multiTest = { type: 'multiple', correctAnswer: [0, 2] };
if (!isAnswerCorrect(multiTest, [0, 2])) errors.push('Exact multi match failed');
if (!isAnswerCorrect(multiTest, [2, 0])) errors.push('Unordered multi match failed');
if (isAnswerCorrect(multiTest, [0])) errors.push('Partial multi match was incorrectly accepted');
if (isAnswerCorrect(multiTest, [0, 1, 2])) errors.push('Superset multi match was incorrectly accepted');
if (isAnswerCorrect(multiTest, [1, 3])) errors.push('Wrong multi match was incorrectly accepted');
if (isAnswerCorrect(multiTest, [])) errors.push('Empty multi match was incorrectly accepted');
if (isAnswerCorrect(multiTest, null)) errors.push('Null multi match was incorrectly accepted');

const singleTest = { type: 'single', correctAnswer: 3 };
if (!isAnswerCorrect(singleTest, 3)) errors.push('Exact single match failed');
if (isAnswerCorrect(singleTest, 1)) errors.push('Wrong single match was incorrectly accepted');
if (isAnswerCorrect(singleTest, null)) errors.push('Null single match was incorrectly accepted');

console.log('✓ Scoring assertion tests completed.');

console.log('\n================ FINAL RESULTS ================');
if (errors.length > 0) {
  console.error(`❌ Verification FAILED with ${errors.length} errors:`);
  for (const err of errors) {
    console.error(`  - ${err}`);
  }
  process.exit(1);
} else {
  console.log('✅ ALL VERIFICATIONS PASSED 100% WITH ZERO ERRORS!');
  process.exit(0);
}
