"use client"

import { useRouter } from "next/navigation"
import Image from "next/image"
import Link from "next/link"

export default function Report({ params }: { params: { id: string } }) {
  const router = useRouter()

  // Placeholder data - in a real app, this would come from Firebase
  const reportData = {
    exerciseName: "Chest Press",
    accuracy: 85,
    timeElapsed: 300, // 5 minutes
    totalCount: 30,
    pauses: 2,
  }

  const getMessage = (accuracy: number) => {
    if (accuracy >= 90) return "Excellent job! Keep up the great work!"
    if (accuracy >= 70) return "Great effort! There's still room for improvement."
    return "Good start! Keep practicing to improve your form."
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
        <h1 className="text-3xl font-bold mb-6">Exercise Report: {reportData.exerciseName}</h1>

        <div className="bg-gray-100 p-6 rounded-lg shadow-md mb-8">
          <h2 className="text-2xl font-bold mb-4">Performance Summary</h2>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <p className="font-semibold">Accuracy</p>
              <p className="text-3xl">{reportData.accuracy}%</p>
            </div>
            <div>
              <p className="font-semibold">Time Elapsed</p>
              <p className="text-3xl">
                {Math.floor(reportData.timeElapsed / 60)}:{(reportData.timeElapsed % 60).toString().padStart(2, "0")}
              </p>
            </div>
            <div>
              <p className="font-semibold">Total Count</p>
              <p className="text-3xl">{reportData.totalCount}</p>
            </div>
            <div>
              <p className="font-semibold">Number of Pauses</p>
              <p className="text-3xl">{reportData.pauses}</p>
            </div>
          </div>
        </div>

        <div className="bg-black text-white p-6 rounded-lg shadow-md mb-8">
          <h2 className="text-2xl font-bold mb-2">Feedback</h2>
          <p>{getMessage(reportData.accuracy)}</p>
        </div>

        <Link
          href="/dashboard"
          className="bg-black text-white px-8 py-3 rounded-full text-lg font-semibold hover:bg-gray-800 transition-colors inline-block"
        >
          Return to Dashboard
        </Link>
      </main>

      <footer className="bg-black text-white py-6">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2023 PhysioGuide. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

