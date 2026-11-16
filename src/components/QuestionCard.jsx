import React, { useState } from 'react';
import { Bookmark, HelpCircle, CheckCircle2, XCircle, AlertCircle, Sparkles, CheckSquare, Square, Check } from 'lucide-react';
import CodeBlock from './CodeBlock';

const OPTION_LABELS = ['A', 'B', 'C', 'D'];

/**
 * Check if the user's answer is completely correct.
 * For multiple-select: exact match (no missing, no extra).
 */
export function isAnswerCorrect(question, userSelection) {
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

export default function QuestionCard({
  question,
  questionIndex = 0,
  selectedAnswer = null,
  onSelectAnswer,
  mode = 'practice', // 'practice' | 'exam' | 'review'
  showInstantFeedback = true,
  isBookmarked = false,
  onToggleBookmark,
}) {
  const [showManualExplanation, setShowManualExplanation] = useState(false);
  const [confirmedMultiPractice, setConfirmedMultiPractice] = useState(false);

  if (!question) return null;

  const isMulti = question.type === 'multiple' || Array.isArray(question.correctAnswer);
  const correctAnswersList = Array.isArray(question.correctAnswer)
    ? question.correctAnswer
    : [question.correctAnswer];

  // Selected array representation
  const selectedList = isMulti
    ? (Array.isArray(selectedAnswer) ? selectedAnswer : [])
    : (selectedAnswer !== null && selectedAnswer !== undefined ? [selectedAnswer] : []);

  const isAnswered = isMulti ? selectedList.length > 0 : selectedAnswer !== null && selectedAnswer !== undefined;
  const isCorrect = isAnswerCorrect(question, selectedAnswer);

  const isExam = mode === 'exam';
  const isReview = mode === 'review';
  const isPractice = mode === 'practice';

  // For multi-select in practice mode, reveal when user clicked confirm or instant feedback enabled
  const shouldReveal = isReview || 
    (isPractice && isAnswered && showInstantFeedback && (!isMulti || confirmedMultiPractice)) || 
    showManualExplanation;

  const handleOptionClick = (optIndex) => {
    if (isReview) return;

    if (isMulti) {
      let updated;
      if (selectedList.includes(optIndex)) {
        updated = selectedList.filter(i => i !== optIndex);
      } else {
        updated = [...selectedList, optIndex].sort((a, b) => a - b);
      }
      onSelectAnswer(updated);
    } else {
      onSelectAnswer(optIndex);
    }
  };

  const difficultyColors = {
    easy: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300 border-emerald-300 dark:border-emerald-800',
    medium: 'bg-amber-100 text-amber-800 dark:bg-amber-950/60 dark:text-amber-300 border-amber-300 dark:border-amber-800',
    hard: 'bg-rose-100 text-rose-800 dark:bg-rose-950/60 dark:text-rose-300 border-rose-300 dark:border-rose-800'
  };

  const difficultyLabels = {
    easy: 'Dễ',
    medium: 'Trung bình',
    hard: 'Nâng cao'
  };

  return (
    <div
      id={`question-${question.id}`}
      className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm hover:shadow-md transition-shadow p-5 md:p-6 mb-6"
    >
      {/* Top Bar: Question Index, Badges, Bookmark Flag */}
      <div className="flex items-center justify-between gap-2 mb-4 pb-3 border-b border-slate-100 dark:border-slate-800">
        <div className="flex items-center flex-wrap gap-2">
          <span className="font-bold text-base md:text-lg text-slate-800 dark:text-slate-100">
            Câu {questionIndex + 1}
          </span>
          <span className="text-xs text-slate-400 font-mono px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800">
            {question.id}
          </span>

          {/* Type Badge: Single vs Multiple */}
          {isMulti ? (
            <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-purple-100 text-purple-700 dark:bg-purple-950 dark:text-purple-300 border border-purple-300 dark:border-purple-800 flex items-center gap-1">
              <CheckSquare size={12} />
              <span>Chọn nhiều đáp án</span>
            </span>
          ) : (
            <span className="text-[11px] font-medium px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-400">
              Chọn 1 đáp án
            </span>
          )}

          {question.difficulty && (
            <span
              className={`text-[11px] font-semibold px-2 py-0.5 rounded-full border ${
                difficultyColors[question.difficulty] || difficultyColors.medium
              }`}
            >
              {difficultyLabels[question.difficulty] || question.difficulty}
            </span>
          )}

          {question.tags && question.tags.length > 0 && (
            <div className="hidden sm:flex items-center gap-1">
              {question.tags.slice(0, 2).map((t, idx) => (
                <span
                  key={idx}
                  className="text-[11px] font-medium px-2 py-0.5 rounded bg-indigo-50 dark:bg-indigo-950/50 text-indigo-600 dark:text-indigo-400"
                >
                  #{t}
                </span>
              ))}
            </div>
          )}
        </div>

        <button
          onClick={onToggleBookmark}
          className={`flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-xs font-medium transition-colors cursor-pointer ${
            isBookmarked
              ? 'bg-amber-100 text-amber-700 dark:bg-amber-950/80 dark:text-amber-300 border border-amber-300 dark:border-amber-700'
              : 'text-slate-400 hover:text-slate-600 dark:hover:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
          }`}
          title={isBookmarked ? 'Bỏ đánh dấu câu hỏi' : 'Đánh dấu để xem lại'}
        >
          <Bookmark size={15} className={isBookmarked ? 'fill-current' : ''} />
          <span className="hidden sm:inline">{isBookmarked ? 'Đã ghim' : 'Ghim'}</span>
        </button>
      </div>

      {/* Question Title */}
      <h3 className="text-slate-800 dark:text-slate-100 font-medium text-base md:text-lg leading-relaxed mb-3">
        {question.title}
      </h3>

      {/* Code Snippet (if any) */}
      {question.code && (
        <CodeBlock code={question.code} language="java" title={`Mã nguồn - Câu ${questionIndex + 1}`} />
      )}

      {/* Options List */}
      <div className="space-y-2.5 my-4">
        {question.options.map((optionText, optIndex) => {
          const isChosen = selectedList.includes(optIndex);
          const isTheCorrectOption = correctAnswersList.includes(optIndex);

          let optionStyle =
            'border-slate-200 dark:border-slate-800 hover:border-indigo-300 dark:hover:border-indigo-700 bg-white dark:bg-slate-800/60 text-slate-700 dark:text-slate-200';
          let badgeStyle =
            'bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border-slate-300 dark:border-slate-700';

          if (isExam) {
            if (isChosen) {
              optionStyle =
                'border-indigo-600 bg-indigo-50/70 dark:bg-indigo-950/60 text-indigo-900 dark:text-indigo-200 ring-2 ring-indigo-500/20';
              badgeStyle = 'bg-indigo-600 text-white border-indigo-600';
            }
          } else if (shouldReveal) {
            if (isTheCorrectOption) {
              optionStyle =
                'border-emerald-500 bg-emerald-50/80 dark:bg-emerald-950/70 text-emerald-950 dark:text-emerald-100 ring-2 ring-emerald-500/30';
              badgeStyle = 'bg-emerald-600 text-white border-emerald-600';
            } else if (isChosen && !isTheCorrectOption) {
              optionStyle =
                'border-rose-500 bg-rose-50/80 dark:bg-rose-950/70 text-rose-950 dark:text-rose-100 ring-2 ring-rose-500/30';
              badgeStyle = 'bg-rose-600 text-white border-rose-600';
            } else {
              optionStyle =
                'opacity-60 border-slate-200 dark:border-slate-800 bg-slate-50/40 dark:bg-slate-900/40 text-slate-500 dark:text-slate-400';
            }
          } else if (isChosen) {
            optionStyle =
              'border-indigo-600 bg-indigo-50/70 dark:bg-indigo-950/60 text-indigo-900 dark:text-indigo-200 ring-2 ring-indigo-500/20';
            badgeStyle = 'bg-indigo-600 text-white border-indigo-600';
          }

          return (
            <div
              key={optIndex}
              onClick={() => handleOptionClick(optIndex)}
              className={`flex items-start gap-3 p-3.5 rounded-xl border transition-all cursor-pointer select-none ${optionStyle}`}
            >
              {/* Checkbox (Square) for Multi-select, Radio (Rounded-full or pill) for Single */}
              <div
                className={`flex-shrink-0 w-7 h-7 ${
                  isMulti ? 'rounded-md' : 'rounded-full'
                } border font-bold text-xs flex items-center justify-center transition-colors ${badgeStyle}`}
              >
                {OPTION_LABELS[optIndex]}
              </div>

              <div className="flex-1 text-sm md:text-base leading-relaxed pt-0.5">
                {optionText}
              </div>

              {shouldReveal && (
                <div className="flex-shrink-0 pt-0.5">
                  {isTheCorrectOption ? (
                    <CheckCircle2 size={18} className="text-emerald-600 dark:text-emerald-400" />
                  ) : isChosen ? (
                    <XCircle size={18} className="text-rose-600 dark:text-rose-400" />
                  ) : null}
                </div>
              )}
            </div>
          );
        })}
      </div>

      {/* Multi-select Confirmation Button for Practice Mode */}
      {isPractice && isMulti && isAnswered && !shouldReveal && (
        <div className="mt-3 pt-3 border-t border-slate-100 dark:border-slate-800 flex justify-end gap-2">
          <button
            onClick={() => setConfirmedMultiPractice(true)}
            className="flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-bold bg-indigo-600 hover:bg-indigo-700 text-white cursor-pointer shadow-sm transition"
          >
            <Check size={14} />
            <span>Xác nhận ({selectedList.length} lựa chọn)</span>
          </button>
        </div>
      )}

      {/* Practice Mode Controls: Toggle Explanation button if not revealed */}
      {isPractice && isAnswered && !showInstantFeedback && !shouldReveal && (
        <div className="mt-3 pt-3 border-t border-slate-100 dark:border-slate-800 flex justify-end">
          <button
            onClick={() => setShowManualExplanation(true)}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-indigo-50 dark:bg-indigo-950 text-indigo-600 dark:text-indigo-400 hover:bg-indigo-100 cursor-pointer transition-colors"
          >
            <Sparkles size={14} />
            <span>Xem đáp án & giải thích</span>
          </button>
        </div>
      )}

      {/* Detailed Explanation Box */}
      {shouldReveal && (
        <div className="mt-4 pt-4 border-t border-slate-100 dark:border-slate-800">
          <div className="p-4 rounded-xl bg-amber-50/70 dark:bg-amber-950/30 border border-amber-200/80 dark:border-amber-900/50">
            <div className="flex items-center gap-2 mb-2">
              <Sparkles size={16} className="text-amber-600 dark:text-amber-400" />
              <span className="font-bold text-sm text-amber-900 dark:text-amber-300">
                Đáp án đúng: {correctAnswersList.map(idx => OPTION_LABELS[idx]).join(', ')}
              </span>
              <span className="text-xs text-amber-700/80 dark:text-amber-400/80 font-medium">
                ({isMulti ? 'Chọn nhiều đáp án' : 'Phân tích chi tiết'})
              </span>
            </div>
            <p className="text-sm text-slate-700 dark:text-slate-300 leading-relaxed font-sans">
              {question.explanation}
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
