# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
#
#
# import cv2
# import json
# import os
# import numpy as np
# from pytube import YouTube
# from utils.pose_detector import PoseDetector  # Import your PoseDetector
#
# EXERCISE_NAME = "arm_raise"  # Change this for different exercises
# OUTPUT_JSON = f"data/{EXERCISE_NAME}.json"
#
# # Replace with the actual YouTube video link
# YOUTUBE_URL = "https://www.youtube.com/watch?v=your_video_id"
#
#
# def download_youtube_video(url, output_path="videos/"):
#     try:
#         yt = YouTube(url)
#         stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
#        #stream = yt.streams.filter(res="360p").first()  # Low resolution for faster processing
#        # Low resolution for faster processing
#         if stream is None:
#             print(f"No suitable video stream found for resolution 360p. Trying with the highest resolution.")
#             stream = yt.streams.get_highest_resolution()  # Fallback to highest resolution
#         video_path = stream.download(output_path)
#         print(f"Video downloaded to {video_path}")
#         return video_path
#     except Exception as e:
#         print(f"Error downloading the video: {e}")
#         return None
#
#
# def extract_angles_from_video(video_path):
#     if not video_path:
#         print("No video path provided, exiting.")
#         return
#
#     detector = PoseDetector()
#     cap = cv2.VideoCapture(video_path)
#
#     angle_list = []
#
#     while cap.isOpened():
#         success, frame = cap.read()
#         if not success:
#             break
#
#         frame = detector.find_pose(frame, draw=False)
#         landmarks = detector.get_positions(frame)
#
#         if landmarks:
#             angles = detector.extract_angles(landmarks)
#             angle_list.append(angles)
#
#     cap.release()
#
#     if angle_list:
#         # Compute average angles across all frames
#         avg_angles = np.mean(angle_list, axis=0).tolist()
#
#         # Save angles to JSON
#         os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)  # Ensure the 'data' folder exists
#         with open(OUTPUT_JSON, "w") as f:
#             json.dump({"exercise": EXERCISE_NAME, "angles": avg_angles}, f, indent=4)
#
#         print(f"Angles stored in {OUTPUT_JSON}")
#     else:
#         print("No angles were detected in the video.")
#
#
# if __name__ == "__main__": #if _name_ == "__main__":
#
#     os.makedirs("videos", exist_ok=True)  # Ensure the 'videos' folder exists
#     video_path = download_youtube_video("https://www.youtube.com/watch?v=Bqvmyni_sKQ")
#     extract_angles_from_video(video_path)

