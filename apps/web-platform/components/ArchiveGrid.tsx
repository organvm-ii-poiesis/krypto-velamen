'use client'

import React from 'react'

interface Fragment {
  id: string
  slug: string
  version: number
  mode: 'concealment' | 'visibility'
  date: string
  decay_level?: number
}

export default function ArchiveGrid({ fragments }: { fragments: Fragment[] }) {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 w-full">
      {fragments.map((frag) => (
        <div 
          key={frag.id} 
          className={`border p-4 transition-all cursor-pointer group relative overflow-hidden ${
            frag.mode === 'visibility' 
              ? 'border-magenta-500 bg-magenta-900/10' 
              : 'border-green-800 bg-green-900/5'
          }`}
        >
          {/* Decay Overlay */}
          <div 
            className="absolute bottom-0 left-0 h-1 bg-red-600 transition-all duration-1000" 
            style={{ width: `${(frag.decay_level || 0) * 100}%` }}
          />

          <div className="flex justify-between items-center mb-2">
            <div className="text-[10px] opacity-50">{frag.date}</div>
            <div className="text-[10px] bg-green-900 px-1 text-green-400">v{frag.version}</div>
          </div>
          <h3 className="font-bold text-lg uppercase tracking-widest group-hover:text-white transition-colors">
            {frag.decay_level && frag.decay_level > 0.7 ? "[CORRUPTED]" : frag.slug}
          </h3>
          <div className="mt-4 flex justify-between items-center">
            <span className="text-[10px] uppercase border px-1 border-current opacity-70">
              {frag.mode}
            </span>
            <button className="text-[10px] py-1 px-2 border border-green-700 hover:bg-green-500 hover:text-black transition-colors">
              WITNESS
            </button>
          </div>
        </div>
      ))}
    </div>
  )
}
