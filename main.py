import cv2
import argparse
from live_pose import LivePose


def parse_args():
    parser = argparse.ArgumentParser(description='Exercise Form Analysis')
    parser.add_argument('--exercise', type=str, required=True,
                        choices=['squat', 'pushup', 'arm_raise', 'lunge'],
                        help='Type of exercise to analyze')
    parser.add_argument('--camera', type=int, default=0,
                        help='Camera index (default: 0)')
    return parser.parse_args()


def main():
    args = parse_args()

    # Initialize camera
    cap = cv2.VideoCapture(args.camera)
    live_pose = LivePose()

    # Set camera resolution (optional)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    print(f"\nAnalyzing {args.exercise} form...")
    print("\nControls:")
    print("Press 'q' to quit")
    print("Press 'r' to reset counter\n")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        frame = cv2.flip(frame, 1)
        processed_frame, feedback = live_pose.process_frame(frame, args.exercise)

        # Display feedback
        y_position = 150
        for fb in feedback:
            cv2.putText(processed_frame, fb,
                        (10, y_position),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)
            y_position += 40

        cv2.imshow('Exercise Form Analysis', processed_frame)

        # Handle keyboard input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):
            live_pose.reset_counter()

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()




