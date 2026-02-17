'use client'

import React from 'react'

export default function CommunityPage() {
  const threads = [
    { id: '1', title: 'The Ethics of Digital Archives', topic: 'Topic 17', messages: 12 },
    { id: '2', title: 'BBS Nostalgia vs Utility', topic: 'Topic 26', messages: 8 },
    { id: '3', title: 'Porpentine and Somatic Encoding', topic: 'Artist Spotlight', messages: 45 },
  ]

  return (
    <div className="w-full max-w-6xl p-8">
      <header className="mb-12 border-b border-green-900 pb-4">
        <h1 className="text-3xl font-bold">// THE_SUBSTRATE</h1>
        <p className="text-sm opacity-70 mt-2">Collaborative journals and threaded community discussions.</p>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-12">
        <div className="lg:col-span-2 space-y-8">
          <section>
            <h2 className="text-xs font-bold mb-6 tracking-[0.3em] text-green-800 uppercase">
              // ACTIVE_THREADS
            </h2>
            <div className="space-y-4">
              {threads.map(t => (
                <div key={t.id} className="border border-green-900 p-4 hover:border-green-500 transition-colors flex justify-between items-center group">
                  <div>
                    <div className="text-[10px] opacity-50 uppercase">{t.topic}</div>
                    <h3 className="font-bold group-hover:text-white transition-colors">{t.title}</h3>
                  </div>
                  <div className="text-right text-xs opacity-50">
                    {t.messages} MESSAGES
                  </div>
                </div>
              ))}
            </div>
          </section>
        </div>

        <aside className="space-y-8">
          <div className="border border-green-800 p-6 bg-green-950/10">
            <h2 className="font-bold mb-4 uppercase tracking-widest text-sm">Your Journal</h2>
            <p className="text-xs opacity-70 mb-6">3 Private Fragments | 1 Public Transmission</p>
            <button className="w-full py-2 bg-green-900 text-black font-bold uppercase text-xs hover:bg-green-500">
              NEW_DRAFT
            </button>
          </div>
          
          <div className="border border-green-800 p-6">
            <h2 className="font-bold mb-4 uppercase tracking-widest text-sm">Direct Messages</h2>
            <div className="text-xs italic opacity-40">No active signals.</div>
          </div>
        </aside>
      </div>
    </div>
  )
}
