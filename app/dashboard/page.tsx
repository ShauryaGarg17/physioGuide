"use client"

import { useState, useEffect } from "react"
import Image from "next/image"
import Link from "next/link"
import { useAuthContext } from "../../context/AuthContext"
import { useRouter } from "next/navigation"
import { db } from "../../lib/firebase"
import { collection, query, where, getDocs } from "firebase/firestore"

const muscleGroups = ["Chest", "Back", "Legs", "Arms", "Shoulders", "Core"]

export default function Dashboard() {
  const [selectedMuscleGroup, setSelectedMuscleGroup] = useState("")
  const [recentActivities, setRecentActivities] = useState([])
  const { user, signOutUser } = useAuthContext()
  const router = useRouter()

  useEffect(() => {
    if (!user) {
      router.push("/")
    } else {
      fetchRecentActivities()
    }
  }, [user, router])

  const fetchRecentActivities = async () => {
    if (!user) return

    const activitiesRef = collection(db, "activities")
    const q = query(
      activitiesRef,
      where("userId", "==", user.uid),
      where("timestamp", ">=", new Date(Date.now() - 7 * 24 * 60 * 60 * 1000)),
    )

    const querySnapshot = await getDocs(q)
    const activities = querySnapshot.docs.map((doc) => ({ id: doc.id, ...doc.data() }))
    setRecentActivities(activities)
  }

  const handleSignOut = async () => {
    await signOutUser()
    router.push("/")
  }

  if (!user) {
    return null // or a loading spinner
  }

  return (
    <div className="min-h-screen flex flex-col">
      <header className="bg-white shadow-md">
        <div className="container mx-auto px-4 py-6 flex justify-between items-center">
          <Image src="/logo.svg" alt="PhysioGuide Logo" width={150} height={50} />
          <nav>
            <Link href="/profile" className="text-black hover:text-gray-600 transition-colors mr-4">
              Profile
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

      <main className="flex-grow container mx-auto px-4 py-12 flex">
        <aside className="w-1/4 pr-8">
          <h2 className="text-2xl font-bold mb-4">Muscle Groups</h2>
          <ul>
            {muscleGroups.map((group) => (
              <li key={group} className="mb-2">
                <button
                  onClick={() => setSelectedMuscleGroup(group)}
                  className={`w-full text-left px-4 py-2 rounded-md transition-colors ${
                    selectedMuscleGroup === group ? "bg-black text-white" : "hover:bg-gray-100"
                  }`}
                >
                  {group}
                </button>
              </li>
            ))}
          </ul>
        </aside>

        <div className="w-3/4">
          <h1 className="text-3xl font-bold mb-6">Dashboard</h1>

          <section className="mb-8">
            <h2 className="text-2xl font-bold mb-4">Your Progress</h2>
            <div className="bg-gray-100 p-4 rounded-md">
              {/* Placeholder for progress bar */}
              <div className="h-8 bg-gray-200 rounded-full overflow-hidden">
                <div className="h-full bg-black" style={{ width: "60%" }}></div>
              </div>
            </div>
          </section>

          <section>
            <h2 className="text-2xl font-bold mb-4">Recent Activities</h2>
            <div className="space-y-4">
              {recentActivities.map((activity) => (
                <div key={activity.id} className="bg-gray-100 p-4 rounded-md">
                  <h3 className="font-semibold">{activity.exerciseName}</h3>
                  <p>Date: {new Date(activity.timestamp.seconds * 1000).toLocaleDateString()}</p>
                  <p>Duration: {activity.duration} minutes</p>
                </div>
              ))}
            </div>
          </section>
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

