import React, { useState, useEffect, useMemo } from 'react';
import { 
  GraduationCap, 
  Clock, 
  Send, 
  Layers, 
  ListOrdered, 
  RotateCcw, 
  AlertTriangle, 
  CheckCircle, 
  ChevronLeft, 
  ChevronRight,
  Eye,
  Settings,
  HelpCircle
} from 'lucide-react';
import { EXAM_PRESETS, getExamQuestions, getAllQuestions } from '../data';
import { useQuiz } from '../context/QuizContext';
import QuestionCard from '../components/QuestionCard';
import QuizNavigation from '../components/QuizNavigation';
import Timer from '../components/Timer';
import ResultModal from '../components/ResultModal';

export default function ExamPage({ onNavigate }) {
  // Preset & Configuration
  const [selectedPresetId, setSelectedPresetId] = useState('exam-101');
  const [timerDuration, setTimerDuration] = useState(40); // 40, 30, or 0 (untimed)
  const [isExamStarted, setIsExamStarted] = useState(false);
  const [isExamSubmitted, setIsExamSubmitted] = useState(false);
  const [isReviewMode, setIsReviewMode] = useState(false);
  const [reviewFilter, setReviewFilter] = useState('all'); // 'all' or 'wrong'

  // View mode: 'card' (1 question at a time + palette) or 'continuous' (Google Form style)
  const [viewMode, setViewMode] = useState('card');
  const [currentCardIndex, setCurrentCardIndex] = useState(0);

  // Exam state
  const [examQuestions, setExamQuestions] = useState([]);
  const [userAnswers, setUserAnswers] = useState({}); // { [index]: optionIndex }
  const [timeSpentSeconds, setTimeSpentSeconds] = useState(0);
  const [isSubmitModalOpen, setIsSubmitModalOpen] = useState(false);
  const [isResultModalOpen, setIsResultModalOpen] = useState(false);

  const { 
    recordAnswerResult, 
    toggleBookmark, 
    isBookmarked, 
    addQuizHistory 
  } = useQuiz();

  // Start exam handler
  const handleStartExam = (presetId = selectedPresetId) => {
    const qList = getExamQuestions(presetId, 30);
    setExamQuestions(qList);
    setUserAnswers({});
    setCurrentCardIndex(0);
    setTimeSpentSeconds(0);
    setIsExamStarted(true);
    setIsExamSubmitted(false);
    setIsReviewMode(false);
    setIsResultModalOpen(false);
    setIsSubmitModalOpen(false);
  };

  const handleSelectAnswer = (qIndex, optionIndex) => {
    if (isExamSubmitted && !isReviewMode) return;
    setUserAnswers(prev => ({
      ...prev,
      [qIndex]: optionIndex
    }));
  };

  const handleTimeUp = () => {
    alert('Đã hết thời gian làm bài! Hệ thống đang tự động nộp bài của bạn.');
    handleSubmitFinal();
  };

  const handleSubmitFinal = () => {
    setIsSubmitModalOpen(false);
    setIsExamSubmitted(true);

    // Compute score
    let score = 0;
    examQuestions.forEach((q, idx) => {
      const chosen = userAnswers[idx];
      const isCorrect = chosen === q.correctAnswer;
      if (isCorrect) score += 1;
      // Record answer result
      recordAnswerResult(q.id, q.lessonId, isCorrect, chosen);
    });

    // Save to history
    const presetObj = EXAM_PRESETS.find(p => p.id === selectedPresetId);
    addQuizHistory({
      type: 'exam',
      presetId: selectedPresetId,
      title: presetObj ? presetObj.title : 'Đề thi thử 30 câu',
      score,
      total: examQuestions.length,
      percentage: Math.round((score / examQuestions.length) * 100),
      timeSpentSeconds,
      answers: userAnswers
    });

    setIsResultModalOpen(true);
  };

  const handleJumpToQuestion = (index) => {
    if (viewMode === 'card') {
      setCurrentCardIndex(index);
    } else {
      // Continuous Google Form style: smooth scroll to question card
      const targetQuestion = examQuestions[index];
      if (targetQuestion) {
        const el = document.getElementById(`question-${targetQuestion.id}`);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }
    }
  };

  // Score calculation for review mode
  const currentScore = useMemo(() => {
    let score = 0;
    examQuestions.forEach((q, idx) => {
      if (userAnswers[idx] === q.correctAnswer) score++;
    });
    return score;
  }, [examQuestions, userAnswers]);

  const answeredCount = Object.keys(userAnswers).filter(k => userAnswers[k] !== undefined).length;
  const unansweredCount = examQuestions.length - answeredCount;

  // Filtered list for review mode if 'wrong' selected
  const displayQuestions = useMemo(() => {
    if (!isReviewMode || reviewFilter === 'all') {
      return examQuestions;
    }
    return examQuestions.filter((q, idx) => userAnswers[idx] !== q.correctAnswer);
  }, [examQuestions, isReviewMode, reviewFilter, userAnswers]);

  return (
    <div className="space-y-6 pb-12">
      {/* 1. Exam Configuration Screen (Before starting) */}
      {!isExamStarted && (
        <div className="max-w-3xl mx-auto space-y-6">
          <div className="text-center space-y-3">
            <div className="inline-flex p-3.5 rounded-2xl bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400">
              <GraduationCap size={36} />
            </div>
            <h1 className="text-2xl sm:text-3xl font-black text-slate-800 dark:text-slate-100">
              Phòng Thi Thử Trắc Nghiệm LTNC
            </h1>
            <p className="text-slate-500 dark:text-slate-400 text-sm max-w-lg mx-auto">
              Mô phỏng kỳ thi trắc nghiệm học kỳ: 30 câu hỏi chọn lọc từ 9 bài học, phân loại theo độ khó và bẫy code JVM.
            </p>
          </div>

          {/* Exam Presets Selection */}
          <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200/80 dark:border-slate-800 p-6 shadow-sm space-y-5">
            <h3 className="font-bold text-sm text-slate-800 dark:text-slate-200">
              1. Chọn bộ đề thi
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
              {EXAM_PRESETS.map((preset) => {
                const isSelected = selectedPresetId === preset.id;
                return (
                  <div
                    key={preset.id}
                    onClick={() => setSelectedPresetId(preset.id)}
                    className={`p-4 rounded-2xl border-2 transition-all cursor-pointer text-left ${
                      isSelected
                        ? 'border-indigo-600 bg-indigo-50/50 dark:bg-indigo-950/40 text-indigo-950 dark:text-indigo-200 shadow-sm'
                        : 'border-slate-200 dark:border-slate-800 hover:border-indigo-300'
                    }`}
                  >
                    <div className="flex items-center justify-between mb-2">
                      <span className="font-extrabold text-sm text-indigo-600 dark:text-indigo-400">
                        {preset.code}
                      </span>
                      <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400">
                        30 câu
                      </span>
                    </div>
                    <h4 className="font-bold text-xs text-slate-800 dark:text-slate-100 mb-1">
                      {preset.title}
                    </h4>
                    <p className="text-[11px] text-slate-500 dark:text-slate-400 line-clamp-2">
                      {preset.description}
                    </p>
                  </div>
                );
              })}
            </div>

            {/* Timer setting */}
            <h3 className="font-bold text-sm text-slate-800 dark:text-slate-200 pt-2">
              2. Cài đặt thời gian làm bài
            </h3>
            <div className="grid grid-cols-3 gap-3">
              {[
                { label: '40 phút (Chuẩn thi UET)', value: 40 },
                { label: '30 phút (Tốc độ cao)', value: 30 },
                { label: 'Không giới hạn thời gian', value: 0 }
              ].map((opt) => (
                <button
                  key={opt.value}
                  onClick={() => setTimerDuration(opt.value)}
                  className={`py-3 px-3 rounded-xl border text-xs font-bold transition cursor-pointer text-center ${
                    timerDuration === opt.value
                      ? 'border-indigo-600 bg-indigo-600 text-white'
                      : 'border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300'
                  }`}
                >
                  {opt.label}
                </button>
              ))}
            </div>

            {/* View Mode default */}
            <h3 className="font-bold text-sm text-slate-800 dark:text-slate-200 pt-2">
              3. Chọn chế độ hiển thị mặc định
            </h3>
            <div className="grid grid-cols-2 gap-3">
              <button
                onClick={() => setViewMode('card')}
                className={`flex items-center justify-center gap-2 py-3 px-3 rounded-xl border text-xs font-bold transition cursor-pointer ${
                  viewMode === 'card'
                    ? 'border-indigo-600 bg-indigo-50 dark:bg-indigo-950/60 text-indigo-700 dark:text-indigo-300'
                    : 'border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300'
                }`}
              >
                <Layers size={16} />
                <span>Thẻ từng câu + Palette</span>
              </button>
              <button
                onClick={() => setViewMode('continuous')}
                className={`flex items-center justify-center gap-2 py-3 px-3 rounded-xl border text-xs font-bold transition cursor-pointer ${
                  viewMode === 'continuous'
                    ? 'border-indigo-600 bg-indigo-50 dark:bg-indigo-950/60 text-indigo-700 dark:text-indigo-300'
                    : 'border-slate-200 dark:border-slate-800 text-slate-700 dark:text-slate-300'
                }`}
              >
                <ListOrdered size={16} />
                <span>Cuộn liên tục (Google Form style)</span>
              </button>
            </div>

            {/* Launch Exam CTA */}
            <div className="pt-4">
              <button
                onClick={() => handleStartExam()}
                className="w-full py-4 rounded-2xl font-black text-base bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 text-white shadow-xl shadow-indigo-500/25 transition transform hover:-translate-y-0.5 cursor-pointer flex items-center justify-center gap-2"
              >
                <GraduationCap size={22} />
                <span>Bắt Đầu Làm Bài Thi Ngay</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* 2. Active Exam / Review Mode View */}
      {isExamStarted && (
        <div className="space-y-5">
          {/* Sticky Header Bar during exam */}
          <div className="sticky top-16 z-30 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md p-4 rounded-2xl border border-slate-200/80 dark:border-slate-800 shadow-md flex flex-wrap items-center justify-between gap-3">
            <div className="flex items-center gap-3">
              <div className="flex items-center gap-2">
                <span className="font-extrabold text-sm sm:text-base text-slate-800 dark:text-slate-100">
                  {isReviewMode ? 'Xem lại bài thi' : 'Đang làm bài thi'}
                </span>
                <span className="px-2 py-0.5 rounded text-[11px] font-bold bg-indigo-100 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300">
                  {examQuestions.length} câu
                </span>
              </div>

              {/* View Switcher Toggle */}
              <div className="hidden sm:flex items-center bg-slate-100 dark:bg-slate-800 rounded-xl p-1 text-xs">
                <button
                  onClick={() => setViewMode('card')}
                  className={`flex items-center gap-1.5 px-3 py-1 rounded-lg font-semibold transition cursor-pointer ${
                    viewMode === 'card'
                      ? 'bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-300 shadow-sm'
                      : 'text-slate-600 dark:text-slate-400'
                  }`}
                  title="Chế độ hiển thị thẻ từng câu"
                >
                  <Layers size={13} />
                  <span>Card</span>
                </button>
                <button
                  onClick={() => setViewMode('continuous')}
                  className={`flex items-center gap-1.5 px-3 py-1 rounded-lg font-semibold transition cursor-pointer ${
                    viewMode === 'continuous'
                      ? 'bg-white dark:bg-slate-700 text-indigo-600 dark:text-indigo-300 shadow-sm'
                      : 'text-slate-600 dark:text-slate-400'
                  }`}
                  title="Chế độ cuộn liên tục Google Form"
                >
                  <ListOrdered size={13} />
                  <span>Cuộn liên tục</span>
                </button>
              </div>
            </div>

            {/* Timer & Submit / Review Actions */}
            <div className="flex items-center gap-3">
              {!isExamSubmitted ? (
                <>
                  <Timer
                    initialMinutes={timerDuration}
                    isUntimed={timerDuration === 0}
                    isRunning={!isExamSubmitted}
                    onTimeUp={handleTimeUp}
                    onTick={(elapsed) => setTimeSpentSeconds(elapsed)}
                  />
                  <button
                    onClick={() => setIsSubmitModalOpen(true)}
                    className="flex items-center gap-1.5 px-4 py-2 rounded-xl text-xs font-extrabold bg-indigo-600 hover:bg-indigo-700 text-white shadow-md shadow-indigo-500/20 transition cursor-pointer"
                  >
                    <Send size={14} />
                    <span>Nộp bài</span>
                  </button>
                </>
              ) : (
                <div className="flex items-center gap-2">
                  <span className="font-bold text-xs px-3 py-1.5 rounded-xl bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-800">
                    Điểm: {currentScore}/{examQuestions.length} ({Math.round((currentScore / examQuestions.length) * 100)}%)
                  </span>

                  <button
                    onClick={() => setIsResultModalOpen(true)}
                    className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-indigo-50 dark:bg-indigo-950 text-indigo-600 dark:text-indigo-400 cursor-pointer"
                  >
                    <Eye size={14} />
                    <span>Xem bảng điểm</span>
                  </button>

                  <button
                    onClick={() => handleStartExam()}
                    className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 cursor-pointer"
                  >
                    <RotateCcw size={14} />
                    <span>Thi lại</span>
                  </button>
                </div>
              )}
            </div>
          </div>

          {/* Filter options when in Review mode */}
          {isReviewMode && (
            <div className="flex items-center gap-2 p-3 bg-white dark:bg-slate-900 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
              <span className="font-semibold text-slate-600 dark:text-slate-400">Xem:</span>
              <button
                onClick={() => setReviewFilter('all')}
                className={`px-3 py-1 rounded-lg font-bold transition cursor-pointer ${
                  reviewFilter === 'all'
                    ? 'bg-indigo-600 text-white'
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                }`}
              >
                Tất cả ({examQuestions.length})
              </button>
              <button
                onClick={() => setReviewFilter('wrong')}
                className={`px-3 py-1 rounded-lg font-bold transition cursor-pointer ${
                  reviewFilter === 'wrong'
                    ? 'bg-rose-600 text-white'
                    : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                }`}
              >
                Chỉ câu sai ({examQuestions.length - currentScore})
              </button>
            </div>
          )}

          {/* Main Layout: Left Questions / Right Palette */}
          <div className="grid grid-cols-1 lg:grid-cols-4 gap-6 items-start">
            
            {/* Questions View */}
            <div className="lg:col-span-3 space-y-4">
              
              {/* DUAL VIEW OPTION 1: CARD VIEW */}
              {viewMode === 'card' && (
                <div>
                  {displayQuestions[currentCardIndex] && (
                    <QuestionCard
                      question={displayQuestions[currentCardIndex]}
                      questionIndex={currentCardIndex}
                      selectedAnswer={userAnswers[currentCardIndex]}
                      onSelectAnswer={(optIdx) => handleSelectAnswer(currentCardIndex, optIdx)}
                      mode={isReviewMode ? 'review' : 'exam'}
                      isBookmarked={isBookmarked(displayQuestions[currentCardIndex].id)}
                      onToggleBookmark={() => toggleBookmark(displayQuestions[currentCardIndex].id)}
                    />
                  )}

                  {/* Previous / Next Navigation Buttons for Card view */}
                  <div className="flex items-center justify-between pt-2">
                    <button
                      onClick={() => setCurrentCardIndex(Math.max(0, currentCardIndex - 1))}
                      disabled={currentCardIndex === 0}
                      className="flex items-center gap-2 px-4 py-2.5 rounded-xl border border-slate-300 dark:border-slate-700 text-slate-700 dark:text-slate-300 text-xs font-bold disabled:opacity-30 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer"
                    >
                      <ChevronLeft size={16} />
                      <span>Câu trước</span>
                    </button>

                    <div className="text-xs font-medium text-slate-500">
                      {currentCardIndex + 1} / {displayQuestions.length}
                    </div>

                    <button
                      onClick={() => setCurrentCardIndex(Math.min(displayQuestions.length - 1, currentCardIndex + 1))}
                      disabled={currentCardIndex === displayQuestions.length - 1}
                      className="flex items-center gap-2 px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold disabled:opacity-30 shadow-md shadow-indigo-500/20 cursor-pointer"
                    >
                      <span>Câu sau</span>
                      <ChevronRight size={16} />
                    </button>
                  </div>
                </div>
              )}

              {/* DUAL VIEW OPTION 2: CONTINUOUS SCROLL VIEW (GOOGLE FORM STYLE) */}
              {viewMode === 'continuous' && (
                <div className="space-y-4">
                  {displayQuestions.map((q, idx) => (
                    <QuestionCard
                      key={q.id}
                      question={q}
                      questionIndex={idx}
                      selectedAnswer={userAnswers[idx]}
                      onSelectAnswer={(optIdx) => handleSelectAnswer(idx, optIdx)}
                      mode={isReviewMode ? 'review' : 'exam'}
                      isBookmarked={isBookmarked(q.id)}
                      onToggleBookmark={() => toggleBookmark(q.id)}
                    />
                  ))}

                  {!isExamSubmitted && (
                    <div className="p-6 bg-white dark:bg-slate-900 rounded-2xl border border-slate-200 dark:border-slate-800 text-center space-y-3">
                      <p className="text-xs text-slate-500 dark:text-slate-400">
                        Bạn đã trả lời {answeredCount} / {examQuestions.length} câu hỏi.
                      </p>
                      <button
                        onClick={() => setIsSubmitModalOpen(true)}
                        className="px-6 py-3 rounded-xl font-bold text-sm bg-indigo-600 hover:bg-indigo-700 text-white shadow-lg shadow-indigo-500/25 cursor-pointer"
                      >
                        Nộp Bài Thi
                      </button>
                    </div>
                  )}
                </div>
              )}
            </div>

            {/* Right Side: Quiz Navigation Palette 1..30 */}
            <div className="lg:col-span-1">
              <QuizNavigation
                totalQuestions={examQuestions.length}
                currentIndex={currentCardIndex}
                onJumpToQuestion={handleJumpToQuestion}
                answers={userAnswers}
                isQuestionBookmarked={(qId) => isBookmarked(qId)}
                onSubmitQuiz={() => setIsSubmitModalOpen(true)}
                mode={isReviewMode ? 'review' : 'exam'}
                questions={examQuestions}
              />
            </div>
          </div>
        </div>
      )}

      {/* Submit Confirmation Dialog */}
      {isSubmitModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm">
          <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 p-6 max-w-md w-full shadow-2xl space-y-4">
            <div className="flex items-center gap-3">
              <div className="p-3 rounded-2xl bg-amber-50 dark:bg-amber-950/60 text-amber-600 dark:text-amber-400">
                <AlertTriangle size={24} />
              </div>
              <div>
                <h3 className="font-extrabold text-lg text-slate-800 dark:text-slate-100">
                  Xác nhận nộp bài?
                </h3>
                <p className="text-xs text-slate-500 dark:text-slate-400">
                  Bạn có chắc chắn muốn kết thúc bài thi ngay bây giờ?
                </p>
              </div>
            </div>

            <div className="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/60 space-y-2 text-xs">
              <div className="flex justify-between">
                <span className="text-slate-500">Đã trả lời:</span>
                <span className="font-bold text-indigo-600 dark:text-indigo-400">
                  {answeredCount} / {examQuestions.length} câu
                </span>
              </div>
              {unansweredCount > 0 && (
                <div className="flex justify-between text-amber-600 dark:text-amber-400 font-semibold">
                  <span>Chưa trả lời:</span>
                  <span>{unansweredCount} câu</span>
                </div>
              )}
            </div>

            <div className="grid grid-cols-2 gap-3 pt-2">
              <button
                onClick={() => setIsSubmitModalOpen(false)}
                className="py-2.5 rounded-xl text-xs font-bold border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 cursor-pointer"
              >
                Tiếp tục làm
              </button>
              <button
                onClick={handleSubmitFinal}
                className="py-2.5 rounded-xl text-xs font-bold bg-indigo-600 hover:bg-indigo-700 text-white shadow-md shadow-indigo-500/20 cursor-pointer"
              >
                Nộp bài ngay
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Result Modal */}
      <ResultModal
        isOpen={isResultModalOpen}
        onClose={() => setIsResultModalOpen(false)}
        score={currentScore}
        total={examQuestions.length}
        timeSpentSeconds={timeSpentSeconds}
        questions={examQuestions}
        answers={userAnswers}
        onRetake={() => handleStartExam()}
        onReviewMode={() => {
          setIsReviewMode(true);
          setViewMode('card');
          setCurrentCardIndex(0);
        }}
        onGoToMistakes={() => onNavigate('mistakes')}
      />
    </div>
  );
}