# import os
# import cv2
# import json
# import numpy as np
# from utils.pose_detector import PoseDetector  # Import your PoseDetector
#
#
#
# EXERCISE_NAME = "arm_raise"  # Change this for different exercises
# OUTPUT_JSON = f"data/{EXERCISE_NAME}.json"
#
# VIDEO_PATH = "C:/Users/Drashti/Downloads/1 Minute Yoga Upper Body Stretches ( BEST Desk Yoga Stretch! ) (1).mp4"  # Update with the correct path to your downloaded video
#
# # Define the timestamps (in seconds) where you want to extract angles/poses
# TIMESTAMPS = [36, 40]  # Example: 5 seconds, 10 seconds, 15 seconds
# TOLERANCE = 0.5  # Tolerance (in seconds) for matching timestamps
#
# def extract_angles_from_video(video_path):
#     if not video_path:
#         print("No video path provided, exiting.")
#         return
#
#     detector = PoseDetector()
#     cap = cv2.VideoCapture(video_path)
#
#     angle_list = []
#     frame_count = 0  # Counter to keep track of frames
#     video_fps = cap.get(cv2.CAP_PROP_FPS)  # Get frames per second (fps) of the video
#
#     # Sort timestamps to make sure they are in order
#     TIMESTAMPS.sort()
#
#     while cap.isOpened():
#         success, frame = cap.read()
#         if not success:
#             print("Failed to read frame. Exiting.")
#             break
#
#         frame_count += 1
#         current_time = frame_count / video_fps  # Get the current timestamp in seconds
#
#         # Check if the current frame is within the tolerance range of any timestamp
#         for timestamp in TIMESTAMPS:
#             if abs(current_time - timestamp) <= TOLERANCE:
#                 print(f"Processing frame at {current_time:.2f} seconds (target: {timestamp} seconds)")
#
#                 frame = detector.find_pose(frame, draw=False)  # Call the pose detector to detect poses
#                 landmarks = detector.get_positions(frame)  # Get the landmarks of the frame
#
#                 if landmarks:
#                     print(f"Landmarks detected: {landmarks}")  # Debug print to check landmarks
#                     angles = detector.extract_angles(landmarks)  # Extract angles from landmarks
#                     if angles:
#                         print(f"Angles detected: {angles}")  # Debug print to check angles
#                         angle_list.append(angles)
#                 else:
#                     print(f"No landmarks detected at {current_time:.2f} seconds.")  # Debug print if no landmarks found
#
#         # Skip frames to reach the next timestamp
#         if current_time > max(TIMESTAMPS):
#             break
#
#     cap.release()
#
#     if angle_list:
#         # Compute average angles across the selected timestamps
#         avg_angles = np.mean(angle_list, axis=0).tolist()
#
#         # Save angles to JSON
#         os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)  # Ensure the 'data' folder exists
#         with open(OUTPUT_JSON, "w") as f:
#             json.dump({"exercise": EXERCISE_NAME, "angles": avg_angles}, f, indent=4)
#
#         print(f"Angles stored in {OUTPUT_JSON}")
#     else:
#         print("No angles were detected at the specified timestamps.")
#
# if __name__ == "__main__":
#     extract_angles_from_video(VIDEO_PATH)


import os
import cv2
import json
from utils.pose_detector import PoseDetector

EXERCISE_NAME = "arm_raise"
OUTPUT_JSON = f"data/{EXERCISE_NAME}.json"

VIDEO_PATH = "C:/Users/Drashti/Downloads/1 Minute Yoga Upper Body Stretches ( BEST Desk Yoga Stretch! ) (1).mp4"

TIMESTAMPS = [36, 40]
TOLERANCE = 0.5  # Tolerance (in seconds)

POINTS = {
    'left_elbow': (11, 13, 15),
    'right_elbow': (12, 14, 16),
    'left_knee': (23, 25, 27),
    'right_knee': (24, 26, 28)
}

def extract_angles_from_video(video_path):
    if not video_path:
        print("No video path provided, exiting.")
        return

    detector = PoseDetector()
    cap = cv2.VideoCapture(video_path)

    angle_ranges = {f"{ts}s": {} for ts in TIMESTAMPS}  # Store min-max ranges
    frame_count = 0
    video_fps = cap.get(cv2.CAP_PROP_FPS)

    TIMESTAMPS.sort()

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame_count += 1
        current_time = frame_count / video_fps

        for timestamp in TIMESTAMPS:
            if abs(current_time - timestamp) <= TOLERANCE:
                frame = detector.find_pose(frame, draw=False)
                angles = detector.extract_angles(frame, POINTS)

                if angles:
                    for key, value in angles.items():
                        rounded_angle = round(value, 1)
                        if key not in angle_ranges[f"{timestamp}s"]:
                            angle_ranges[f"{timestamp}s"][key] = {"min": rounded_angle, "max": rounded_angle}
                        else:
                            # Update min and max values
                            angle_ranges[f"{timestamp}s"][key]["min"] = min(angle_ranges[f"{timestamp}s"][key]["min"], rounded_angle)
                            angle_ranges[f"{timestamp}s"][key]["max"] = max(angle_ranges[f"{timestamp}s"][key]["max"], rounded_angle)

        if current_time > max(TIMESTAMPS):
            break

    cap.release()

    if any(angle_ranges.values()):
        os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
        with open(OUTPUT_JSON, "w") as f:
            json.dump({"exercise": EXERCISE_NAME, "angles": angle_ranges}, f, indent=4)

        print(f"Angle ranges stored in {OUTPUT_JSON}")
    else:
        print("No angles detected at the specified timestamps.")

if __name__ == "__main__":
    extract_angles_from_video(VIDEO_PATH)




