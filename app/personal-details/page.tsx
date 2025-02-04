"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import Image from "next/image"

export default function PersonalDetails() {
  const router = useRouter()
  const [formData, setFormData] = useState({
    fullName: "",
    dateOfBirth: "",
    gender: "",
    height: "",
    weight: "",
    phoneNumber: "",
    medicalHistory: "",
  })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setFormData((prevState) => ({ ...prevState, [name]: value }))
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // TODO: Store data in Firebase
    console.log(formData)
    router.push("/dashboard")
  }

  return (
    <div className="min-h-screen flex flex-col">
      <header className="bg-white shadow-md">
        <div className="container mx-auto px-4 py-6">
          <Image src="/logo.svg" alt="PhysioGuide Logo" width={150} height={50} />
        </div>
      </header>

      <main className="flex-grow container mx-auto px-4 py-12">
        <h1 className="text-3xl font-bold mb-6">Personal Details</h1>
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
              Submit
            </button>
          </div>
        </form>
      </main>

      <footer className="bg-black text-white py-6">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2023 PhysioGuide. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

