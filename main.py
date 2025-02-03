import cv2
import numpy as np
from utils.pose import PoseDetector
from utils.angle_calculator import calculate_angle

print("All imports successful!")  # Debug print


class PhysiotherapyAI:
    def __init__(self):
        print("Initializing PhysiotherapyAI...")  # Debug print
        self.detector = PoseDetector()
        self.exercise_counters = {
            'squat': 0,
            'arm_raise': 0
        }
        self.exercise_stages = {
            'squat': None,
            'arm_raise': None
        }
        print("PhysiotherapyAI initialized successfully!")  # Debug print

    def analyze_squat(self, landmarks):
        """Analyze squat form"""
        # Get hip, knee and ankle points
        hip = landmarks[23][:2] if len(landmarks) > 23 else None
        knee = landmarks[25][:2] if len(landmarks) > 25 else None
        ankle = landmarks[27][:2] if len(landmarks) > 27 else None

        if all([hip, knee, ankle]):
            angle = calculate_angle(hip, knee, ankle)
            stage = None  # Initialize stage

            # Check squat form
            if angle > 160:
                stage = "up"
            elif angle < 90:
                stage = "down"
            else:
                stage = "middle"  # Added middle stage

            # Count reps
            if self.exercise_stages['squat'] == "down" and stage == "up":
                self.exercise_counters['squat'] += 1

            self.exercise_stages['squat'] = stage

            return angle, stage
        return None, None

    def analyze_arm_raise(self, landmarks):
        """Analyze arm raise form"""
        # Get shoulder, elbow and wrist points
        shoulder = landmarks[11][:2] if len(landmarks) > 11 else None
        elbow = landmarks[13][:2] if len(landmarks) > 13 else None
        wrist = landmarks[15][:2] if len(landmarks) > 15 else None

        if all([shoulder, elbow, wrist]):
            angle = calculate_angle(shoulder, elbow, wrist)
            stage = None  # Initialize stage

            # Check arm raise form
            if angle > 160:
                stage = "up"
            elif angle < 30:
                stage = "down"
            else:
                stage = "middle"  # Added middle stage

            # Count reps
            if self.exercise_stages['arm_raise'] == "down" and stage == "up":
                self.exercise_counters['arm_raise'] += 1

            self.exercise_stages['arm_raise'] = stage

            return angle, stage
        return None, None

    def process_frame(self, frame, exercise_type='squat'):
        """Process each frame and return feedback"""
        frame = self.detector.find_pose(frame)
        landmarks = self.detector.get_positions(frame)

        feedback = []

        if exercise_type == 'arm_raise':
            angle, stage = self.analyze_arm_raise(landmarks)
            if angle is not None:
                feedback.append(f"Squat angle: {angle:.2f}")
                feedback.append(f"Stage: {stage}")
                feedback.append(f"Count: {self.exercise_counters['squat']}")

                # Form checking
                if stage == "down" and angle > 100:
                    feedback.append("Go lower in your squat")
                elif stage == "down" and angle < 70:
                    feedback.append("You're going too low")

        elif exercise_type == 'squat':
            angle, stage = self.analyze_squat(landmarks)
            if angle is not None:
                feedback.append(f"Arm angle: {angle:.2f}")
                feedback.append(f"Stage: {stage}")
                feedback.append(f"Count: {self.exercise_counters['arm_raise']}")

                # Form checking
                if stage == "up" and angle < 150:
                    feedback.append("Raise your arm higher")

        return frame, feedback


# def main():
#     print("Starting camera...")
#     cap = cv2.VideoCapture(0)
#     if not cap.isOpened():
#         print("Error: Could not open camera!")  # Debug print
#         return
#     print("Camera initialized successfully!")
#
#     ai_trainer = PhysiotherapyAI()
#     exercise_type = 'squat'  # or 'arm_raise'
#
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to grab frame")
#             break
#
#         frame, feedback = ai_trainer.process_frame(frame, exercise_type)
#
#         # Display feedback
#         y = 30
#         for text in feedback:
#             cv2.putText(frame, text, (10, y),
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
#             y += 30
#
#         cv2.imshow('Physiotherapy AI', frame)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#
#     print("Cleaning up...")
#     cap.release()
#     cv2.destroyAllWindows()
#
#
# if __name__ == "__main__":
#     print("Program starting...")  # Debug print
#     main()

def main():
    print("Welcome to Physiotherapy AI!")

    # Ask user for exercise type
    exercise_type = None
    while exercise_type not in ['squat', 'arm_raise']:
        exercise_type = input("Which exercise would you like to perform? (squat/arm_raise): ").strip().lower()
        if exercise_type not in ['squat', 'arm_raise']:
            print("Invalid choice. Please enter 'squat' or 'arm_raise'.")

    print(f"Starting {exercise_type} detection...")

    print("Starting camera...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera!")  # Debug print
        return
    print("Camera initialized successfully!")

    ai_trainer = PhysiotherapyAI()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame, feedback = ai_trainer.process_frame(frame, exercise_type)

        # Display feedback
        y = 30
        for text in feedback:
            cv2.putText(frame, text, (10, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            y += 30

        cv2.imshow('Physiotherapy AI', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("Cleaning up...")
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    print("Program starting...")  # Debug print
    main()
