import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'KRYPTO-VELAMEN Instrument',
  description: 'A Living Cultural Operating System',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="bg-black text-green-500 font-mono antialiased">
        <main className="min-h-screen flex flex-col items-center">
          {children}
        </main>
      </body>
    </html>
  )
}
