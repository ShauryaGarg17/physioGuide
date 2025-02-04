"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import Image from "next/image"
import Link from "next/link"

export default function Profile() {
  const router = useRouter()
  const [formData, setFormData] = useState({
    fullName: "John Doe",
    dateOfBirth: "1990-01-01",
    gender: "Male",
    height: "180",
    weight: "75",
    phoneNumber: "1234567890",
    medicalHistory: "No significant medical history",
  })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setFormData((prevState) => ({ ...prevState, [name]: value }))
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // TODO: Update data in Firebase
    console.log(formData)
    // Show success message or redirect
  }

  const handleSignOut = () => {
    // TODO: Implement sign out functionality
    router.push("/")
  }

  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <header className="bg-white shadow-md rounded-b-lg">
        <div className="container mx-auto px-4 py-6 flex justify-between items-center">
          <Image src="/logo.svg" alt="PhysioGuide Logo" width={150} height={50} />
          <nav>
            <Link href="/dashboard" className="text-gray-800 hover:text-gray-600 transition-colors mr-4">
              Dashboard
            </Link>
            <button
              onClick={handleSignOut}
              className="bg-gray-800 text-white px-4 py-2 rounded-full hover:bg-gray-700 transition-colors"
            >
              Sign Out
            </button>
          </nav>
        </div>
      </header>

      <main className="flex-grow container mx-auto px-4 py-12">
        <h1 className="text-4xl font-bold mb-8 text-gray-800">Profile</h1>
        <form onSubmit={handleSubmit} className="max-w-2xl mx-auto bg-white p-8 rounded-lg shadow-lg">
          <div className="mb-6">
            <label htmlFor="fullName" className="block text-sm font-medium text-gray-700">
              Full Name
            </label>
            <input
              type="text"
              id="fullName"
              name="fullName"
              value={formData.fullName}
              onChange={handleChange}
              required
              className="mt-1 block w-full rounded-full border-gray-300 shadow-sm focus:border-gray-800 focus:ring-gray-800"
            />
          </div>
          <div className="mb-6">
            <label htmlFor="dateOfBirth" className="block text-sm font-medium text-gray-700">
              Date of Birth
            </label>
            <input
              type="date"
              id="dateOfBirth"
              name="dateOfBirth"
              value={formData.dateOfBirth}
              onChange={handleChange}
              required
              className="mt-1 block w-full rounded-full border-gray-300 shadow-sm focus:border-gray-800 focus:ring-gray-800"
            />
          </div>
          <div className="mb-6">
            <label htmlFor="gender" className="block text-sm font-medium text-gray-700">
              Gender
            </label>
            <input
              type="text"
              id="gender"
              name="gender"
              value={formData.gender}
              onChange={handleChange}
              required
              className="mt-1 block w-full rounded-full border-gray-300 shadow-sm focus:border-gray-800 focus:ring-gray-800"
            />
          </div>
          <div className="mb-6">
            <label htmlFor="height" className="block text-sm font-medium text-gray-700">
              Height (cm)
            </label>
            <input
              type="number"
              id="height"
              name="height"
              value={formData.height}
              onChange={handleChange}
              required
              className="mt-1 block w-full rounded-full border-gray-300 shadow-sm focus:border-gray-800 focus:ring-gray-800"
            />
          </div>
          <div className="mb-6">
            <label htmlFor="weight" className="block text-sm font-medium text-gray-700">
              Weight (kg)
            </label>
            <input
              type="number"
              id="weight"
              name="weight"
              value={formData.weight}
              onChange={handleChange}
              required
              className="mt-1 block w-full rounded-full border-gray-300 shadow-sm focus:border-gray-800 focus:ring-gray-800"
            />
          </div>
          <div className="mb-6">
            <label htmlFor="phoneNumber" className="block text-sm font-medium text-gray-700">
              Phone Number
            </label>
            <input
              type="tel"
              id="phoneNumber"
              name="phoneNumber"
              value={formData.phoneNumber}
              onChange={handleChange}
              required
              className="mt-1 block w-full rounded-full border-gray-300 shadow-sm focus:border-gray-800 focus:ring-gray-800"
            />
          </div>
          <div className="mb-6">
            <label htmlFor="medicalHistory" className="block text-sm font-medium text-gray-700">
              Medical History
            </label>
            <textarea
              id="medicalHistory"
              name="medicalHistory"
              value={formData.medicalHistory}
              onChange={handleChange}
              rows={4}
              className="mt-1 block w-full rounded-lg border-gray-300 shadow-sm focus:border-gray-800 focus:ring-gray-800"
            ></textarea>
          </div>
          <div className="mt-8">
            <button
              type="submit"
              className="w-full bg-gray-800 text-white px-4 py-2 rounded-full hover:bg-gray-700 transition-colors"
            >
              Update Profile
            </button>
          </div>
        </form>

        <section className="mt-16">
          <h2 className="text-3xl font-bold mb-6 text-gray-800">Previous Activities</h2>
          <div className="space-y-6">
            {/* Placeholder for previous activities */}
            {[1, 2, 3].map((i) => (
              <div key={i} className="bg-white p-6 rounded-lg shadow-md">
                <h3 className="font-semibold text-gray-800">Activity {i}</h3>
                <p className="text-gray-600">Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </div>
            ))}
          </div>
        </section>
      </main>

      <footer className="bg-gray-800 text-white py-6 rounded-t-lg">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2023 PhysioGuide. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

