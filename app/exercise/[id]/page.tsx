"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import Image from "next/image"
import Link from "next/link"

export default function Exercise({ params }: { params: { id: string } }) {
  const router = useRouter()
  const [isPlaying, setIsPlaying] = useState(false)

  const handleStartExercise = () => {
    router.push(`/perform/${params.id}`)
  }

  return (
    <div className="min-h-screen flex flex-col">
      <header className="bg-white shadow-md">
        <div className="container mx-auto px-4 py-6 flex justify-between items-center">
          <Image src="/logo.svg" alt="PhysioGuide Logo" width={150} height={50} />
          <Link href="/dashboard" className="text-black hover:text-gray-600 transition-colors">
            Back to Dashboard
          </Link>
        </div>
      </header>

      <main className="flex-grow container mx-auto px-4 py-12">
        <h1 className="text-3xl font-bold mb-6">Exercise: {params.id}</h1>

        <div className="mb-8">
          <div className="aspect-w-16 aspect-h-9 mb-4">
            {/* Placeholder for YouTube embed */}
            <div className="bg-gray-200 flex items-center justify-center">
              <p className="text-gray-500">YouTube Video Placeholder</p>
            </div>
          </div>
          <button
            onClick={() => setIsPlaying(!isPlaying)}
            className="bg-black text-white px-4 py-2 rounded-md hover:bg-gray-800 transition-colors"
          >
            {isPlaying ? "Pause" : "Play"}
          </button>
        </div>

        <div className="mb-8">
          <h2 className="text-2xl font-bold mb-2">Exercise Details</h2>
          <p className="mb-2">
            <strong>Muscle Group:</strong> Chest
          </p>
          <p className="mb-4">This exercise helps improve chest strength and muscle definition.</p>
        </div>

        <button
          onClick={handleStartExercise}
          className="bg-black text-white px-8 py-3 rounded-full text-lg font-semibold hover:bg-gray-800 transition-colors"
        >
          Start Exercise
        </button>
      </main>

      <footer className="bg-black text-white py-6">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2023 PhysioGuide. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

