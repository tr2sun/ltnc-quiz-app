import React, { useState, useMemo } from 'react';
import { 
  BookOpen, 
  Filter, 
  ChevronLeft, 
  ChevronRight, 
  RotateCcw, 
  Sparkles, 
  Search,
  CheckCircle2,
  XCircle,
  HelpCircle,
  Eye,
  EyeOff
} from 'lucide-react';
import { LESSONS_METADATA, getQuestionsByLesson, getAllQuestions } from '../data';
import { useQuiz } from '../context/QuizContext';
import QuestionCard from '../components/QuestionCard';

export default function PracticePage({ initialLessonId = 1 }) {
  const [selectedLessonId, setSelectedLessonId] = useState(initialLessonId);
  const [difficultyFilter, setDifficultyFilter] = useState('all'); // all, easy, medium, hard
  const [searchQuery, setSearchQuery] = useState('');
  const [currentIndex, setCurrentIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState({}); // { [questionId]: chosenOptionIndex }
  const [instantExplanation, setInstantExplanation] = useState(true);

  const { 
    recordAnswerResult, 
    toggleBookmark, 
    isBookmarked,
    isMistake 
  } = useQuiz();

  // Load questions for the selected lesson or all
  const rawQuestions = useMemo(() => {
    if (selectedLessonId === 'all') {
      return getAllQuestions();
    }
    return getQuestionsByLesson(selectedLessonId);
  }, [selectedLessonId]);

  // Filter by difficulty and search term
  const filteredQuestions = useMemo(() => {
    return rawQuestions.filter(q => {
      if (difficultyFilter !== 'all' && q.difficulty !== difficultyFilter) {
        return false;
      }
      if (searchQuery.trim()) {
        const query = searchQuery.toLowerCase();
        const matchTitle = q.title.toLowerCase().includes(query);
        const matchTags = q.tags && q.tags.some(t => t.toLowerCase().includes(query));
        const matchCode = q.code && q.code.toLowerCase().includes(query);
        if (!matchTitle && !matchTags && !matchCode) return false;
      }
      return true;
    });
  }, [rawQuestions, difficultyFilter, searchQuery]);

  // Ensure current index is within bounds
  const currentQIndex = Math.min(currentIndex, Math.max(0, filteredQuestions.length - 1));
  const currentQuestion = filteredQuestions[currentQIndex];

  const handleSelectAnswer = (q, optionIndex) => {
    const isCorrect = optionIndex === q.correctAnswer;
    setUserAnswers(prev => ({ ...prev, [q.id]: optionIndex }));
    recordAnswerResult(q.id, q.lessonId, isCorrect, optionIndex);
  };

  const handleResetSession = () => {
    setUserAnswers({});
    setCurrentIndex(0);
  };

  // Stats for the active session
  const answeredCount = Object.keys(userAnswers).length;
  let correctCount = 0;
  filteredQuestions.forEach(q => {
    if (userAnswers[q.id] === q.correctAnswer) correctCount++;
  });

  const selectedLessonMeta = LESSONS_METADATA.find(l => l.id === Number(selectedLessonId));

  return (
    <div className="space-y-6 pb-12">
      {/* Top Banner */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white dark:bg-slate-900 p-5 rounded-2xl border border-slate-200/80 dark:border-slate-800 shadow-sm">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <span className="p-1.5 rounded-lg bg-indigo-50 dark:bg-indigo-950 text-indigo-600 dark:text-indigo-400">
              <BookOpen size={18} />
            </span>
            <h1 className="font-extrabold text-xl sm:text-2xl text-slate-800 dark:text-slate-100">
              Luyện Tập Theo Chuyên Đề
            </h1>
          </div>
          <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400">
            Học lý thuyết song hành thực hành bẫy code Java có giải thích JVM chi tiết
          </p>
        </div>

        {/* Instant explanation toggle */}
        <div className="flex items-center gap-3">
          <button
            onClick={() => setInstantExplanation(!instantExplanation)}
            className={`flex items-center gap-2 px-3 py-2 rounded-xl text-xs font-semibold border transition cursor-pointer ${
              instantExplanation
                ? 'bg-indigo-50 border-indigo-200 text-indigo-700 dark:bg-indigo-950 dark:border-indigo-800 dark:text-indigo-300'
                : 'bg-slate-100 border-slate-200 text-slate-600 dark:bg-slate-800 dark:border-slate-700 dark:text-slate-400'
            }`}
          >
            {instantExplanation ? <Eye size={15} /> : <EyeOff size={15} />}
            <span>Giải thích ngay khi chọn: {instantExplanation ? 'BẬT' : 'TẮT'}</span>
          </button>

          <button
            onClick={handleResetSession}
            className="flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-semibold bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-300 transition cursor-pointer"
            title="Làm lại từ đầu bài học này"
          >
            <RotateCcw size={14} />
            <span>Làm lại</span>
          </button>
        </div>
      </div>

      {/* Lesson Selector Pills */}
      <div className="flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none">
        <button
          onClick={() => {
            setSelectedLessonId('all');
            setCurrentIndex(0);
          }}
          className={`flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition cursor-pointer ${
            selectedLessonId === 'all'
              ? 'bg-indigo-600 text-white shadow-sm'
              : 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-800 hover:border-indigo-300'
          }`}
        >
          Tất cả 9 bài học
        </button>

        {LESSONS_METADATA.map((l) => (
          <button
            key={l.id}
            onClick={() => {
              setSelectedLessonId(l.id);
              setCurrentIndex(0);
            }}
            className={`flex-shrink-0 px-3.5 py-2 rounded-xl text-xs font-bold transition cursor-pointer ${
              selectedLessonId === l.id
                ? 'bg-indigo-600 text-white shadow-sm'
                : 'bg-white dark:bg-slate-900 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-800 hover:border-indigo-300'
            }`}
          >
            Bài {l.id}
          </button>
        ))}
      </div>

      {/* Filter and Search Bar */}
      <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
        <div className="relative col-span-2">
          <Search size={16} className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
          <input
            type="text"
            placeholder="Tìm kiếm theo từ khóa (static, PECS, override, exception...)..."
            value={searchQuery}
            onChange={(e) => {
              setSearchQuery(e.target.value);
              setCurrentIndex(0);
            }}
            className="w-full pl-10 pr-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 text-slate-800 dark:text-slate-100 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
        </div>

        <div className="flex items-center gap-2">
          <Filter size={15} className="text-slate-400" />
          <select
            value={difficultyFilter}
            onChange={(e) => {
              setDifficultyFilter(e.target.value);
              setCurrentIndex(0);
            }}
            className="w-full px-3 py-2.5 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 text-slate-800 dark:text-slate-100 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
          >
            <option value="all">Mọi độ khó</option>
            <option value="easy">Dễ</option>
            <option value="medium">Trung bình</option>
            <option value="hard">Nâng cao</option>
          </select>
        </div>
      </div>

      {/* Active Lesson Header Info */}
      {selectedLessonMeta && (
        <div className="p-4 rounded-2xl bg-indigo-50/50 dark:bg-indigo-950/20 border border-indigo-100 dark:border-indigo-900/40 flex items-center justify-between">
          <div>
            <h3 className="font-bold text-sm text-indigo-950 dark:text-indigo-200">
              {selectedLessonMeta.title}: {selectedLessonMeta.subtitle}
            </h3>
            <p className="text-xs text-indigo-700/80 dark:text-indigo-400/80 mt-0.5">
              {selectedLessonMeta.description}
            </p>
          </div>
          <div className="hidden sm:block text-right">
            <span className="text-xs font-mono font-bold text-indigo-600 dark:text-indigo-400">
              {filteredQuestions.length} câu hỏi
            </span>
          </div>
        </div>
      )}

      {/* Main Practice Area */}
      {filteredQuestions.length === 0 ? (
        <div className="text-center py-12 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 p-8">
          <HelpCircle size={40} className="mx-auto text-slate-300 dark:text-slate-600 mb-3" />
          <h3 className="font-bold text-slate-700 dark:text-slate-200 mb-1">
            Không tìm thấy câu hỏi phù hợp
          </h3>
          <p className="text-xs text-slate-500 dark:text-slate-400">
            Hãy thử thay đổi độ khó hoặc từ khóa tìm kiếm.
          </p>
        </div>
      ) : (
        <div className="space-y-4">
          {/* Question Index Progress Navigation */}
          <div className="flex items-center justify-between bg-white dark:bg-slate-900 p-3.5 rounded-2xl border border-slate-200/80 dark:border-slate-800 shadow-sm text-xs">
            <span className="font-semibold text-slate-600 dark:text-slate-300">
              Câu {currentQIndex + 1} / {filteredQuestions.length}
            </span>

            <div className="flex items-center gap-1.5 sm:gap-2">
              <button
                onClick={() => setCurrentIndex(Math.max(0, currentQIndex - 1))}
                disabled={currentQIndex === 0}
                className="p-2 rounded-lg border border-slate-200 dark:border-slate-700 disabled:opacity-30 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer"
                title="Câu trước"
              >
                <ChevronLeft size={16} />
              </button>

              {/* Number bubbles preview */}
              <div className="hidden md:flex items-center gap-1 max-w-[360px] overflow-x-auto px-1">
                {filteredQuestions.map((q, idx) => {
                  const isDone = userAnswers[q.id] !== undefined;
                  const isCurrent = idx === currentQIndex;
                  return (
                    <button
                      key={q.id}
                      onClick={() => setCurrentIndex(idx)}
                      className={`w-7 h-7 rounded-md text-[11px] font-semibold flex items-center justify-center transition cursor-pointer ${
                        isCurrent
                          ? 'bg-indigo-600 text-white ring-2 ring-indigo-400'
                          : isDone
                          ? 'bg-indigo-100 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300'
                          : 'bg-slate-100 dark:bg-slate-800 text-slate-500'
                      }`}
                    >
                      {idx + 1}
                    </button>
                  );
                })}
              </div>

              <button
                onClick={() => setCurrentIndex(Math.min(filteredQuestions.length - 1, currentQIndex + 1))}
                disabled={currentQIndex === filteredQuestions.length - 1}
                className="p-2 rounded-lg border border-slate-200 dark:border-slate-700 disabled:opacity-30 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer"
                title="Câu tiếp theo"
              >
                <ChevronRight size={16} />
              </button>
            </div>
          </div>

          {/* Current Question Card */}
          {currentQuestion && (
            <QuestionCard
              question={currentQuestion}
              questionIndex={currentQIndex}
              selectedAnswer={userAnswers[currentQuestion.id]}
              onSelectAnswer={(optIdx) => handleSelectAnswer(currentQuestion, optIdx)}
              mode="practice"
              showInstantFeedback={instantExplanation}
              isBookmarked={isBookmarked(currentQuestion.id)}
              onToggleBookmark={() => toggleBookmark(currentQuestion.id)}
            />
          )}

          {/* Bottom Next/Prev Action Buttons */}
          <div className="flex items-center justify-between pt-2">
            <button
              onClick={() => setCurrentIndex(Math.max(0, currentQIndex - 1))}
              disabled={currentQIndex === 0}
              className="flex items-center gap-1.5 px-4 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-xs font-bold disabled:opacity-30 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer transition"
            >
              <ChevronLeft size={16} />
              <span>Câu trước</span>
            </button>

            <button
              onClick={() => setCurrentIndex(Math.min(filteredQuestions.length - 1, currentQIndex + 1))}
              disabled={currentQIndex === filteredQuestions.length - 1}
              className="flex items-center gap-1.5 px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold disabled:opacity-30 shadow-md shadow-indigo-500/20 cursor-pointer transition"
            >
              <span>Câu tiếp theo</span>
              <ChevronRight size={16} />
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
