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
    <div className="min-h-screen flex flex-col bg-gray-50">
      <header className="bg-white shadow-md">
        <div className="container mx-auto px-4 py-6 flex justify-between items-center">
          <Image src="/logo.svg" alt="PhysioGuide Logo" width={150} height={50} />
          <Link href="/dashboard" className="text-black hover:text-gray-600 transition-colors">
            Back to Dashboard
          </Link>
        </div>
      </header>

      <main className="flex-grow container mx-auto px-4 py-12">
        <h1 className="text-4xl font-extrabold mb-6 text-gray-800">Exercise: {params.id}</h1>

        <div className="mb-8">
          <div className="aspect-w-16 aspect-h-9 mb-4">
            <iframe
              width="864"
              height="486"
              src="https://www.youtube.com/embed/xvFZjo5PgG0"
              title="Rick Roll (Different link + no ads)"
              frameBorder="0"
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
              referrerPolicy="strict-origin-when-cross-origin"
              allowFullScreen
              className="rounded-md shadow-md"
            ></iframe>
          </div>
          <button
            onClick={() => setIsPlaying(!isPlaying)}
            className="bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-colors"
          >
            {isPlaying ? "Pause" : "Play"}
          </button>
        </div>

        <div className="mb-8">
          <h2 className="text-3xl font-bold mb-2 text-gray-800">Exercise Details</h2>
          <p className="mb-2 text-gray-600">
            <strong>Muscle Group:</strong> Chest
          </p>
          <p className="mb-4 text-gray-600">This exercise helps improve chest strength and muscle definition.</p>
        </div>

        <button
          onClick={handleStartExercise}
          className="bg-blue-600 text-white px-8 py-3 rounded-full text-lg font-semibold hover:bg-blue-700 transition-colors"
        >
          Start Exercise
        </button>
      </main>

      <footer className="bg-gray-800 text-white py-6">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2023 PhysioGuide. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

