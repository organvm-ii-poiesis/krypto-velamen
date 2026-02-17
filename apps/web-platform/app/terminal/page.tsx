'use client'

import React from 'react'
import TerminalInterface from '@/components/TerminalInterface'

export default function TerminalPage() {
  return (
    <div className="w-full max-w-4xl p-8 flex flex-col items-center justify-center min-h-[80vh]">
      <h1 className="sr-only">Terminal Access</h1>
      <div className="w-full">
        <TerminalInterface />
      </div>
      <p className="mt-8 text-xs opacity-40 text-center">
        Press ESC to disconnect.
      </p>
    </div>
  )
}
