import React, { useState, useEffect } from 'react';
import { Clock, AlertTriangle, Infinity } from 'lucide-react';

export default function Timer({
  initialMinutes = 40,
  onTimeUp,
  isRunning = true,
  isUntimed = false,
  onTick
}) {
  const [secondsRemaining, setSecondsRemaining] = useState(initialMinutes * 60);

  useEffect(() => {
    setSecondsRemaining(initialMinutes * 60);
  }, [initialMinutes]);

  useEffect(() => {
    if (isUntimed || !isRunning) return;

    if (secondsRemaining <= 0) {
      if (onTimeUp) onTimeUp();
      return;
    }

    const interval = setInterval(() => {
      setSecondsRemaining(prev => {
        const next = prev - 1;
        if (onTick) onTick((initialMinutes * 60) - next);
        if (next <= 0) {
          clearInterval(interval);
          if (onTimeUp) onTimeUp();
          return 0;
        }
        return next;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [isRunning, isUntimed, secondsRemaining, initialMinutes, onTimeUp, onTick]);

  if (isUntimed) {
    return (
      <div className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-mono text-sm font-semibold border border-slate-200 dark:border-slate-700">
        <Infinity size={16} className="text-indigo-500" />
        <span>Không giới hạn</span>
      </div>
    );
  }

  const minutes = Math.floor(secondsRemaining / 60);
  const seconds = secondsRemaining % 60;
  const isWarning = secondsRemaining <= 300; // < 5 minutes
  const isCritical = secondsRemaining <= 60; // < 1 minute

  return (
    <div
      className={`flex items-center gap-2 px-3.5 py-1.5 rounded-xl font-mono text-sm font-bold border transition-colors ${
        isCritical
          ? 'bg-rose-50 text-rose-600 border-rose-300 dark:bg-rose-950/70 dark:text-rose-400 dark:border-rose-800 animate-pulse'
          : isWarning
          ? 'bg-amber-50 text-amber-700 border-amber-300 dark:bg-amber-950/60 dark:text-amber-400 dark:border-amber-800'
          : 'bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-200 border-slate-200 dark:border-slate-700 shadow-sm'
      }`}
    >
      {isWarning ? (
        <AlertTriangle size={16} className="text-amber-500" />
      ) : (
        <Clock size={16} className="text-indigo-500" />
      )}
      <span>
        {String(minutes).padStart(2, '0')}:{String(seconds).padStart(2, '0')}
      </span>
      {isWarning && (
        <span className="hidden sm:inline text-[11px] font-sans font-medium text-amber-600 dark:text-amber-400">
          (Sắp hết giờ!)
        </span>
      )}
    </div>
  );
}
