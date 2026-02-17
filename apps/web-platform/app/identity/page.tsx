'use client'

import React, { useState } from 'react'

export default function IdentityPage() {
  const [surveillance, setSurveillance] = useState(3)

  return (
    <div className="w-full max-w-4xl p-8">
      <header className="mb-12 border-b border-green-900 pb-4">
        <h1 className="text-3xl font-bold">// THE_MASK</h1>
        <p className="text-sm opacity-70 mt-2">Manage your archival presence and privacy calibration.</p>
      </header>

      <div className="space-y-12">
        <section className="border border-green-800 p-6 bg-black/50">
          <h2 className="text-xl font-bold mb-6 uppercase tracking-widest">Profile Configuration</h2>
          <div className="space-y-4">
            <div>
              <label className="block text-xs uppercase opacity-50 mb-1">Active Handle</label>
              <input 
                type="text" 
                disabled 
                value="ANONYMOUS_OPERATOR" 
                className="w-full bg-green-900/20 border border-green-800 p-2 text-green-500"
              />
            </div>
            <div>
              <label className="block text-xs uppercase opacity-50 mb-1">Surveillance Pressure (1-5)</label>
              <input 
                type="range" 
                min="1" 
                max="5" 
                value={surveillance} 
                onChange={(e) => setSurveillance(parseInt(e.target.value))}
                className="w-full accent-green-500"
              />
              <div className="flex justify-between text-[10px] mt-1">
                <span>1: MINIMAL</span>
                <span>5: TOTALITARIAN</span>
              </div>
            </div>
          </div>
        </section>

        <section className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="border border-green-800 p-6">
            <h3 className="font-bold mb-4">// PUBLIC_VISIBILITY</h3>
            <div className="flex items-center gap-4">
              <div className="w-12 h-6 bg-green-900 rounded-full relative">
                <div className="absolute right-1 top-1 w-4 h-4 bg-green-500 rounded-full"></div>
              </div>
              <span className="text-sm">ENABLED</span>
            </div>
          </div>
          <div className="border border-green-800 p-6">
            <h3 className="font-bold mb-4">// ENCRYPTION_MODE</h3>
            <span className="text-sm bg-green-900 px-2 py-1">AES-256-GCM</span>
          </div>
        </section>
      </div>
    </div>
  )
}
