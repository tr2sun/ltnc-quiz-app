import React, { useState } from 'react';
import { QuizProvider } from './context/QuizContext';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import PracticePage from './pages/PracticePage';
import ExamPage from './pages/ExamPage';
import MistakesPage from './pages/MistakesPage';
import CheatSheetPage from './pages/CheatSheetPage';
import { GraduationCap, Heart, Github, Sparkles } from 'lucide-react';

export default function App() {
  const [activeTab, setActiveTab] = useState('home');
  const [selectedPracticeLesson, setSelectedPracticeLesson] = useState(1);

  const handleSelectLessonFromHome = (lessonId) => {
    setSelectedPracticeLesson(lessonId);
    setActiveTab('practice');
  };

  return (
    <QuizProvider>
      <div className="min-h-screen flex flex-col bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-100 transition-colors">
        {/* Navigation Bar */}
        <Navbar activeTab={activeTab} onSelectTab={setActiveTab} />

        {/* Main Content Area */}
        <main className="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 pt-6">
          {activeTab === 'home' && (
            <HomePage
              onNavigate={setActiveTab}
              onSelectLesson={handleSelectLessonFromHome}
            />
          )}

          {activeTab === 'practice' && (
            <PracticePage initialLessonId={selectedPracticeLesson} />
          )}

          {activeTab === 'exam' && (
            <ExamPage onNavigate={setActiveTab} />
          )}

          {activeTab === 'mistakes' && (
            <MistakesPage onNavigate={setActiveTab} />
          )}

          {activeTab === 'cheatsheet' && (
            <CheatSheetPage />
          )}
        </main>

        {/* Footer */}
        <footer className="border-t border-slate-200/80 dark:border-slate-800 bg-white dark:bg-slate-900 py-6 text-xs text-slate-500 dark:text-slate-400">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left">
            <div className="flex items-center gap-2">
              <span className="font-bold text-slate-700 dark:text-slate-300">
                LTNC Quiz Pro
              </span>
              <span>•</span>
              <span>Lập trình nâng cao (CS2043)</span>
              <span>•</span>
              <span>Trường Đại học Công nghệ - ĐHQGHN</span>
            </div>

            <div className="flex items-center gap-1 text-[11px]">
              <span>Xây dựng cho sinh viên UET</span>
              <Heart size={12} className="text-rose-500 fill-current" />
              <span>Ôn thi đạt điểm A+</span>
            </div>
          </div>
        </footer>
      </div>
    </QuizProvider>
  );
}
