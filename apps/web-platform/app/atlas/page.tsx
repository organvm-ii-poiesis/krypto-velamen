'use client'

import React from 'react'
import AtlasVis from '@/components/AtlasVis'

export default function AtlasPage() {
  return (
    <div className="w-full max-w-6xl p-8">
      <header className="mb-12 border-b border-green-900 pb-4">
        <h1 className="text-3xl font-bold">// THE_ATLAS</h1>
        <p className="text-sm opacity-70 mt-2">Constellation view of the living archive.</p>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <AtlasVis />
        </div>
        
        <aside className="space-y-6">
          <div className="border border-green-800 p-6 bg-black/50">
            <h3 className="font-bold mb-4 uppercase text-xs tracking-widest">Pathfinding</h3>
            <div className="space-y-2">
              <div className="flex justify-between text-xs opacity-70">
                <span>START:</span>
                <span className="text-green-500">Stonewall</span>
              </div>
              <div className="flex justify-between text-xs opacity-70">
                <span>END:</span>
                <span className="text-magenta-500">VRChat</span>
              </div>
              <button className="w-full mt-4 py-1 border border-green-700 text-[10px] hover:bg-green-900">
                CALCULATE ROUTE
              </button>
            </div>
          </div>
          
          <div className="border border-green-800 p-6">
            <h3 className="font-bold mb-4 uppercase text-xs tracking-widest">Active Nodes</h3>
            <ul className="text-xs space-y-1 opacity-60">
              <li>• Rimbaud (Cluster A)</li>
              <li>• Porpentine (Cluster F)</li>
              <li>• The Glitch (Mechanism)</li>
            </ul>
          </div>

          <div className="border border-green-800 p-6 bg-green-900/5">
            <h3 className="font-bold mb-4 uppercase text-xs tracking-widest text-green-400">Particle Cloud</h3>
            <div className="flex flex-wrap gap-2">
              <span className="text-xs px-1 border border-green-900 opacity-80">bright</span>
              <span className="text-[10px] px-1 border border-green-900 opacity-40">shredder</span>
              <span className="text-sm px-1 border border-green-900 text-white">desire</span>
              <span className="text-xs px-1 border border-green-900 opacity-60">terminal</span>
              <span className="text-[10px] px-1 border border-green-900 opacity-30">static</span>
            </div>
          </div>
        </aside>
      </div>
    </div>
  )
}
