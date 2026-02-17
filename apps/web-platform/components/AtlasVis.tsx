'use client'

import React from 'react'

export default function AtlasVis() {
  return (
    <div className="w-full h-96 bg-black border border-green-800 relative overflow-hidden group">
      <div className="absolute inset-0 bg-[url('/grid.png')] opacity-20"></div>
      <div className="absolute inset-0 flex items-center justify-center">
        <div className="text-center">
          <h3 className="text-2xl font-bold glitch-text mb-2">THE ATLAS</h3>
          <p className="text-xs opacity-60 max-w-md mx-auto">
            [VISUALIZATION OFFLINE]
            <br/>
            Neural link required for deep dive.
            <br/>
            Processing 150+ entities...
          </p>
        </div>
      </div>
      
      {/* Mock Nodes */}
      <div className="absolute top-1/4 left-1/4 w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
      <div className="absolute bottom-1/3 right-1/3 w-3 h-3 bg-magenta-500 rounded-full animate-pulse delay-75"></div>
      <div className="absolute top-1/2 right-1/4 w-1 h-1 bg-white rounded-full"></div>
      
      {/* Interactive overlay */}
      <div className="absolute inset-0 bg-green-500/5 opacity-0 group-hover:opacity-100 transition-opacity flex items-end justify-between p-4 cursor-crosshair">
        <span className="text-[10px]">ZOOM: 100%</span>
        <span className="text-[10px]">TARGET: RIMBAUD</span>
      </div>
    </div>
  )
}
