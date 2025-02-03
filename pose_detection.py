import cv2
import numpy as np
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, model_complexity=1, enable_segmentation=False, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    return 360.0 - angle if angle > 180.0 else angle

def get_coordinates(landmarks, index, width, height):
    landmark = landmarks[index]
    return [int(landmark.x * width), int(landmark.y * height)]

def arm_raise_detection(frame, landmarks, width, height):
    hip = get_coordinates(landmarks, mp_pose.PoseLandmark.LEFT_HIP.value, width, height)
    shoulder = get_coordinates(landmarks, mp_pose.PoseLandmark.LEFT_SHOULDER.value, width, height)
    elbow = get_coordinates(landmarks, mp_pose.PoseLandmark.LEFT_ELBOW.value, width, height)

    shoulder_angle = calculate_angle(hip, shoulder, elbow)

    cv2.putText(frame, f'Shoulder Angle: {int(shoulder_angle)} degrees', tuple(shoulder),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    if shoulder_angle > 160:
        cv2.putText(frame, 'Good Arm Raise!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, 'Raise your arm higher!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

def squat_detection(frame, landmarks, width, height):
    hip = get_coordinates(landmarks, mp_pose.PoseLandmark.LEFT_HIP.value, width, height)
    knee = get_coordinates(landmarks, mp_pose.PoseLandmark.LEFT_KNEE.value, width, height)
    ankle = get_coordinates(landmarks, mp_pose.PoseLandmark.LEFT_ANKLE.value, width, height)
    knee_angle = calculate_angle(hip, knee, ankle)

    cv2.putText(frame, f'Knee Angle: {int(knee_angle)} degrees', tuple(knee),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    if 70 < knee_angle < 90:
        cv2.putText(frame, 'Good squat posture!', (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    elif knee_angle >= 90:
        cv2.putText(frame, 'Bend your knees more!', (50, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

def leg_raise_detection(frame, landmarks, width, height):
    shoulder = get_coordinates(landmarks, mp_pose.PoseLandmark.LEFT_SHOULDER.value, width, height)
    hip = get_coordinates(landmarks, mp_pose.PoseLandmark.LEFT_HIP.value, width, height)
    knee = get_coordinates(landmarks, mp_pose.PoseLandmark.LEFT_KNEE.value, width, height)
    leg_angle = calculate_angle(shoulder, hip, knee)

    cv2.putText(frame, f'Leg Angle: {int(leg_angle)} degrees', tuple(hip),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    if leg_angle > 170:
        cv2.putText(frame, 'Straight leg! Keep it up!', (50, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, 'Straighten your leg!', (50, 170), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

def elbow_straightening_detection(frame, landmarks, width, height):
    shoulder = get_coordinates(landmarks, mp_pose.PoseLandmark.LEFT_SHOULDER.value, width, height)
    elbow = get_coordinates(landmarks, mp_pose.PoseLandmark.LEFT_ELBOW.value, width, height)
    wrist = get_coordinates(landmarks, mp_pose.PoseLandmark.LEFT_WRIST.value, width, height)

    elbow_angle = calculate_angle(shoulder, elbow, wrist)

    cv2.putText(frame, f'Elbow Angle: {int(elbow_angle)} degrees', tuple(elbow),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    if elbow_angle > 160:
        cv2.putText(frame, 'Good Elbow Posture!', (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    else:
        cv2.putText(frame, 'Straighten your elbow!', (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

def process_pose_detection(exercise_choice):
    cap = cv2.VideoCapture(0)

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            height, width, _ = frame.shape
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                landmarks = results.pose_landmarks.landmark

                if exercise_choice == 1:
                    arm_raise_detection(image, landmarks, width, height)
                elif exercise_choice == 2:
                    squat_detection(image, landmarks, width, height)
                elif exercise_choice == 3:
                    leg_raise_detection(image, landmarks, width, height)
                elif exercise_choice == 4:
                    elbow_straightening_detection(image, landmarks, width, height)

            cv2.imshow('Physiotherapy AI Pose Detection', image)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

def main():
    print("Select the exercise you want to perform:")
    print("1. Arm Raise")
    print("2. Squats")
    print("3. Leg Raise")
    print("4. Elbow Straightening")
    exercise_choice = int(input("Enter the number of your choice: "))

    if exercise_choice not in [1, 2, 3, 4]:
        print("Invalid choice! Exiting...")
        return

    process_pose_detection(exercise_choice)

if __name__ == "__main__":
    main()
