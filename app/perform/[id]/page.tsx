"use client"

import { useState, useEffect } from "react"
import { useRouter } from "next/navigation"
import Image from "next/image"

export default function Perform({ params }: { params: { id: string } }) {
  const router = useRouter()
  const [count, setCount] = useState(0)
  const [time, setTime] = useState(0)
  const [isPaused, setIsPaused] = useState(false)

  useEffect(() => {
    let interval: NodeJS.Timeout
    if (!isPaused) {
      interval = setInterval(() => {
        setTime((prevTime) => prevTime + 1)
      }, 1000)
    }
    return () => clearInterval(interval)
  }, [isPaused])

  const handlePause = () => {
    setIsPaused(!isPaused)
  }

  const handleEndExercise = () => {
    router.push(`/report/${params.id}`)
  }

  return (
    <div className="min-h-screen flex flex-col">
      <header className="bg-white shadow-md">
        <div className="container mx-auto px-4 py-6">
          <Image src="/logo.svg" alt="PhysioGuide Logo" width={150} height={50} />
        </div>
      </header>

      <main className="flex-grow container mx-auto px-4 py-12 flex">
        <div className="w-1/4 pr-8">
          <h2 className="text-2xl font-bold mb-4">Exercise Data</h2>
          <div className="space-y-4">
            <div>
              <p className="font-semibold">Count</p>
              <p className="text-3xl">{count}</p>
            </div>
            <div>
              <p className="font-semibold">Time Elapsed</p>
              <p className="text-3xl">
                {Math.floor(time / 60)}:{(time % 60).toString().padStart(2, "0")}
              </p>
            </div>
            <div>
              <p className="font-semibold">Progress</p>
              <div className="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
                <div className="bg-black h-2.5 rounded-full" style={{ width: "45%" }}></div>
              </div>
            </div>
          </div>
        </div>

        <div className="w-3/4">
          <h1 className="text-3xl font-bold mb-6">Performing Exercise: {params.id}</h1>

          <div className="aspect-w-16 aspect-h-9 mb-8">
            {/* Placeholder for exercise video/AI analysis */}
            <div className="bg-gray-200 flex items-center justify-center">
              <p className="text-gray-500">Exercise Video / AI Analysis Placeholder</p>
            </div>
          </div>

          <div className="flex space-x-4">
            <button
              onClick={handlePause}
              className="bg-gray-200 text-black px-8 py-3 rounded-full text-lg font-semibold hover:bg-gray-300 transition-colors"
            >
              {isPaused ? "Resume" : "Pause"}
            </button>
            <button
              onClick={handleEndExercise}
              className="bg-black text-white px-8 py-3 rounded-full text-lg font-semibold hover:bg-gray-800 transition-colors"
            >
              End Exercise
            </button>
          </div>
        </div>
      </main>

      <footer className="bg-black text-white py-6">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2023 PhysioGuide. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

