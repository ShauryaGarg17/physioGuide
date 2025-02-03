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
    <div className="min-h-screen flex flex-col">
      <header className="bg-white shadow-md">
        <div className="container mx-auto px-4 py-6 flex justify-between items-center">
          <Image src="/logo.svg" alt="PhysioGuide Logo" width={150} height={50} />
          <nav>
            <Link href="/dashboard" className="text-black hover:text-gray-600 transition-colors mr-4">
              Dashboard
            </Link>
            <button
              onClick={handleSignOut}
              className="bg-black text-white px-4 py-2 rounded-md hover:bg-gray-800 transition-colors"
            >
              Sign Out
            </button>
          </nav>
        </div>
      </header>

      <main className="flex-grow container mx-auto px-4 py-12">
        <h1 className="text-3xl font-bold mb-6">Profile</h1>
        <form onSubmit={handleSubmit} className="max-w-2xl mx-auto">
          <div className="mb-4">
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
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-black focus:ring-black"
            />
          </div>
          <div className="mb-4">
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
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-black focus:ring-black"
            />
          </div>
          <div className="mb-4">
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
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-black focus:ring-black"
            />
          </div>
          <div className="mb-4">
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
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-black focus:ring-black"
            />
          </div>
          <div className="mb-4">
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
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-black focus:ring-black"
            />
          </div>
          <div className="mb-4">
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
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-black focus:ring-black"
            />
          </div>
          <div className="mb-4">
            <label htmlFor="medicalHistory" className="block text-sm font-medium text-gray-700">
              Medical History
            </label>
            <textarea
              id="medicalHistory"
              name="medicalHistory"
              value={formData.medicalHistory}
              onChange={handleChange}
              rows={4}
              className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-black focus:ring-black"
            ></textarea>
          </div>
          <div className="mt-6">
            <button
              type="submit"
              className="w-full bg-black text-white px-4 py-2 rounded-md hover:bg-gray-800 transition-colors"
            >
              Update Profile
            </button>
          </div>
        </form>

        <section className="mt-12">
          <h2 className="text-2xl font-bold mb-4">Previous Activities</h2>
          <div className="space-y-4">
            {/* Placeholder for previous activities */}
            {[1, 2, 3].map((i) => (
              <div key={i} className="bg-gray-100 p-4 rounded-md">
                <h3 className="font-semibold">Activity {i}</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              </div>
            ))}
          </div>
        </section>
      </main>

      <footer className="bg-black text-white py-6">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2023 PhysioGuide. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

