import cv2
import mediapipe as mp
import numpy as np
from angle_calculator import calculate_angle

class PoseDetector:
    def __init__(self, static_image_mode=False,
                 model_complexity=1,
                 smooth_landmarks=True,
                 enable_segmentation=False,
                 smooth_segmentation=True,
                 min_detection_confidence=0.5,
                 min_tracking_confidence=0.5):
        """
        Initialize the PoseDetector with MediaPipe Pose parameters
        """
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=static_image_mode,
            model_complexity=model_complexity,
            smooth_landmarks=smooth_landmarks,
            enable_segmentation=enable_segmentation,
            smooth_segmentation=smooth_segmentation,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.results = None

    def find_pose(self, img, draw=True):
        """
        Detect pose landmarks in an image
        Args:
            img: Input image (BGR format)
            draw: Whether to draw landmarks on the image
        Returns:
            img: Processed image with landmarks drawn (if draw=True)
        """
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)

        if self.results.pose_landmarks and draw:
            self.mp_draw.draw_landmarks(
                img,
                self.results.pose_landmarks,
                self.mp_pose.POSE_CONNECTIONS
            )
        return img

    def get_positions(self, img):
        """
        Get landmark positions as pixel coordinates
        Args:
            img: Input image
        Returns:
            landmarks: Dictionary of landmark positions {id: (x, y)}
        """
        landmarks = {}
        if self.results.pose_landmarks:
            h, w, _ = img.shape
            for idx, landmark in enumerate(self.results.pose_landmarks.landmark):
                landmarks[idx] = (int(landmark.x * w), int(landmark.y * h))
        return landmarks

    def extract_angles(self, img, points):
        """
        Extract angles between specified landmark points
        Args:
            img: Input image
            points: Dictionary of point triplets {angle_name: (p1, p2, p3)}
        Returns:
            angles: Dictionary of calculated angles
        """
        landmarks = self.get_positions(img)
        if not landmarks:
            return {}

        angles = {}
        for key, (p1, p2, p3) in points.items():
            if all(p in landmarks for p in (p1, p2, p3)):
                angles[key] = calculate_angle(
                    landmarks[p1],
                    landmarks[p2],
                    landmarks[p3]
                )
        return angles

# import cv2
# import mediapipe as mp
# from .angle_calculator import calculate_angle
#
# class PoseDetector:
#     def __init__(self, static_image_mode=False,
#                  model_complexity=1,
#                  smooth_landmarks=True,
#                  enable_segmentation=False,
#                  smooth_segmentation=True,
#                  min_detection_confidence=0.5,
#                  min_tracking_confidence=0.5):
#         self.mp_pose = mp.solutions.pose
#         self.pose = self.mp_pose.Pose(
#             static_image_mode=static_image_mode,
#             model_complexity=model_complexity,
#             smooth_landmarks=smooth_landmarks,
#             enable_segmentation=enable_segmentation,
#             smooth_segmentation=smooth_segmentation,
#             min_detection_confidence=min_detection_confidence,
#             min_tracking_confidence=min_tracking_confidence
#         )
#         self.mp_draw = mp.solutions.drawing_utils
#         self.results = None
#
#     def find_pose(self, img, draw=True):
#         img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.pose.process(img_rgb)
#
#         if self.results.pose_landmarks and draw:
#             self.mp_draw.draw_landmarks(
#                 img,
#                 self.results.pose_landmarks,
#                 self.mp_pose.POSE_CONNECTIONS
#             )
#         return img
#
#     def get_positions(self, img):
#         landmarks = {}
#         if self.results.pose_landmarks:
#             h, w, _ = img.shape
#             for idx, landmark in enumerate(self.results.pose_landmarks.landmark):
#                 landmarks[idx] = (int(landmark.x * w), int(landmark.y * h))
#         return landmarks
#
#     def extract_angles(self, img, points):
#         landmarks = self.get_positions(img)
#         if not landmarks:
#             return {}
#
#         angles = {}
#         for key, (p1, p2, p3) in points.items():
#             if all(p in landmarks for p in (p1, p2, p3)):
#                 angle = calculate_angle(
#                     landmarks[p1],
#                     landmarks[p2],
#                     landmarks[p3]
#                 )
#                 angles[key] = angle  # Keep raw value; rounding happens in live_processing.py
#         return angles


