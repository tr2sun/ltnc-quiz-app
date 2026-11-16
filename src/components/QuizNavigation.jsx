import React from 'react';
import { Bookmark, CheckCircle2, Send, HelpCircle } from 'lucide-react';

export default function QuizNavigation({
  totalQuestions,
  currentIndex = 0,
  onJumpToQuestion,
  answers = {},
  isQuestionBookmarked,
  onSubmitQuiz,
  mode = 'exam', // 'exam' | 'practice'
  questions = []
}) {
  const answeredCount = Object.keys(answers).filter(k => answers[k] !== undefined && answers[k] !== null).length;
  const remainingCount = totalQuestions - answeredCount;

  return (
    <div className="bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 shadow-sm p-4 sticky top-20">
      {/* Header & Stats */}
      <div className="flex items-center justify-between mb-3 pb-3 border-b border-slate-100 dark:border-slate-800">
        <div>
          <h4 className="font-bold text-sm text-slate-800 dark:text-slate-100">
            Danh sách câu hỏi
          </h4>
          <p className="text-xs text-slate-500 dark:text-slate-400">
            Đã làm <span className="font-semibold text-indigo-600 dark:text-indigo-400">{answeredCount}</span>/{totalQuestions} câu
          </p>
        </div>

        {mode === 'exam' && onSubmitQuiz && (
          <button
            onClick={onSubmitQuiz}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-bold bg-indigo-600 hover:bg-indigo-700 text-white shadow-sm transition cursor-pointer"
          >
            <Send size={13} />
            <span>Nộp bài</span>
          </button>
        )}
      </div>

      {/* Status Legends */}
      <div className="flex items-center justify-between text-[11px] text-slate-500 dark:text-slate-400 mb-3 px-1">
        <div className="flex items-center gap-1.5">
          <span className="w-2.5 h-2.5 rounded bg-indigo-600"></span>
          <span>Đã làm ({answeredCount})</span>
        </div>
        <div className="flex items-center gap-1.5">
          <span className="w-2.5 h-2.5 rounded border border-slate-300 dark:border-slate-600 bg-slate-50 dark:bg-slate-800"></span>
          <span>Chưa ({remainingCount})</span>
        </div>
        <div className="flex items-center gap-1.5">
          <span className="w-2 h-2 rounded-full bg-amber-500"></span>
          <span>Ghim</span>
        </div>
      </div>

      {/* Grid Palette 1..30 */}
      <div className="grid grid-cols-5 sm:grid-cols-6 gap-2 max-h-[320px] overflow-y-auto pr-1">
        {Array.from({ length: totalQuestions }).map((_, idx) => {
          const isAnswered = answers[idx] !== undefined && answers[idx] !== null;
          const isCurrent = currentIndex === idx;
          const qObj = questions[idx];
          const isFlagged = qObj && isQuestionBookmarked ? isQuestionBookmarked(qObj.id) : false;

          let btnClass = 'border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:border-indigo-400 hover:bg-indigo-50/50';

          if (isAnswered) {
            btnClass = 'bg-indigo-600 border-indigo-600 text-white font-semibold hover:bg-indigo-700';
          }

          if (isCurrent) {
            btnClass += ' ring-2 ring-indigo-400 ring-offset-2 dark:ring-offset-slate-900';
          }

          return (
            <button
              key={idx}
              onClick={() => onJumpToQuestion(idx)}
              className={`relative h-9 rounded-lg border text-xs font-medium flex items-center justify-center transition-all cursor-pointer ${btnClass}`}
              title={`Chuyển tới câu ${idx + 1}`}
            >
              {idx + 1}
              {isFlagged && (
                <span className="absolute -top-1 -right-1 w-2.5 h-2.5 rounded-full bg-amber-500 border border-white dark:border-slate-900" />
              )}
            </button>
          );
        })}
      </div>

      {/* Quick summary for uncompleted items */}
      {remainingCount > 0 && mode === 'exam' && (
        <div className="mt-4 pt-3 border-t border-slate-100 dark:border-slate-800 text-center">
          <span className="text-[11px] text-amber-600 dark:text-amber-400 font-medium">
            ⚠️ Bạn còn {remainingCount} câu chưa chọn đáp án!
          </span>
        </div>
      )}
    </div>
  );
}
