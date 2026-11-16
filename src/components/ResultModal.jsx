import React, { useEffect } from 'react';
import confetti from 'canvas-confetti';
import { Trophy, CheckCircle, XCircle, Clock, RotateCcw, Eye, ArrowRight, BookOpen } from 'lucide-react';
import { LESSONS_METADATA } from '../data/lessonsMetadata';
import { isAnswerCorrect } from './QuestionCard';

export default function ResultModal({
  isOpen,
  onClose,
  score = 0,
  total = 30,
  timeSpentSeconds = 0,
  questions = [],
  answers = {},
  onRetake,
  onReviewMode,
  onGoToMistakes
}) {
  useEffect(() => {
    if (isOpen) {
      const percentage = (score / total) * 100;
      if (percentage >= 70) {
        confetti({
          particleCount: 80,
          spread: 70,
          origin: { y: 0.6 }
        });
      }
    }
  }, [isOpen, score, total]);

  if (!isOpen) return null;

  const percentage = Math.round((score / total) * 100);
  const score10Scale = ((score / total) * 10).toFixed(1);

  const formatTime = (secs) => {
    const m = Math.floor(secs / 60);
    const s = secs % 60;
    return `${m}m ${s < 10 ? '0' : ''}${s}s`;
  };

  // Lesson breakdown analysis
  const lessonStats = {};
  questions.forEach((q, idx) => {
    const lId = q.lessonId || 1;
    if (!lessonStats[lId]) {
      lessonStats[lId] = { correct: 0, total: 0 };
    }
    lessonStats[lId].total += 1;
    if (isAnswerCorrect(q, answers[idx])) {
      lessonStats[lId].correct += 1;
    }
  });

  const getEvaluation = (pct) => {
    if (pct >= 90) return { text: 'Xuất sắc! (Điểm A+)', color: 'text-emerald-600 dark:text-emerald-400', bg: 'bg-emerald-50 dark:bg-emerald-950/60' };
    if (pct >= 80) return { text: 'Giỏi! (Điểm A)', color: 'text-indigo-600 dark:text-indigo-400', bg: 'bg-indigo-50 dark:bg-indigo-950/60' };
    if (pct >= 70) return { text: 'Khá! (Điểm B/B+)', color: 'text-blue-600 dark:text-blue-400', bg: 'bg-blue-50 dark:bg-blue-950/60' };
    if (pct >= 50) return { text: 'Trung bình (Điểm C)', color: 'text-amber-600 dark:text-amber-400', bg: 'bg-amber-50 dark:bg-amber-950/60' };
    return { text: 'Cần ôn luyện thêm! (Điểm D/F)', color: 'text-rose-600 dark:text-rose-400', bg: 'bg-rose-50 dark:bg-rose-950/60' };
  };

  const evaluation = getEvaluation(percentage);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/70 backdrop-blur-sm overflow-y-auto">
      <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto p-6 md:p-8 animate-in fade-in zoom-in duration-200">
        
        {/* Top Trophy Banner */}
        <div className="text-center mb-6">
          <div className="inline-flex p-4 rounded-2xl bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400 mb-3 shadow-inner">
            <Trophy size={42} />
          </div>
          <h2 className="text-2xl md:text-3xl font-extrabold text-slate-800 dark:text-slate-100">
            Kết Quả Bài Thi
          </h2>
          <div className="mt-2 inline-block px-3.5 py-1 rounded-full text-xs font-bold border border-current tracking-wide uppercase"
               style={{ color: evaluation.color }}>
            {evaluation.text}
          </div>
        </div>

        {/* Score Cards Grid */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-6">
          <div className="p-3.5 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-800 text-center">
            <span className="text-xs font-semibold text-slate-500 dark:text-slate-400 block mb-1">
              Điểm số (Thang 10)
            </span>
            <span className="text-2xl font-black text-indigo-600 dark:text-indigo-400">
              {score10Scale}
            </span>
          </div>

          <div className="p-3.5 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-800 text-center">
            <span className="text-xs font-semibold text-slate-500 dark:text-slate-400 block mb-1">
              Số câu đúng
            </span>
            <span className="text-2xl font-black text-emerald-600 dark:text-emerald-400">
              {score}/{total}
            </span>
          </div>

          <div className="p-3.5 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-800 text-center">
            <span className="text-xs font-semibold text-slate-500 dark:text-slate-400 block mb-1">
              Độ chính xác
            </span>
            <span className="text-2xl font-black text-blue-600 dark:text-blue-400">
              {percentage}%
            </span>
          </div>

          <div className="p-3.5 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-800 text-center">
            <span className="text-xs font-semibold text-slate-500 dark:text-slate-400 block mb-1">
              Thời gian làm
            </span>
            <span className="text-2xl font-black text-slate-700 dark:text-slate-300 font-mono">
              {formatTime(timeSpentSeconds)}
            </span>
          </div>
        </div>

        {/* Breakdown by Lesson */}
        <div className="mb-6 p-4 rounded-2xl bg-slate-50/70 dark:bg-slate-800/40 border border-slate-200/80 dark:border-slate-800">
          <h4 className="font-bold text-xs uppercase tracking-wider text-slate-500 dark:text-slate-400 mb-3">
            Phân tích chi tiết từng bài học
          </h4>
          <div className="space-y-2">
            {Object.keys(lessonStats).map((lId) => {
              const meta = LESSONS_METADATA.find(m => m.id === Number(lId));
              const stat = lessonStats[lId];
              const pct = stat.total > 0 ? Math.round((stat.correct / stat.total) * 100) : 0;
              return (
                <div key={lId} className="flex items-center justify-between text-xs gap-3">
                  <div className="flex-1 truncate">
                    <span className="font-semibold text-slate-700 dark:text-slate-200">
                      {meta ? meta.title : `Bài ${lId}`}
                    </span>
                  </div>
                  <div className="w-24 bg-slate-200 dark:bg-slate-700 h-2 rounded-full overflow-hidden">
                    <div
                      className={`h-full rounded-full ${
                        pct >= 80 ? 'bg-emerald-500' : pct >= 50 ? 'bg-amber-500' : 'bg-rose-500'
                      }`}
                      style={{ width: `${pct}%` }}
                    />
                  </div>
                  <span className="font-mono text-slate-600 dark:text-slate-400 w-12 text-right">
                    {stat.correct}/{stat.total} ({pct}%)
                  </span>
                </div>
              );
            })}
          </div>
        </div>

        {/* Action Buttons */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
          <button
            onClick={() => {
              onClose();
              if (onReviewMode) onReviewMode();
            }}
            className="flex items-center justify-center gap-2 px-4 py-3 rounded-xl font-bold text-sm bg-indigo-600 hover:bg-indigo-700 text-white shadow-md shadow-indigo-500/20 transition cursor-pointer"
          >
            <Eye size={16} />
            <span>Xem lại chi tiết bài làm</span>
          </button>

          <button
            onClick={() => {
              onClose();
              if (onRetake) onRetake();
            }}
            className="flex items-center justify-center gap-2 px-4 py-3 rounded-xl font-bold text-sm bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 transition cursor-pointer"
          >
            <RotateCcw size={16} />
            <span>Làm lại đề thi</span>
          </button>
        </div>

        {onGoToMistakes && (
          <div className="mt-3 text-center">
            <button
              onClick={() => {
                onClose();
                onGoToMistakes();
              }}
              className="text-xs text-indigo-600 dark:text-indigo-400 hover:underline inline-flex items-center gap-1 font-semibold cursor-pointer"
            >
              <BookOpen size={13} />
              <span>Xem các câu làm sai trong Sổ tay câu sai &rarr;</span>
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
