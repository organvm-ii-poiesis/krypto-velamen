'use client'

import React from 'react'

interface Fragment {
  id: string
  slug: string
  mode: 'concealment' | 'visibility'
  date: string
}

export default function ArchiveGrid({ fragments }: { fragments: Fragment[] }) {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 w-full">
      {fragments.map((frag) => (
        <div 
          key={frag.id} 
          className={`border p-4 transition-all cursor-pointer hover:scale-105 ${
            frag.mode === 'visibility' 
              ? 'border-magenta-500 bg-magenta-900/10' 
              : 'border-green-800 bg-green-900/5'
          }`}
        >
          <div className="text-[10px] opacity-50 mb-2">{frag.date}</div>
          <h3 className="font-bold text-lg uppercase tracking-widest">{frag.slug}</h3>
          <div className="mt-4 flex justify-between items-center">
            <span className="text-[10px] uppercase border px-1 border-current opacity-70">
              {frag.mode}
            </span>
            <span className="text-xl">→</span>
          </div>
        </div>
      ))}
    </div>
  )
}
