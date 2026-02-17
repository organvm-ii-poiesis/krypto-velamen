'use client'

import React, { useState, useEffect, useRef } from 'react'

export default function TerminalInterface() {
  const [history, setHistory] = useState<string[]>([
    "KRYPTO-VELAMEN KERNEL v3.0",
    "Initializing Field I connection...",
    "Status: ONLINE",
    "Type 'help' for commands."
  ])
  const [input, setInput] = useState("")
  const bottomRef = useRef<HTMLDivElement>(null)

  const handleCommand = (cmd: string) => {
    const newHistory = [...history, `> ${cmd}`]
    
    switch (cmd.toLowerCase()) {
      case "help":
        newHistory.push("COMMANDS: status, dashboard, flip, exit")
        break
      case "status":
        newHistory.push("SYSTEM: STABLE | POLARITY: DUAL")
        break
      case "dashboard":
        newHistory.push("Accessing dashboard... [REDIRECTING]")
        // In a real app, router.push('/dashboard')
        break
      case "flip":
        newHistory.push("Initiating Field Flip... [WARNING: DREAM LOGIC ACTIVE]")
        break
      default:
        newHistory.push(`Unknown command: ${cmd}`)
    }
    
    setHistory(newHistory)
    setInput("")
  }

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" })
  }, [history])

  return (
    <div className="bg-black text-green-500 font-mono p-4 h-96 overflow-y-auto border border-green-800 rounded shadow-lg shadow-green-900/20">
      <div className="space-y-1">
        {history.map((line, i) => (
          <div key={i} className={line.startsWith(">") ? "font-bold text-white" : "opacity-80"}>
            {line}
          </div>
        ))}
        <div ref={bottomRef} />
      </div>
      <div className="mt-4 flex items-center">
        <span className="mr-2 text-green-400">$</span>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleCommand(input)}
          className="bg-transparent border-none outline-none flex-1 text-green-400 focus:ring-0"
          autoFocus
        />
      </div>
    </div>
  )
}
