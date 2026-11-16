import React, { useState, useEffect } from 'react';
import Prism from 'prismjs';
import 'prismjs/components/prism-java';
import { Copy, Check, Terminal } from 'lucide-react';

export default function CodeBlock({ code, language = 'java', title }) {
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    Prism.highlightAll();
  }, [code]);

  if (!code) return null;

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy code: ', err);
    }
  };

  const lines = code.trim().split('\n');

  return (
    <div className="my-4 rounded-xl overflow-hidden border border-slate-700/60 bg-slate-900 shadow-md">
      {/* Code Header Bar */}
      <div className="flex items-center justify-between px-4 py-2 bg-slate-800/80 border-b border-slate-700/50 text-xs text-slate-400 select-none">
        <div className="flex items-center gap-2">
          <Terminal size={14} className="text-indigo-400" />
          <span className="font-mono font-medium text-slate-300">
            {title || 'Java Code'}
          </span>
          <span className="px-1.5 py-0.5 rounded text-[10px] bg-slate-700 text-indigo-300 font-mono">
            {language}
          </span>
        </div>
        <button
          onClick={handleCopy}
          className="flex items-center gap-1.5 px-2.5 py-1 rounded bg-slate-700/70 hover:bg-slate-700 text-slate-200 transition-colors text-xs font-medium cursor-pointer"
          title="Sao chép mã nguồn"
        >
          {copied ? (
            <>
              <Check size={13} className="text-emerald-400" />
              <span className="text-emerald-300">Đã chép!</span>
            </>
          ) : (
            <>
              <Copy size={13} />
              <span>Sao chép</span>
            </>
          )}
        </button>
      </div>

      {/* Code Body with Line Numbers */}
      <div className="p-3 overflow-x-auto text-sm font-mono flex gap-4">
        <div className="select-none text-slate-500 text-right font-mono pr-2 border-r border-slate-800/70 text-xs leading-6">
          {lines.map((_, i) => (
            <div key={i}>{i + 1}</div>
          ))}
        </div>
        <div className="flex-1 overflow-x-auto">
          <pre className="!bg-transparent !p-0 !m-0 !font-mono text-xs md:text-sm leading-6">
            <code className={`language-${language}`}>
              {code}
            </code>
          </pre>
        </div>
      </div>
    </div>
  );
}
