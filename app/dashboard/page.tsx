"use client"

import { useState, useEffect } from "react"
import Image from "next/image"
import Link from "next/link"
import { useRouter } from "next/navigation"
import { db } from "../../lib/firebase"
import { collection, query, where, getDocs } from "firebase/firestore"

const muscleGroups = ["Squats", "Arm Raises", "Lunges", "Pushups"]

export default function Dashboard() {
  const [selectedMuscleGroup, setSelectedMuscleGroup] = useState("")
  const [recentActivities, setRecentActivities] = useState([])
  const router = useRouter()

  useEffect(() => {
    fetchRecentActivities()
  }, [])

  const fetchRecentActivities = async () => {
    console.log("Fetching recent activities")
    const activitiesRef = collection(db, "activities")
    const q = query(
      activitiesRef,
      where("timestamp", ">=", new Date(Date.now() - 7 * 24 * 60 * 60 * 1000)),
    )

    const querySnapshot = await getDocs(q)
    const activities = querySnapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() }))
    setRecentActivities(activities)
  }

  const handleMuscleGroupClick = (group) => {
    setSelectedMuscleGroup(group)
    if (group === "Chest" || group === "Squats") {
      router.push("/exercise/page")
    }
  }

  return (
    <div className="min-h-screen flex flex-col bg-gray-50 overflow-y-auto">
      <header className="bg-white shadow-md">
        <div className="container mx-auto px-4 py-6 flex justify-between items-center">
          <nav>
            <Link href="/profile" className="text-black hover:text-gray-600 transition-colors mr-4">
              Profile
            </Link>
          </nav>
        </div>
      </header>

      <main className="flex-grow container mx-auto px-4 py-12 flex">
        <aside className="w-1/4 pr-8">
          <h2 className="text-2xl font-bold mb-4 text-gray-800">Exercises</h2>ty
          <ul>
            {muscleGroups.map((group) => (
              <li key={group} className="mb-2">
                <button
                  onClick={() => handleMuscleGroupClick(group)}
                  className={`w-full text-left px-4 py-2 rounded-md transition-colors duration-300 ease-in-out ${
                    selectedMuscleGroup === group ? "bg-blue-600 text-white" : "hover:bg-gray-100"
                  }`}
                >
                  {group}
                </button>
              </li>
            ))}
          </ul>
        </aside>

        <div className="w-3/4">
          <h1 className="text-4xl font-extrabold mb-6 text-gray-800">Dashboard</h1>

          <section className="mb-8">
            <h2 className="text-3xl font-bold mb-4 text-gray-800">Your Progress</h2>
            <div className="bg-gray-100 p-4 rounded-md shadow-md">
              {/* Placeholder for progress bar */}
              <div className="h-8 bg-gray-200 rounded-full overflow-hidden">
                <div className="h-full bg-blue-600 transition-all duration-500 ease-in-out" style={{ width: "60%" }}></div>
              </div>
            </div>
          </section>

          <section>
            <h2 className="text-3xl font-bold mb-4 text-gray-800">Recent Activities</h2>
            <div className="space-y-4">
              {recentActivities.map((activity) => (
                <div key={activity.id} className="bg-white p-4 rounded-md shadow-md transition-transform transform hover:scale-105 duration-300 ease-in-out">
                  <h3 className="font-semibold text-gray-800">{activity.exerciseName}</h3>
                  <p className="text-gray-600">Date: {new Date(activity.timestamp.seconds * 1000).toLocaleDateString()}</p>
                  <p className="text-gray-600">Duration: {activity.duration} minutes</p>
                </div>
              ))}
            </div>
          </section>
        </div>
      </main>

      <footer className="bg-gray-800 text-white py-6">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; 2023 PhysioGuide. All rights reserved.</p>
        </div>
      </footer>
    </div>
  )
}

