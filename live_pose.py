import cv2
import json
import numpy as np
from utils.pose_detector import PoseDetector

EXERCISE_NAME = "arm_raise"
INPUT_JSON = f"data/{EXERCISE_NAME}.json"

def load_reference_angles():
    with open(INPUT_JSON, "r") as f:
        data = json.load(f)
    return data["angles"]

def compare_angles(ref_angles, current_angles):
    if not ref_angles or not current_angles:
        return "No valid angles detected"

    diff = np.abs(np.array(ref_angles) - np.array(current_angles))
    threshold = 10  # Adjust this threshold based on accuracy needed
    if np.all(diff < threshold):
        return "Correct Form ✅"
    else:
        return "Incorrect Form ❌"

def main():
    detector = PoseDetector()
    ref_angles = load_reference_angles()
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame = detector.find_pose(frame, draw=True)
        landmarks = detector.get_positions(frame)
        current_angles = detector.extract_angles(landmarks) if landmarks else []

        feedback = compare_angles(ref_angles, current_angles)
        cv2.putText(frame, feedback, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Live Pose Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
