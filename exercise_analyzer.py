# import cv2
# import json
# import numpy as np
# import os
# import time  # Added for delay before deleting file
# from datetime import datetime
# from utils.pose_detector import PoseDetector, calculate_angle
# import argparse
#
#
# class ExerciseAnalyzer:
#     def __init__(self):
#         self.pose_detector = PoseDetector()
#
#     def analyze_video(self, video_path, exercise_type, start_time=0, end_time=None):
#         """Analyze the video and return angle data"""
#         cap = cv2.VideoCapture(video_path)
#
#         if not cap.isOpened():
#             print(f"Error: Unable to open video file {video_path}")
#             return None
#
#         # Set video start position
#         cap.set(cv2.CAP_PROP_POS_MSEC, start_time * 1000)
#
#         fps = cap.get(cv2.CAP_PROP_FPS)
#         frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#
#         if end_time is None:
#             end_time = frame_count / fps
#
#         angle_data = {
#             'exercise_type': exercise_type,
#             'video_path': video_path,
#             'start_time': start_time,
#             'end_time': end_time,
#             'fps': fps,
#             'frames': []
#         }
#
#         frame_number = 0
#
#         while cap.isOpened():
#             ret, frame = cap.read()
#             if not ret:
#                 break
#
#             current_time = frame_number / fps
#             if current_time > end_time:
#                 break
#
#             # Process frame
#             landmarks = self.pose_detector.detect_pose(frame)
#
#             if landmarks:
#                 frame_data = {
#                     'frame_number': frame_number,
#                     'timestamp': current_time,
#                     'angles': self.get_exercise_angles(landmarks, exercise_type)
#                 }
#                 angle_data['frames'].append(frame_data)
#
#             frame_number += 1
#
#             # Show progress
#             if frame_number % 30 == 0:
#                 progress = (current_time - start_time) / (end_time - start_time) * 100
#                 print(f"Progress: {progress:.1f}%")
#
#         # Ensure the video file is properly released
#         cap.release()
#         cv2.destroyAllWindows()  # Close any OpenCV windows
#
#         return angle_data
#
#     def get_exercise_angles(self, landmarks, exercise_type):
#         """Get relevant angles based on exercise type"""
#         angles = {}
#
#         if exercise_type == 'squat':
#             # Left leg
#             if all(p in landmarks for p in [23, 25, 27]):
#                 angles['left_knee'] = calculate_angle(
#                     landmarks[23][:2],  # hip
#                     landmarks[25][:2],  # knee
#                     landmarks[27][:2]  # ankle
#                 )
#
#             # Right leg
#             if all(p in landmarks for p in [24, 26, 28]):
#                 angles['right_knee'] = calculate_angle(
#                     landmarks[24][:2],  # hip
#                     landmarks[26][:2],  # knee
#                     landmarks[28][:2]  # ankle
#                 )
#
#         elif exercise_type == 'arm_raise':
#             # Left arm
#             if all(p in landmarks for p in [11, 13, 15]):
#                 angles['left_arm'] = 180 - calculate_angle(
#                     landmarks[11][:2],  # shoulder
#                     landmarks[13][:2],  # elbow
#                     landmarks[15][:2]  # wrist
#                 )
#
#             # Right arm
#             if all(p in landmarks for p in [12, 14, 16]):
#                 angles['right_arm'] = calculate_angle(
#                     landmarks[12][:2],  # shoulder
#                     landmarks[14][:2],  # elbow
#                     landmarks[16][:2]  # wrist
#                 )
#
#         # Add more exercise types here
#
#         return angles
#
#     def save_to_json(self, data, output_file):
#         """Save angle data to JSON file"""
#         with open(output_file, 'w') as f:
#             json.dump(data, f, indent=4)
#
#
# def main():
#     parser = argparse.ArgumentParser(description='Analyze exercise form from a local video file')
#     parser.add_argument('--video', required=True, help='Path to the local video file')
#     parser.add_argument('--exercise', required=True, help='Exercise type (squat/arm_raise)')
#     parser.add_argument('--start', type=float, default=0, help='Start time in seconds')
#     parser.add_argument('--end', type=float, help='End time in seconds')
#     parser.add_argument('--output', required=True, help='Output JSON file path')
#
#     args = parser.parse_args()
#
#     analyzer = ExerciseAnalyzer()
#
#     # Analyze video
#     print("Analyzing video...")
#     angle_data = analyzer.analyze_video(
#         args.video,
#         args.exercise,
#         start_time=args.start,
#         end_time=args.end
#     )
#
#     if angle_data:
#         # Save results
#         print("Saving results...")
#         analyzer.save_to_json(angle_data, args.output)
#         print(f"Analysis complete. Results saved to {args.output}")
#     else:
#         print("Analysis failed.")
#
#
# if __name__ == "__main__":
#     main()
