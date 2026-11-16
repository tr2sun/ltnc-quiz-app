import React from 'react';
import { 
  GraduationCap, 
  BookOpen, 
  Bookmark, 
  FileText, 
  CheckCircle2, 
  TrendingUp, 
  Clock, 
  AlertCircle, 
  ArrowRight,
  Sparkles,
  Award,
  Layers,
  Cpu,
  Database,
  FileCode,
  Boxes,
  Zap,
  CheckCircle,
  LayoutGrid
} from 'lucide-react';
import { LESSONS_METADATA, getAllQuestions, getQuestionsByLesson } from '../data';
import { useQuiz } from '../context/QuizContext';

// Map icon string to Lucide component
const ICON_MAP = {
  Cpu: Cpu,
  Layers: Layers,
  FileCode: FileCode,
  Boxes: Boxes,
  Database: Database,
  AlertTriangle: AlertCircle,
  LayoutGrid: LayoutGrid,
  Zap: Zap,
  CheckCircle: CheckCircle
};

export default function HomePage({ onNavigate, onSelectLesson }) {
  const { mistakes, bookmarks, quizHistory, lessonProgress } = useQuiz();

  const allQuestions = getAllQuestions();
  const totalQuestionsInBank = allQuestions.length;

  // Compute overall stats
  let totalAnswered = 0;
  let totalCorrect = 0;
  Object.values(lessonProgress).forEach(p => {
    totalAnswered += p.answered || 0;
    totalCorrect += p.correct || 0;
  });

  const overallAccuracy = totalAnswered > 0 ? Math.round((totalCorrect / totalAnswered) * 100) : 0;
  const mistakeCount = Object.keys(mistakes).length;
  const examCount = quizHistory.filter(h => h.type === 'exam').length;

  return (
    <div className="space-y-8 pb-12">
      {/* Hero Section */}
      <section className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-indigo-900 via-indigo-800 to-purple-950 text-white p-6 sm:p-10 shadow-xl">
        <div className="absolute -right-10 -bottom-10 w-80 h-80 bg-purple-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="absolute right-10 top-6 hidden lg:block opacity-20 pointer-events-none">
          <GraduationCap size={220} />
        </div>

        <div className="relative z-10 max-w-2xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-indigo-500/30 border border-indigo-400/30 text-indigo-200 text-xs font-semibold mb-4 backdrop-blur-sm">
            <Sparkles size={14} className="text-amber-300" />
            <span>Khoá học CS2043 • Đại học Công nghệ (UET)</span>
          </div>

          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight leading-tight mb-4">
            Luyện Thi Trắc Nghiệm <br />
            <span className="bg-gradient-to-r from-amber-300 via-yellow-200 to-indigo-200 bg-clip-text text-transparent">
              Lập Trình Nâng Cao
            </span>
          </h1>

          <p className="text-indigo-100 text-sm sm:text-base leading-relaxed mb-6 font-normal">
            Ngân hàng câu hỏi trắc nghiệm chuyên sâu bám sát đề cương giảng dạy và đề thi cuối kỳ:
            JVM, Đa hình, Generics & PECS, Collections, Ngoại lệ, Đa luồng, Mẫu thiết kế và JUnit.
          </p>

          <div className="flex flex-wrap items-center gap-3">
            <button
              onClick={() => onNavigate('exam')}
              className="flex items-center gap-2 px-5 py-3 rounded-xl font-bold text-sm bg-gradient-to-r from-amber-400 to-amber-500 hover:from-amber-500 hover:to-amber-600 text-slate-950 shadow-lg shadow-amber-500/25 transition transform hover:-translate-y-0.5 cursor-pointer"
            >
              <GraduationCap size={18} />
              <span>Thi thử 30 câu (40 phút)</span>
            </button>

            <button
              onClick={() => onNavigate('practice')}
              className="flex items-center gap-2 px-5 py-3 rounded-xl font-bold text-sm bg-white/10 hover:bg-white/20 text-white border border-white/20 backdrop-blur-md transition cursor-pointer"
            >
              <BookOpen size={18} />
              <span>Luyện theo bài học</span>
            </button>

            <button
              onClick={() => onNavigate('cheatsheet')}
              className="flex items-center gap-2 px-4 py-3 rounded-xl font-bold text-sm text-indigo-200 hover:text-white hover:bg-indigo-700/40 transition cursor-pointer"
            >
              <FileText size={18} />
              <span>Cheat Sheet</span>
            </button>
          </div>
        </div>
      </section>

      {/* User Quick Stats Banner */}
      <section className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div className="bg-white dark:bg-slate-900 rounded-2xl p-5 border border-slate-200/80 dark:border-slate-800 shadow-sm flex items-center gap-4">
          <div className="p-3 rounded-xl bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400">
            <CheckCircle2 size={24} />
          </div>
          <div>
            <span className="text-xs font-semibold text-slate-400 block">Đã trả lời</span>
            <div className="text-xl sm:text-2xl font-black text-slate-800 dark:text-slate-100">
              {totalAnswered}
              <span className="text-xs font-normal text-slate-400 ml-1">câu</span>
            </div>
          </div>
        </div>

        <div className="bg-white dark:bg-slate-900 rounded-2xl p-5 border border-slate-200/80 dark:border-slate-800 shadow-sm flex items-center gap-4">
          <div className="p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400">
            <TrendingUp size={24} />
          </div>
          <div>
            <span className="text-xs font-semibold text-slate-400 block">Độ chính xác</span>
            <div className="text-xl sm:text-2xl font-black text-emerald-600 dark:text-emerald-400">
              {overallAccuracy}%
            </div>
          </div>
        </div>

        <div className="bg-white dark:bg-slate-900 rounded-2xl p-5 border border-slate-200/80 dark:border-slate-800 shadow-sm flex items-center gap-4">
          <div className="p-3 rounded-xl bg-rose-50 dark:bg-rose-950/60 text-rose-600 dark:text-rose-400">
            <AlertCircle size={24} />
          </div>
          <div>
            <span className="text-xs font-semibold text-slate-400 block">Sổ tay câu sai</span>
            <div className="text-xl sm:text-2xl font-black text-rose-600 dark:text-rose-400">
              {mistakeCount}
              <span className="text-xs font-normal text-slate-400 ml-1">câu</span>
            </div>
          </div>
        </div>

        <div className="bg-white dark:bg-slate-900 rounded-2xl p-5 border border-slate-200/80 dark:border-slate-800 shadow-sm flex items-center gap-4">
          <div className="p-3 rounded-xl bg-amber-50 dark:bg-amber-950/60 text-amber-600 dark:text-amber-400">
            <Award size={24} />
          </div>
          <div>
            <span className="text-xs font-semibold text-slate-400 block">Đề thi đã làm</span>
            <div className="text-xl sm:text-2xl font-black text-amber-600 dark:text-amber-400">
              {examCount}
              <span className="text-xs font-normal text-slate-400 ml-1">đề</span>
            </div>
          </div>
        </div>
      </section>

      {/* 9 Lessons Curriculum Grid */}
      <section className="space-y-4">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-xl sm:text-2xl font-extrabold text-slate-800 dark:text-slate-100">
              Chuyên Đề Luyện Tập
            </h2>
            <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400">
              Phân loại 9 bài học theo tiến trình học tập chuẩn UET (CS2043)
            </p>
          </div>
          <button
            onClick={() => onNavigate('practice')}
            className="text-xs sm:text-sm font-semibold text-indigo-600 dark:text-indigo-400 hover:underline flex items-center gap-1 cursor-pointer"
          >
            <span>Xem tất cả</span>
            <ArrowRight size={14} />
          </button>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {LESSONS_METADATA.map((lesson) => {
            const IconComponent = ICON_MAP[lesson.icon] || BookOpen;
            const lessonQuestions = getQuestionsByLesson(lesson.id);
            const progress = lessonProgress[lesson.id] || { answered: 0, correct: 0 };
            const progressPct = lessonQuestions.length > 0 
              ? Math.min(100, Math.round((progress.answered / lessonQuestions.length) * 100))
              : 0;

            return (
              <div
                key={lesson.id}
                className="group bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-5 shadow-sm hover:shadow-md transition-all flex flex-col justify-between"
              >
                <div>
                  {/* Top Bar with Icon & Badge */}
                  <div className="flex items-center justify-between mb-3">
                    <div className={`w-10 h-10 rounded-xl bg-gradient-to-tr ${lesson.color} text-white flex items-center justify-center shadow-sm`}>
                      <IconComponent size={20} />
                    </div>
                    <span className="text-[11px] font-bold px-2.5 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
                      {lesson.badge}
                    </span>
                  </div>

                  {/* Title & Subtitle */}
                  <h3 className="font-bold text-base text-slate-800 dark:text-slate-100 group-hover:text-indigo-600 dark:group-hover:text-indigo-400 transition-colors mb-1">
                    {lesson.title}
                  </h3>
                  <p className="text-xs font-medium text-slate-500 dark:text-slate-400 mb-2">
                    {lesson.subtitle}
                  </p>
                  <p className="text-xs text-slate-600 dark:text-slate-300 line-clamp-2 mb-4 leading-relaxed">
                    {lesson.description}
                  </p>

                  {/* Tags */}
                  <div className="flex flex-wrap gap-1.5 mb-4">
                    {lesson.tags.slice(0, 3).map((tag, tIdx) => (
                      <span
                        key={tIdx}
                        className="text-[10px] font-semibold px-2 py-0.5 rounded bg-slate-100 dark:bg-slate-800/80 text-slate-600 dark:text-slate-400"
                      >
                        {tag}
                      </span>
                    ))}
                  </div>
                </div>

                <div>
                  {/* Progress bar */}
                  <div className="mb-3">
                    <div className="flex items-center justify-between text-[11px] text-slate-500 dark:text-slate-400 mb-1">
                      <span>Đã làm: {progress.answered}/{lessonQuestions.length}</span>
                      <span className="font-semibold">{progressPct}%</span>
                    </div>
                    <div className="w-full bg-slate-100 dark:bg-slate-800 h-1.5 rounded-full overflow-hidden">
                      <div
                        className="h-full bg-indigo-600 rounded-full transition-all"
                        style={{ width: `${progressPct}%` }}
                      />
                    </div>
                  </div>

                  {/* Action button */}
                  <button
                    onClick={() => {
                      if (onSelectLesson) onSelectLesson(lesson.id);
                      onNavigate('practice');
                    }}
                    className="w-full flex items-center justify-center gap-2 py-2 px-3 rounded-xl text-xs font-bold bg-indigo-50 hover:bg-indigo-100 dark:bg-indigo-950/60 dark:hover:bg-indigo-900/60 text-indigo-700 dark:text-indigo-300 transition cursor-pointer"
                  >
                    <span>Luyện tập ngay</span>
                    <ArrowRight size={13} />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      {/* Quick Access to Mistakes if any */}
      {mistakeCount > 0 && (
        <section className="p-5 sm:p-6 rounded-2xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-900/50 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-4 text-center sm:text-left">
            <div className="p-3 rounded-2xl bg-rose-100 dark:bg-rose-900/50 text-rose-600 dark:text-rose-400">
              <AlertCircle size={28} />
            </div>
            <div>
              <h4 className="font-bold text-base text-rose-900 dark:text-rose-200">
                Bạn có {mistakeCount} câu hỏi làm sai cần khắc phục!
              </h4>
              <p className="text-xs text-rose-700 dark:text-rose-300 mt-0.5">
                Ôn luyện lại các bẫy lý thuyết và mã nguồn Java để không lặp lại lỗi trong kỳ thi.
              </p>
            </div>
          </div>
          <button
            onClick={() => onNavigate('mistakes')}
            className="flex-shrink-0 px-4 py-2.5 rounded-xl font-bold text-xs bg-rose-600 hover:bg-rose-700 text-white shadow-md shadow-rose-500/20 transition cursor-pointer"
          >
            Mở sổ tay câu sai &rarr;
          </button>
        </section>
      )}
    </div>
  );
}
