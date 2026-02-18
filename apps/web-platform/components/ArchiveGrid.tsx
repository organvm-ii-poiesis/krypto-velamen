'use client'

import React from 'react'

import { Film, Music, Type, Eye, Terminal } from 'lucide-react'

interface Fragment {
  id: string
  slug: string
  version: number
  mode: 'concealment' | 'visibility'
  triforce_polarity: 'conscious' | 'subconscious' | 'temporal'
  media_type: 'text' | 'film' | 'audio' | 'visual' | 'interactive'
  date: string
  decay_level?: number
}

const MediaIcon = ({ type }: { type: Fragment['media_type'] }) => {
  switch (type) {
    case 'film': return <Film size={14} className="text-yellow-500" />
    case 'audio': return <Music size={14} className="text-blue-500" />
    case 'visual': return <Eye size={14} className="text-magenta-500" />
    case 'interactive': return <Terminal size={14} className="text-cyan-500" />
    default: return <Type size={14} className="opacity-50" />
  }
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
            <div className="flex items-center gap-2">
              <MediaIcon type={frag.media_type} />
              <div className="text-[10px] opacity-50">{frag.date}</div>
            </div>
            <div className="text-[10px] bg-green-900 px-1 text-green-400">v{frag.version}</div>
          </div>
          
          <div className="text-[8px] uppercase tracking-tighter mb-1 font-bold text-blue-400">
            {frag.triforce_polarity}
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
