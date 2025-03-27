"use client"

import Image from "next/image"
import { useRouter } from "next/navigation"
import { useEffect } from "react"

export default function Home() {
  const router = useRouter()

  const handleGetStarted = async () => {
    console.log("Get Started button clicked")
    router.push("/dashboard") // Directly redirect to dashboard
  }

  return (
    <div className="min-h-screen flex flex-col bg-gray-50 overflow-y-auto">
      <main className="flex-grow container mx-auto px-4 py-12 flex flex-col items-center justify-center text-center">
        <h1 className="text-5xl font-extrabold mb-6 text-gray-800">Welcome to FitnessOne</h1>
        <p className="text-xl mb-8 max-w-2xl text-gray-600">
          Your personal guide to better physical health. Get started with personalized physiotherapy exercises and track
          your progress.
        </p>
        <button
          onClick={handleGetStarted}
          className="bg-blue-600 text-white px-8 py-3 rounded-full text-lg font-semibold hover:bg-blue-700 transition-colors mb-12"
        >
          Get Started
        </button>
        <section className="bg-white shadow-md rounded-lg p-8 mb-12 w-full max-w-4xl">
          <h2 className="text-3xl font-bold mb-4 text-gray-800">About FitnessOne</h2>
          <p className="text-lg text-gray-600 mb-4">
            PhysioGuide is designed to help you achieve better physical health through personalized physiotherapy exercises.
            Our platform offers a variety of exercises tailored to your specific needs and tracks your progress over time.
          </p>
          <p className="text-lg text-gray-600 mb-4">
            Whether you are recovering from an injury or looking to improve your overall fitness, PhysioGuide provides the
            tools and guidance you need to succeed. Join us today and take the first step towards a healthier you.
          </p>
        </section>
        <section className="bg-white shadow-md rounded-lg p-8 mb-12 w-full max-w-4xl">
          <h2 className="text-3xl font-bold mb-4 text-gray-800">Features</h2>
          <ul className="list-disc list-inside text-lg text-gray-600">
            <li>Personalized physiotherapy exercises</li>
            <li>Progress tracking and analytics</li>
            <li>Expert guidance and support</li>
            <li>Easy-to-follow video tutorials</li>
            <li>Community support and motivation</li>
          </ul>
        </section>
      </main>

      <footer className="bg-gray-800 text-white py-6">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2023 PhysioGuide. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

