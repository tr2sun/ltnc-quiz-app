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
  HelpCircle,
  BookOpen,
  Sparkles,
  Zap
} from 'lucide-react';
import { 
  EXAM_PRESETS, 
  getExamQuestions, 
  getAllQuestions,
  LESSONS_METADATA,
  SECTION_PRESETS,
  getPresetsForLesson,
  getSectionQuestions
} from '../data';
import { useQuiz } from '../context/QuizContext';
import QuestionCard, { isAnswerCorrect } from '../components/QuestionCard';
import QuizNavigation from '../components/QuizNavigation';
import Timer from '../components/Timer';
import ResultModal from '../components/ResultModal';

export default function ExamPage({ onNavigate, examParams = null }) {
  // Main Category Tab: 'general' (30 questions) vs 'section' (15 questions per lesson)
  const [examCategory, setExamCategory] = useState(examParams?.category || 'general');

  // General 30-question presets
  const [selectedGeneralPresetId, setSelectedGeneralPresetId] = useState('exam-101');

  // Section 15-question presets
  const [selectedLessonId, setSelectedLessonId] = useState(examParams?.lessonId || 1);
  const [selectedSectionPresetId, setSelectedSectionPresetId] = useState(examParams?.presetId || 'random');

  // Timer duration in minutes: default 40 for 30 questions, 20 for 15 questions
  const [timerDuration, setTimerDuration] = useState(examCategory === 'section' ? 20 : 40);

  // Exam runtime state
  const [isExamStarted, setIsExamStarted] = useState(false);
  const [isExamSubmitted, setIsExamSubmitted] = useState(false);
  const [isReviewMode, setIsReviewMode] = useState(false);
  const [reviewFilter, setReviewFilter] = useState('all'); // 'all' or 'wrong'
  const [examTitle, setExamTitle] = useState('Đề thi trắc nghiệm LTNC');

  // View mode: 'card' (single question card + palette) or 'continuous' (Google Form style)
  const [viewMode, setViewMode] = useState('card');
  const [currentCardIndex, setCurrentCardIndex] = useState(0);

  // Questions and user selections
  const [examQuestions, setExamQuestions] = useState([]);
  const [userAnswers, setUserAnswers] = useState({}); // { [index]: optionIndex or [indices] }
  const [timeSpentSeconds, setTimeSpentSeconds] = useState(0);
  const [isSubmitModalOpen, setIsSubmitModalOpen] = useState(false);
  const [isResultModalOpen, setIsResultModalOpen] = useState(false);

  const { 
    recordAnswerResult, 
    toggleBookmark, 
    isBookmarked, 
    addQuizHistory 
  } = useQuiz();

  // If examParams were passed from HomePage, auto configure
  useEffect(() => {
    if (examParams) {
      if (examParams.category) setExamCategory(examParams.category);
      if (examParams.lessonId) setSelectedLessonId(examParams.lessonId);
      if (examParams.presetId) setSelectedSectionPresetId(examParams.presetId);
      if (examParams.autoStart) {
        handleStartExam(examParams.category, examParams.lessonId, examParams.presetId);
      }
    }
  }, [examParams]);

  // Adjust default timer when switching exam category
  const handleSwitchCategory = (cat) => {
    setExamCategory(cat);
    if (cat === 'section') {
      setTimerDuration(20);
    } else {
      setTimerDuration(40);
    }
  };

  // Start exam handler
  const handleStartExam = (category = examCategory, lessonId = selectedLessonId, sectionPresetId = selectedSectionPresetId) => {
    let qList = [];
    let title = '';

    if (category === 'section') {
      qList = getSectionQuestions(lessonId, sectionPresetId);
      const lessonMeta = LESSONS_METADATA.find(l => l.id === Number(lessonId));
      const presets = getPresetsForLesson(lessonId);
      const presetObj = presets.find(p => p.id === sectionPresetId);
      const presetName = presetObj ? presetObj.title : 'Đề ngẫu nhiên 15 câu';
      title = `${lessonMeta ? lessonMeta.title : `Bài ${lessonId}`} - ${presetName}`;
    } else {
      qList = getExamQuestions(selectedGeneralPresetId, 30);
      const presetObj = EXAM_PRESETS.find(p => p.id === selectedGeneralPresetId);
      title = presetObj ? presetObj.title : 'Đề thi thử 30 câu chuẩn UET';
    }

    setExamTitle(title);
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

  const handleSelectAnswer = (qIndex, selection) => {
    if (isExamSubmitted && !isReviewMode) return;
    setUserAnswers(prev => ({
      ...prev,
      [qIndex]: selection
    }));
  };

  const handleTimeUp = () => {
    alert('Đã hết thời gian làm bài! Hệ thống đang tự động nộp bài của bạn.');
    handleSubmitFinal();
  };

  const handleSubmitFinal = () => {
    setIsSubmitModalOpen(false);
    setIsExamSubmitted(true);

    // Compute score using exact match via isAnswerCorrect
    let score = 0;
    examQuestions.forEach((q, idx) => {
      const chosen = userAnswers[idx];
      const isCorrect = isAnswerCorrect(q, chosen);
      if (isCorrect) score += 1;
      // Record answer result for analytics and mistakes
      recordAnswerResult(q.id, q.lessonId, isCorrect, chosen);
    });

    // Save to history
    addQuizHistory({
      type: 'exam',
      category: examCategory,
      title: examTitle,
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
      if (isAnswerCorrect(q, userAnswers[idx])) score++;
    });
    return score;
  }, [examQuestions, userAnswers]);

  const answeredCount = Object.keys(userAnswers).filter(k => {
    const val = userAnswers[k];
    if (val === undefined || val === null) return false;
    if (Array.isArray(val)) return val.length > 0;
    return true;
  }).length;

  const unansweredCount = examQuestions.length - answeredCount;

  // Filtered list for review mode if 'wrong' selected
  const displayQuestions = useMemo(() => {
    if (!isReviewMode || reviewFilter === 'all') {
      return examQuestions;
    }
    return examQuestions.filter((q, idx) => !isAnswerCorrect(q, userAnswers[idx]));
  }, [examQuestions, isReviewMode, reviewFilter, userAnswers]);

  // Section presets for the currently selected lesson
  const currentLessonPresets = useMemo(() => {
    return getPresetsForLesson(selectedLessonId);
  }, [selectedLessonId]);

  return (
    <div className="space-y-6 pb-12">
      {/* 1. Exam Configuration Screen (Before starting) */}
      {!isExamStarted && (
        <div className="max-w-4xl mx-auto space-y-6">
          <div className="text-center space-y-3">
            <div className="inline-flex p-3.5 rounded-2xl bg-indigo-50 dark:bg-indigo-950/60 text-indigo-600 dark:text-indigo-400">
              <GraduationCap size={36} />
            </div>
            <h1 className="text-2xl sm:text-3xl font-black text-slate-800 dark:text-slate-100">
              Phòng Thi Trắc Nghiệm LTNC (UET - CS2043)
            </h1>
            <p className="text-slate-500 dark:text-slate-400 text-sm max-w-lg mx-auto">
              Luyện thi trắc nghiệm chuẩn cấu trúc: Hỗ trợ đề tổng hợp 30 câu (40 phút) và đề chuyên đề 15 câu theo từng bài (20 phút).
            </p>
          </div>

          {/* 2 Primary Mode Tabs: Tổng hợp vs Chuyên đề */}
          <div className="flex p-1.5 bg-slate-200/80 dark:bg-slate-800 rounded-2xl max-w-md mx-auto">
            <button
              onClick={() => handleSwitchCategory('general')}
              className={`flex-1 py-2.5 rounded-xl text-xs sm:text-sm font-bold transition cursor-pointer flex items-center justify-center gap-2 ${
                examCategory === 'general'
                  ? 'bg-white dark:bg-slate-900 text-indigo-600 dark:text-indigo-400 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
              }`}
            >
              <Zap size={16} />
              <span>Đề tổng hợp (30 câu)</span>
            </button>

            <button
              onClick={() => handleSwitchCategory('section')}
              className={`flex-1 py-2.5 rounded-xl text-xs sm:text-sm font-bold transition cursor-pointer flex items-center justify-center gap-2 ${
                examCategory === 'section'
                  ? 'bg-white dark:bg-slate-900 text-indigo-600 dark:text-indigo-400 shadow-sm'
                  : 'text-slate-600 dark:text-slate-400 hover:text-slate-900'
              }`}
            >
              <BookOpen size={16} />
              <span>Đề chuyên đề theo bài (15 câu)</span>
            </button>
          </div>

          <div className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200/80 dark:border-slate-800 p-6 shadow-sm space-y-6">
            
            {/* TAB 1: ĐỀ TỔNG HỢP 30 CÂU */}
            {examCategory === 'general' && (
              <div className="space-y-4">
                <h3 className="font-bold text-sm text-slate-800 dark:text-slate-200">
                  1. Chọn mã đề tổng hợp (30 câu)
                </h3>
                <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-3">
                  {EXAM_PRESETS.map((preset) => {
                    const isSelected = selectedGeneralPresetId === preset.id;
                    return (
                      <div
                        key={preset.id}
                        onClick={() => setSelectedGeneralPresetId(preset.id)}
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
              </div>
            )}

            {/* TAB 2: ĐỀ CHUYÊN ĐỀ THEO BÀI 15 CÂU */}
            {examCategory === 'section' && (
              <div className="space-y-5">
                <div>
                  <h3 className="font-bold text-sm text-slate-800 dark:text-slate-200 mb-2">
                    1. Chọn bài học chuyên đề
                  </h3>
                  <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-2">
                    {LESSONS_METADATA.map((l) => (
                      <button
                        key={l.id}
                        onClick={() => {
                          setSelectedLessonId(l.id);
                          setSelectedSectionPresetId('random');
                        }}
                        className={`p-2.5 rounded-xl border text-xs font-bold transition text-left cursor-pointer ${
                          selectedLessonId === l.id
                            ? 'border-indigo-600 bg-indigo-600 text-white shadow-sm'
                            : 'border-slate-200 dark:border-slate-800 hover:border-indigo-300 bg-slate-50 dark:bg-slate-850 text-slate-700 dark:text-slate-300'
                        }`}
                      >
                        <div className="text-[10px] opacity-80">Bài {l.id}</div>
                        <div className="truncate text-xs">{l.title.split(':')[1]?.trim() || l.title}</div>
                      </button>
                    ))}
                  </div>
                </div>

                <div>
                  <h3 className="font-bold text-sm text-slate-800 dark:text-slate-200 mb-2">
                    2. Chọn mã đề 15 câu (Không trùng lặp câu hỏi)
                  </h3>
                  <div className="grid grid-cols-1 sm:grid-cols-4 gap-3">
                    {/* Fixed presets: Đề A, Đề B, Đề C... */}
                    {currentLessonPresets.map((p) => {
                      const isSelected = selectedSectionPresetId === p.id;
                      return (
                        <div
                          key={p.id}
                          onClick={() => setSelectedSectionPresetId(p.id)}
                          className={`p-3.5 rounded-2xl border-2 transition-all cursor-pointer text-left ${
                            isSelected
                              ? 'border-indigo-600 bg-indigo-50/60 dark:bg-indigo-950/40 text-indigo-950 dark:text-indigo-200'
                              : 'border-slate-200 dark:border-slate-800 hover:border-indigo-300'
                          }`}
                        >
                          <div className="flex items-center justify-between mb-1">
                            <span className="font-black text-sm text-indigo-600 dark:text-indigo-400">
                              {p.code}
                            </span>
                            <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-indigo-100 dark:bg-indigo-950 text-indigo-700 dark:text-indigo-300">
                              15 câu
                            </span>
                          </div>
                          <p className="text-xs font-bold text-slate-700 dark:text-slate-200">
                            {p.title}
                          </p>
                          <p className="text-[10px] text-slate-400 mt-1">
                            Đề thi cố định chuẩn hóa
                          </p>
                        </div>
                      );
                    })}

                    {/* Random 15-question preset */}
                    <div
                      onClick={() => setSelectedSectionPresetId('random')}
                      className={`p-3.5 rounded-2xl border-2 transition-all cursor-pointer text-left ${
                        selectedSectionPresetId === 'random'
                          ? 'border-indigo-600 bg-indigo-50/60 dark:bg-indigo-950/40 text-indigo-950 dark:text-indigo-200'
                          : 'border-slate-200 dark:border-slate-800 hover:border-indigo-300'
                      }`}
                    >
                      <div className="flex items-center justify-between mb-1">
                        <span className="font-black text-sm text-purple-600 dark:text-purple-400">
                          Đề Ngẫu Nhiên
                        </span>
                        <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-purple-100 dark:bg-purple-950 text-purple-700 dark:text-purple-300">
                          15 câu
                        </span>
                      </div>
                      <p className="text-xs font-bold text-slate-700 dark:text-slate-200">
                        Xáo trộn ngẫu nhiên
                      </p>
                      <p className="text-[10px] text-slate-400 mt-1">
                        Lấy 15 câu bất kỳ trong bài
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            )}

            {/* Timer setting */}
            <div>
              <h3 className="font-bold text-sm text-slate-800 dark:text-slate-200 mb-2">
                {examCategory === 'general' ? '2. Thời gian làm bài (Chuẩn 40 phút)' : '3. Thời gian làm bài (Chuẩn 20 phút)'}
              </h3>
              <div className="grid grid-cols-3 gap-3">
                {[
                  { label: examCategory === 'general' ? '40 phút (Chuẩn)' : '20 phút (Chuẩn)', value: examCategory === 'general' ? 40 : 20 },
                  { label: examCategory === 'general' ? '30 phút (Nhanh)' : '15 phút (Nhanh)', value: examCategory === 'general' ? 30 : 15 },
                  { label: 'Không giới hạn thời gian', value: 0 }
                ].map((opt) => (
                  <button
                    key={opt.value}
                    onClick={() => setTimerDuration(opt.value)}
                    className={`py-2.5 px-3 rounded-xl border text-xs font-bold transition cursor-pointer text-center ${
                      timerDuration === opt.value
                        ? 'border-indigo-600 bg-indigo-600 text-white'
                        : 'border-slate-200 dark:border-slate-800 bg-slate-50 dark:bg-slate-800 text-slate-700 dark:text-slate-300'
                    }`}
                  >
                    {opt.label}
                  </button>
                ))}
              </div>
            </div>

            {/* View Mode default */}
            <div>
              <h3 className="font-bold text-sm text-slate-800 dark:text-slate-200 mb-2">
                {examCategory === 'general' ? '3. Chọn chế độ xem' : '4. Chọn chế độ xem'}
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
            </div>

            {/* Launch Exam CTA */}
            <div className="pt-2">
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
                <span className="font-extrabold text-sm sm:text-base text-slate-800 dark:text-slate-100 truncate max-w-xs sm:max-w-md">
                  {isReviewMode ? 'Xem lại:' : ''} {examTitle}
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

                  <button
                    onClick={() => setIsExamStarted(false)}
                    className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 cursor-pointer"
                  >
                    <span>Đổi đề thi</span>
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
                      onSelectAnswer={(selection) => handleSelectAnswer(currentCardIndex, selection)}
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
                      onSelectAnswer={(selection) => handleSelectAnswer(idx, selection)}
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

            {/* Right Side: Quiz Navigation Palette 1..15 or 1..30 */}
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
