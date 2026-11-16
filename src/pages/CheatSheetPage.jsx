import React, { useState } from 'react';
import { 
  FileText, 
  Search, 
  Check, 
  Layers, 
  ShieldCheck, 
  AlertTriangle, 
  Cpu, 
  LayoutGrid, 
  Code2, 
  HelpCircle,
  Copy,
  Sparkles
} from 'lucide-react';
import { CHEAT_SHEETS } from '../data/cheatSheetData';
import CodeBlock from '../components/CodeBlock';

export default function CheatSheetPage() {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('all');

  const categories = ['all', 'Cơ bản Java', 'Exception & I/O', 'Generics', 'Cấu trúc dữ liệu', 'Đa luồng', 'Kiến trúc & Mẫu thiết kế'];

  const filteredSheets = CHEAT_SHEETS.filter(sheet => {
    if (selectedCategory !== 'all' && sheet.category !== selectedCategory) {
      return false;
    }
    if (searchQuery.trim()) {
      const q = searchQuery.toLowerCase();
      return (
        sheet.title.toLowerCase().includes(q) ||
        sheet.description.toLowerCase().includes(q) ||
        sheet.category.toLowerCase().includes(q)
      );
    }
    return true;
  });

  return (
    <div className="space-y-6 pb-12">
      {/* Top Banner */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 bg-white dark:bg-slate-900 p-5 rounded-2xl border border-slate-200/80 dark:border-slate-800 shadow-sm">
        <div>
          <div className="flex items-center gap-2 mb-1">
            <span className="p-1.5 rounded-lg bg-amber-50 dark:bg-amber-950 text-amber-600 dark:text-amber-400">
              <FileText size={18} />
            </span>
            <h1 className="font-extrabold text-xl sm:text-2xl text-slate-800 dark:text-slate-100">
              Java & OOP Cheat Sheet
            </h1>
          </div>
          <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400">
            Tóm tắt các quy tắc cốt lõi, bảng tra cứu nhanh và các góc khuất thường gặp trong đề thi LTNC UET
          </p>
        </div>

        {/* Search input */}
        <div className="relative w-full md:w-72">
          <Search size={16} className="absolute left-3.5 top-1/2 -translate-y-1/2 text-slate-400" />
          <input
            type="text"
            placeholder="Tra cứu nhanh (PECS, volatile, static...)..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-10 pr-4 py-2 rounded-xl border border-slate-200 dark:border-slate-800 bg-white dark:bg-slate-900 text-xs sm:text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
        </div>
      </div>

      {/* Category Pills */}
      <div className="flex items-center gap-2 overflow-x-auto pb-1 scrollbar-none">
        {categories.map((cat) => (
          <button
            key={cat}
            onClick={() => setSelectedCategory(cat)}
            className={`flex-shrink-0 px-3.5 py-1.5 rounded-xl text-xs font-bold transition cursor-pointer ${
              selectedCategory === cat
                ? 'bg-indigo-600 text-white shadow-sm'
                : 'bg-white dark:bg-slate-900 text-slate-600 dark:text-slate-400 border border-slate-200 dark:border-slate-800 hover:border-indigo-300'
            }`}
          >
            {cat === 'all' ? 'Tất cả chủ đề' : cat}
          </button>
        ))}
      </div>

      {/* Cheat Sheet Cards List */}
      <div className="space-y-6">
        {filteredSheets.map((sheet) => (
          <div
            key={sheet.id}
            className="bg-white dark:bg-slate-900 rounded-3xl border border-slate-200/80 dark:border-slate-800 p-6 shadow-sm hover:shadow-md transition-shadow"
          >
            {/* Card Header */}
            <div className="flex flex-wrap items-center justify-between gap-2 mb-4 pb-3 border-b border-slate-100 dark:border-slate-800">
              <div>
                <span className="text-[10px] font-bold uppercase tracking-wider text-indigo-600 dark:text-indigo-400 bg-indigo-50 dark:bg-indigo-950 px-2.5 py-1 rounded-full">
                  {sheet.category}
                </span>
                <h3 className="font-extrabold text-lg sm:text-xl text-slate-800 dark:text-slate-100 mt-1.5">
                  {sheet.title}
                </h3>
              </div>
              <p className="text-xs text-slate-500 dark:text-slate-400">
                {sheet.description}
              </p>
            </div>

            {/* Dynamic Content Rendering based on sheet type */}
            
            {/* 1. TABLE TYPE */}
            {sheet.content.type === 'table' && (
              <div className="space-y-4">
                <div className="overflow-x-auto rounded-xl border border-slate-200 dark:border-slate-800">
                  <table className="w-full text-xs sm:text-sm text-left">
                    <thead className="bg-slate-50 dark:bg-slate-800/80 text-slate-700 dark:text-slate-300 font-bold border-b border-slate-200 dark:border-slate-800">
                      <tr>
                        {sheet.content.headers.map((h, i) => (
                          <th key={i} className="px-4 py-3 whitespace-nowrap">
                            {h}
                          </th>
                        ))}
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-slate-100 dark:divide-slate-800 font-mono text-xs">
                      {sheet.content.rows.map((row, rIdx) => (
                        <tr
                          key={rIdx}
                          className="hover:bg-slate-50/50 dark:hover:bg-slate-800/40 transition-colors"
                        >
                          {row.map((cell, cIdx) => (
                            <td
                              key={cIdx}
                              className={`px-4 py-3 whitespace-nowrap ${
                                cIdx === 0
                                  ? 'font-bold text-indigo-600 dark:text-indigo-400 font-sans'
                                  : 'text-slate-700 dark:text-slate-300'
                              }`}
                            >
                              {cell}
                            </td>
                          ))}
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>

                {sheet.content.notes && (
                  <div className="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-800 text-xs space-y-1.5">
                    <span className="font-bold text-slate-700 dark:text-slate-300 block mb-1">
                      💡 Lưu ý trọng tâm:
                    </span>
                    {sheet.content.notes.map((note, nIdx) => (
                      <p key={nIdx} className="text-slate-600 dark:text-slate-400 leading-relaxed">
                        • {note}
                      </p>
                    ))}
                  </div>
                )}
              </div>
            )}

            {/* 2. EXCEPTION TREE & RULES */}
            {sheet.content.type === 'tree-and-rules' && (
              <div className="space-y-4">
                <div className="p-4 rounded-xl bg-slate-900 border border-slate-800 text-xs font-mono text-emerald-400 overflow-x-auto">
                  <pre className="m-0 leading-5 whitespace-pre">
                    {sheet.content.diagram.trim()}
                  </pre>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                  {sheet.content.rules.map((rule, idx) => (
                    <div
                      key={idx}
                      className="p-4 rounded-xl bg-indigo-50/50 dark:bg-indigo-950/20 border border-indigo-100 dark:border-indigo-900/40"
                    >
                      <h4 className="font-bold text-xs text-indigo-950 dark:text-indigo-200 mb-1">
                        {rule.title}
                      </h4>
                      <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                        {rule.text}
                      </p>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* 3. PECS GUIDE */}
            {sheet.content.type === 'pecs-guide' && (
              <div className="space-y-4">
                <div className="p-3.5 rounded-xl bg-gradient-to-r from-indigo-500/10 via-purple-500/10 to-pink-500/10 border border-indigo-200 dark:border-indigo-800 text-center">
                  <span className="font-extrabold text-sm sm:text-base text-indigo-700 dark:text-indigo-300">
                    ⚡ {sheet.content.mnemonic}
                  </span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {sheet.content.rules.map((rule, idx) => (
                    <div
                      key={idx}
                      className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-800 space-y-3"
                    >
                      <div>
                        <span className="font-mono font-bold text-xs text-indigo-600 dark:text-indigo-400 block">
                          {rule.keyword}
                        </span>
                        <h4 className="font-extrabold text-sm text-slate-800 dark:text-slate-100 mt-0.5">
                          {rule.role}
                        </h4>
                      </div>
                      <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                        {rule.explanation}
                      </p>
                      <CodeBlock code={rule.code} title={rule.role} />
                    </div>
                  ))}
                </div>

                <div className="p-3.5 rounded-xl bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-900/60 text-xs text-amber-800 dark:text-amber-300 font-medium">
                  ⚠️ <strong>Cảnh giác:</strong> {sheet.content.invarianceNotice}
                </div>
              </div>
            )}

            {/* 4. THREAD GUIDE */}
            {sheet.content.type === 'thread-guide' && (
              <div className="space-y-4">
                <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2">
                  {sheet.content.states.map((st, idx) => (
                    <div
                      key={idx}
                      className="p-3 rounded-xl bg-slate-50 dark:bg-slate-800/80 border border-slate-200 dark:border-slate-700 text-center"
                    >
                      <span className="font-mono font-bold text-xs text-indigo-600 dark:text-indigo-400 block mb-1">
                        {st.state}
                      </span>
                      <p className="text-[10px] text-slate-500 dark:text-slate-400 leading-tight">
                        {st.desc}
                      </p>
                    </div>
                  ))}
                </div>

                <div className="p-4 rounded-xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-800 space-y-2 text-xs">
                  <span className="font-bold text-slate-700 dark:text-slate-300 block mb-1">
                    📌 3 Quy tắc vàng trong Đa luồng:
                  </span>
                  {sheet.content.goldenRules.map((r, idx) => (
                    <p key={idx} className="text-slate-600 dark:text-slate-400 leading-relaxed">
                      • {r}
                    </p>
                  ))}
                </div>
              </div>
            )}

            {/* 5. PATTERNS & SOLID */}
            {sheet.content.type === 'patterns-guide' && (
              <div className="space-y-6">
                {/* SOLID list */}
                <div>
                  <h4 className="font-extrabold text-xs uppercase tracking-wider text-slate-400 mb-3">
                    5 Nguyên lý SOLID
                  </h4>
                  <div className="grid grid-cols-1 sm:grid-cols-5 gap-2">
                    {sheet.content.solid.map((s, idx) => (
                      <div
                        key={idx}
                        className="p-3 rounded-xl bg-indigo-50/60 dark:bg-indigo-950/40 border border-indigo-100 dark:border-indigo-900/50"
                      >
                        <div className="w-6 h-6 rounded-md bg-indigo-600 text-white font-black text-xs flex items-center justify-center mb-1.5">
                          {s.letter}
                        </div>
                        <h5 className="font-bold text-xs text-slate-800 dark:text-slate-200 mb-1">
                          {s.name}
                        </h5>
                        <p className="text-[11px] text-slate-500 dark:text-slate-400 leading-tight">
                          {s.desc}
                        </p>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Key Patterns */}
                <div>
                  <h4 className="font-extrabold text-xs uppercase tracking-wider text-slate-400 mb-3">
                    Các mẫu thiết kế hay thi nhất
                  </h4>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    {sheet.content.patterns.map((p, idx) => (
                      <div
                        key={idx}
                        className="p-4 rounded-2xl bg-slate-50 dark:bg-slate-800/60 border border-slate-200/80 dark:border-slate-800 space-y-2"
                      >
                        <div className="flex items-center justify-between">
                          <h5 className="font-extrabold text-sm text-slate-800 dark:text-slate-100">
                            {p.name}
                          </h5>
                          <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-200 dark:bg-slate-700 text-slate-700 dark:text-slate-300">
                            {p.type}
                          </span>
                        </div>
                        <p className="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
                          {p.purpose}
                        </p>
                        {p.code && <CodeBlock code={p.code} title={p.name} />}
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            )}

          </div>
        ))}
      </div>
    </div>
  );
}
