"use client"

import Image from "next/image"
import { useAuthContext } from "../context/AuthContext"
import { useRouter } from "next/navigation"
import { useEffect } from "react"

export default function Home() {
  const { user, signIn } = useAuthContext()
  const router = useRouter()

  useEffect(() => {
    if (user) {
      router.push("/dashboard")
    }
  }, [user, router])

  const handleGetStarted = async () => {
    await signIn()
  }

  return (
    <div className="min-h-screen flex flex-col">
      <header className="bg-white shadow-md">
        <div className="container mx-auto px-4 py-6 flex justify-between items-center">
          <Image src="/logo.svg" alt="PhysioGuide Logo" width={150} height={50} />
          <nav>
            {!user && (
              <button onClick={signIn} className="text-black hover:text-gray-600 transition-colors">
                Login
              </button>
            )}
          </nav>
        </div>
      </header>

      <main className="flex-grow container mx-auto px-4 py-12 flex flex-col items-center justify-center text-center">
        <h1 className="text-4xl font-bold mb-6">Welcome to PhysioGuide</h1>
        <p className="text-xl mb-8 max-w-2xl">
          Your personal guide to better physical health. Get started with personalized physiotherapy exercises and track
          your progress.
        </p>
        <button
          onClick={handleGetStarted}
          className="bg-black text-white px-8 py-3 rounded-full text-lg font-semibold hover:bg-gray-800 transition-colors"
        >
          Get Started
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

