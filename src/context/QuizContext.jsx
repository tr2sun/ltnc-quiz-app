import React, { createContext, useContext, useState, useEffect } from 'react';

const QuizContext = createContext();

const STORAGE_KEYS = {
  MISTAKES: 'ltnc_quiz_mistakes_v1',
  BOOKMARKS: 'ltnc_quiz_bookmarks_v1',
  HISTORY: 'ltnc_quiz_history_v1',
  PROGRESS: 'ltnc_quiz_lesson_progress_v1',
  PREFERENCES: 'ltnc_quiz_user_prefs_v1',
};

const DEFAULT_PREFERENCES = {
  theme: 'light',
  instantExplanation: true,
  examViewMode: 'card', // 'card' or 'continuous'
  defaultExamTimer: 40, // 40 minutes
  shuffleQuestions: false,
};

export function QuizProvider({ children }) {
  // Mistakes: { [questionId]: { count: number, lastWrongAnswer: number, updatedAt: string } }
  const [mistakes, setMistakes] = useState(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEYS.MISTAKES);
      return saved ? JSON.parse(saved) : {};
    } catch (e) {
      console.error('Failed to load mistakes from localStorage', e);
      return {};
    }
  });

  // Bookmarks: Array of question IDs
  const [bookmarks, setBookmarks] = useState(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEYS.BOOKMARKS);
      return saved ? JSON.parse(saved) : [];
    } catch (e) {
      console.error('Failed to load bookmarks', e);
      return [];
    }
  });

  // History: Array of completed quiz records
  const [quizHistory, setQuizHistory] = useState(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEYS.HISTORY);
      return saved ? JSON.parse(saved) : [];
    } catch (e) {
      console.error('Failed to load history', e);
      return [];
    }
  });

  // Lesson progress: { [lessonId]: { answered: number, correct: number } }
  const [lessonProgress, setLessonProgress] = useState(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEYS.PROGRESS);
      return saved ? JSON.parse(saved) : {};
    } catch (e) {
      console.error('Failed to load progress', e);
      return {};
    }
  });

  // User preferences
  const [preferences, setPreferences] = useState(() => {
    try {
      const saved = localStorage.getItem(STORAGE_KEYS.PREFERENCES);
      return saved ? { ...DEFAULT_PREFERENCES, ...JSON.parse(saved) } : DEFAULT_PREFERENCES;
    } catch (e) {
      console.error('Failed to load preferences', e);
      return DEFAULT_PREFERENCES;
    }
  });

  // Save changes to localStorage
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEYS.MISTAKES, JSON.stringify(mistakes));
    } catch (e) {
      console.error(e);
    }
  }, [mistakes]);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEYS.BOOKMARKS, JSON.stringify(bookmarks));
    } catch (e) {
      console.error(e);
    }
  }, [bookmarks]);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEYS.HISTORY, JSON.stringify(quizHistory));
    } catch (e) {
      console.error(e);
    }
  }, [quizHistory]);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEYS.PROGRESS, JSON.stringify(lessonProgress));
    } catch (e) {
      console.error(e);
    }
  }, [lessonProgress]);

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEYS.PREFERENCES, JSON.stringify(preferences));
      if (preferences.theme === 'dark') {
        document.documentElement.classList.add('dark');
      } else {
        document.documentElement.classList.remove('dark');
      }
    } catch (e) {
      console.error(e);
    }
  }, [preferences]);

  // Mistakes actions
  const recordAnswerResult = (questionId, lessonId, isCorrect, chosenAnswer) => {
    // Update mistakes
    if (!isCorrect) {
      setMistakes(prev => {
        const existing = prev[questionId] || { count: 0 };
        return {
          ...prev,
          [questionId]: {
            count: existing.count + 1,
            lastWrongAnswer: chosenAnswer,
            updatedAt: new Date().toISOString()
          }
        };
      });
    } else {
      // Optional: If correct, we can decrement or remove from mistakes if practicing mistakes
    }

    // Update lesson progress
    if (lessonId) {
      setLessonProgress(prev => {
        const cur = prev[lessonId] || { answered: 0, correct: 0 };
        return {
          ...prev,
          [lessonId]: {
            answered: cur.answered + 1,
            correct: cur.correct + (isCorrect ? 1 : 0)
          }
        };
      });
    }
  };

  const removeMistake = (questionId) => {
    setMistakes(prev => {
      const next = { ...prev };
      delete next[questionId];
      return next;
    });
  };

  const clearAllMistakes = () => {
    setMistakes({});
  };

  const isMistake = (questionId) => {
    return Boolean(mistakes[questionId]);
  };

  // Bookmark actions
  const toggleBookmark = (questionId) => {
    setBookmarks(prev => {
      if (prev.includes(questionId)) {
        return prev.filter(id => id !== questionId);
      } else {
        return [...prev, questionId];
      }
    });
  };

  const isBookmarked = (questionId) => {
    return bookmarks.includes(questionId);
  };

  const clearAllBookmarks = () => {
    setBookmarks([]);
  };

  // History actions
  const addQuizHistory = (record) => {
    const newEntry = {
      id: 'history_' + Date.now(),
      timestamp: new Date().toISOString(),
      ...record
    };
    setQuizHistory(prev => [newEntry, ...prev.slice(0, 49)]); // keep latest 50
    return newEntry;
  };

  const clearHistory = () => {
    setQuizHistory([]);
  };

  // Preferences actions
  const updatePreference = (key, value) => {
    setPreferences(prev => ({ ...prev, [key]: value }));
  };

  const toggleTheme = () => {
    setPreferences(prev => ({
      ...prev,
      theme: prev.theme === 'dark' ? 'light' : 'dark'
    }));
  };

  return (
    <QuizContext.Provider
      value={{
        mistakes,
        bookmarks,
        quizHistory,
        lessonProgress,
        preferences,
        recordAnswerResult,
        removeMistake,
        clearAllMistakes,
        isMistake,
        toggleBookmark,
        isBookmarked,
        clearAllBookmarks,
        addQuizHistory,
        clearHistory,
        updatePreference,
        toggleTheme
      }}
    >
      {children}
    </QuizContext.Provider>
  );
}

export function useQuiz() {
  const context = useContext(QuizContext);
  if (!context) {
    throw new Error('useQuiz must be used within a QuizProvider');
  }
  return context;
}
