import React, { useState, useMemo } from 'react';
import { 
  Bookmark, 
  AlertCircle, 
  Trash2, 
  RotateCcw, 
  Play, 
  CheckCircle2, 
  HelpCircle,
  Sparkles,
  ArrowRight
} from 'lucide-react';
import { getAllQuestions, getQuestionById } from '../data';
import { useQuiz } from '../context/QuizContext';
import QuestionCard from '../components/QuestionCard';

export default function MistakesPage({ onNavigate }) {
  const [activeTab, setActiveTab] = useState('mistakes'); // 'mistakes' | 'bookmarks'
  const [retakeMode, setRetakeMode] = useState(false);
  const [retakeAnswers, setRetakeAnswers] = useState({});
  const [currentIndex, setCurrentIndex] = useState(0);

  const { 
    mistakes, 
    bookmarks, 
    removeMistake, 
    clearAllMistakes, 
    toggleBookmark, 
    isBookmarked,
    clearAllBookmarks,
    recordAnswerResult
  } = useQuiz();

  const allQuestions = useMemo(() => getAllQuestions(), []);

  // Questions from mistakes
  const mistakeQuestions = useMemo(() => {
    const list = [];
    Object.keys(mistakes).forEach(id => {
      const q = allQuestions.find(item => item.id === id);
      if (q) list.push({ ...q, mistakeMeta: mistakes[id] });
    });
    return list;
  }, [mistakes, allQuestions]);

  // Questions from bookmarks
  const bookmarkedQuestions = useMemo(() => {
    const list = [];
    bookmarks.forEach(id => {
      const q = allQuestions.find(item => item.id === id);
      if (q) list.push(q);
    });
    return list;
  }, [bookmarks, allQuestions]);

  const activeQuestions = activeTab === 'mistakes' ? mistakeQuestions : bookmarkedQuestions;

  // Handle re-answering in retake mode
  const handleSelectRetakeAnswer = (q, optIndex) => {
    const isCorrect = optIndex === q.correctAnswer;
    setRetakeAnswers(prev => ({ ...prev, [q.id]: optIndex }));
    recordAnswerResult(q.id, q.lessonId, isCorrect, optIndex);

    // If correct in retake mode, offer auto-removal
    if (isCorrect && activeTab === 'mistakes') {
      setTimeout(() => {
        removeMistake(q.id);
      }, 1000);
    }
  };

  const handleStartRetake = () => {
    setRetakeAnswers({});
    setCurrentIndex(0);
    setRetakeMode(true);
  };

  return (
    <div className="space-y-6 pb-12">
      {/* Top Banner */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white dark:bg-slate-900 p-5 rounded-2xl border border-slate-200/80 dark:border-slate-800 shadow-sm">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <span className="p-1.5 rounded-lg bg-rose-50 dark:bg-rose-950 text-rose-600 dark:text-rose-400">
              <Bookmark size={18} />
            </span>
            <h1 className="font-extrabold text-xl sm:text-2xl text-slate-800 dark:text-slate-100">
              Sổ Tay Câu Sai & Đã Ghim
            </h1>
          </div>
          <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400">
            Xem lại những câu hỏi đã từng trả lời sai hoặc đánh dấu cờ để ghi nhớ sâu bản chất
          </p>
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-2">
          {activeQuestions.length > 0 && !retakeMode && (
            <button
              onClick={handleStartRetake}
              className="flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-bold bg-indigo-600 hover:bg-indigo-700 text-white shadow-md shadow-indigo-500/20 transition cursor-pointer"
            >
              <Play size={14} />
              <span>Luyện tập lại ({activeQuestions.length})</span>
            </button>
          )}

          {retakeMode && (
            <button
              onClick={() => setRetakeMode(false)}
              className="flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 transition cursor-pointer"
            >
              <RotateCcw size={14} />
              <span>Thoát chế độ luyện</span>
            </button>
          )}

          {activeTab === 'mistakes' && mistakeQuestions.length > 0 && !retakeMode && (
            <button
              onClick={() => {
                if (window.confirm('Bạn có chắc chắn muốn xoá tất cả câu trong sổ tay câu sai?')) {
                  clearAllMistakes();
                }
              }}
              className="flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-semibold text-rose-600 hover:bg-rose-50 dark:text-rose-400 dark:hover:bg-rose-950/40 border border-rose-200 dark:border-rose-900 transition cursor-pointer"
            >
              <Trash2 size={14} />
              <span>Xoá tất cả</span>
            </button>
          )}

          {activeTab === 'bookmarks' && bookmarkedQuestions.length > 0 && !retakeMode && (
            <button
              onClick={() => {
                if (window.confirm('Bạn có chắc chắn muốn bỏ ghim tất cả câu hỏi?')) {
                  clearAllBookmarks();
                }
              }}
              className="flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-semibold text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800 border border-slate-200 dark:border-slate-700 transition cursor-pointer"
            >
              <Trash2 size={14} />
              <span>Bỏ ghim tất cả</span>
            </button>
          )}
        </div>
      </div>

      {/* Tabs Switcher: Mistakes vs Bookmarks */}
      {!retakeMode && (
        <div className="flex border-b border-slate-200 dark:border-slate-800 gap-6">
          <button
            onClick={() => setActiveTab('mistakes')}
            className={`pb-3 font-bold text-sm flex items-center gap-2 border-b-2 transition cursor-pointer ${
              activeTab === 'mistakes'
                ? 'border-rose-600 text-rose-600 dark:text-rose-400'
                : 'border-transparent text-slate-500 hover:text-slate-700 dark:hover:text-slate-300'
            }`}
          >
            <AlertCircle size={16} />
            <span>Câu đã làm sai</span>
            <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-rose-100 text-rose-700 dark:bg-rose-950/80 dark:text-rose-300">
              {mistakeQuestions.length}
            </span>
          </button>

          <button
            onClick={() => setActiveTab('bookmarks')}
            className={`pb-3 font-bold text-sm flex items-center gap-2 border-b-2 transition cursor-pointer ${
              activeTab === 'bookmarks'
                ? 'border-amber-500 text-amber-600 dark:text-amber-400'
                : 'border-transparent text-slate-500 hover:text-slate-700 dark:hover:text-slate-300'
            }`}
          >
            <Bookmark size={16} />
            <span>Câu đã đánh dấu cờ</span>
            <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-amber-100 text-amber-700 dark:bg-amber-950/80 dark:text-amber-300">
              {bookmarkedQuestions.length}
            </span>
          </button>
        </div>
      )}

      {/* Content Display */}
      {activeQuestions.length === 0 ? (
        <div className="text-center py-16 bg-white dark:bg-slate-900 rounded-3xl border border-slate-200/80 dark:border-slate-800 p-8 shadow-sm">
          <div className="w-16 h-16 rounded-full bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400 flex items-center justify-center mx-auto mb-4">
            <CheckCircle2 size={32} />
          </div>
          <h3 className="font-extrabold text-lg text-slate-800 dark:text-slate-100 mb-1">
            {activeTab === 'mistakes' ? 'Chưa có câu sai nào!' : 'Chưa có câu hỏi nào được ghim'}
          </h3>
          <p className="text-xs text-slate-500 dark:text-slate-400 max-w-md mx-auto mb-6">
            {activeTab === 'mistakes'
              ? 'Luyện tập theo chuyên đề hoặc làm bài thi thử; các câu bạn trả lời sai sẽ tự động được lưu vào đây để tiện xem lại.'
              : 'Trong khi làm bài, bạn có thể bấm biểu tượng cái ghim ở góc phải câu hỏi để lưu lại.'}
          </p>
          <button
            onClick={() => onNavigate('exam')}
            className="px-5 py-2.5 rounded-xl font-bold text-xs bg-indigo-600 hover:bg-indigo-700 text-white shadow-md shadow-indigo-500/20 cursor-pointer"
          >
            Làm bài thi thử 30 câu ngay &rarr;
          </button>
        </div>
      ) : retakeMode ? (
        /* Retake Practice Mode: One-by-one or continuous */
        <div className="space-y-4">
          <div className="flex items-center justify-between p-3.5 bg-indigo-50 dark:bg-indigo-950/50 rounded-2xl border border-indigo-200 dark:border-indigo-800 text-xs">
            <span className="font-bold text-indigo-950 dark:text-indigo-200">
              Đang luyện lại câu {currentIndex + 1} / {activeQuestions.length}
            </span>
            <span className="text-indigo-700 dark:text-indigo-300">
              (Câu trả lời đúng sẽ tự động được loại khỏi danh sách câu sai)
            </span>
          </div>

          {activeQuestions[currentIndex] && (
            <QuestionCard
              question={activeQuestions[currentIndex]}
              questionIndex={currentIndex}
              selectedAnswer={retakeAnswers[activeQuestions[currentIndex].id]}
              onSelectAnswer={(optIdx) => handleSelectRetakeAnswer(activeQuestions[currentIndex], optIdx)}
              mode="practice"
              showInstantFeedback={true}
              isBookmarked={isBookmarked(activeQuestions[currentIndex].id)}
              onToggleBookmark={() => toggleBookmark(activeQuestions[currentIndex].id)}
            />
          )}

          <div className="flex items-center justify-between pt-2">
            <button
              onClick={() => setCurrentIndex(Math.max(0, currentIndex - 1))}
              disabled={currentIndex === 0}
              className="px-4 py-2 rounded-xl text-xs font-bold border border-slate-300 dark:border-slate-700 disabled:opacity-30 cursor-pointer"
            >
              Câu trước
            </button>

            <button
              onClick={() => setCurrentIndex(Math.min(activeQuestions.length - 1, currentIndex + 1))}
              disabled={currentIndex === activeQuestions.length - 1}
              className="px-5 py-2 rounded-xl text-xs font-bold bg-indigo-600 hover:bg-indigo-700 text-white disabled:opacity-30 cursor-pointer"
            >
              Câu tiếp theo
            </button>
          </div>
        </div>
      ) : (
        /* List of Questions with Remove Option */
        <div className="space-y-4">
          {activeQuestions.map((q, idx) => (
            <div key={q.id} className="relative">
              <div className="flex justify-end mb-1">
                {activeTab === 'mistakes' && (
                  <button
                    onClick={() => removeMistake(q.id)}
                    className="text-[11px] font-semibold text-rose-600 hover:text-rose-800 dark:text-rose-400 hover:underline inline-flex items-center gap-1 cursor-pointer"
                  >
                    <Trash2 size={12} />
                    <span>Xoá câu này khỏi sổ tay</span>
                  </button>
                )}
              </div>
              <QuestionCard
                question={q}
                questionIndex={idx}
                selectedAnswer={null}
                onSelectAnswer={() => {}}
                mode="review"
                showInstantFeedback={true}
                isBookmarked={isBookmarked(q.id)}
                onToggleBookmark={() => toggleBookmark(q.id)}
              />
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
