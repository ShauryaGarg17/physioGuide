import cv2
import argparse
from live_pose import LivePose
from utils.pose_detector import PoseDetector


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--exercise', type=str, default='squat',
                      help='Type of exercise to track (squat, pushup, arm_raise, lunge)')
    parser.add_argument('--video', type=str, default='0',
                      help='Path to video file (0 for webcam)')
    args = parser.parse_args()

    # Initialize detector
    detector = PoseDetector()

    # Set up video capture
    if args.video == '0':
        cap = cv2.VideoCapture(0)
    else:
        cap = cv2.VideoCapture(args.video)

    # Set video resolution
    cap.set(3, 1280)
    cap.set(4, 720)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Process frame
        frame = detector.process_frame(frame, args.exercise)

        # Display frame
        cv2.imshow('Exercise Detection', frame)

        # Break loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()