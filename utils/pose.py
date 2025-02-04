# import cv2
# import mediapipe as mp
# import numpy as np
#
#
# class PoseDetector:
#     def __init__(self, static_image_mode=False, model_complexity=1, min_detection_confidence=0.5,
#                  min_tracking_confidence=0.5):
#         self.static_image_mode = static_image_mode
#         self.model_complexity = model_complexity
#         self.min_detection_confidence = min_detection_confidence
#         self.min_tracking_confidence = min_tracking_confidence
#
#         self.mp_pose = mp.solutions.pose
#         self.pose = self.mp_pose.Pose(
#             static_image_mode=self.static_image_mode,
#             model_complexity=self.model_complexity,
#             min_detection_confidence=self.min_detection_confidence,
#             min_tracking_confidence=self.min_tracking_confidence
#         )
#         self.mp_draw = mp.solutions.drawing_utils
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
#         landmarks = []
#         if self.results.pose_landmarks:
#             for id, lm in enumerate(self.results.pose_landmarks.landmark):
#                 h, w, c = img.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 landmarks.append([id, cx, cy])
#         return landmarks


import cv2
import mediapipe as mp
import numpy as np

class PoseDetector:
    def __init__(self, static_image_mode=False, model_complexity=1, min_detection_confidence=0.5,
                 min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.model_complexity = model_complexity
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=self.static_image_mode,
            model_complexity=self.model_complexity,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_pose(self, img, draw=True):
        """Detects pose landmarks and optionally draws them on the image."""
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
        """Extracts (id, x, y) for each detected landmark."""
        landmarks = {}
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, _ = img.shape
                landmarks[id] = (int(lm.x * w), int(lm.y * h))
        return landmarks

    def calculate_angle(self, a, b, c):
        """Computes the angle between three points."""
        a, b, c = np.array(a), np.array(b), np.array(c)

        ba = a - b
        bc = c - b

        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        angle = np.degrees(np.arccos(np.clip(cosine_angle, -1.0, 1.0)))

        return angle

    def extract_angles(self, landmarks):
        """Calculates specific joint angles from detected pose landmarks."""
        if not landmarks:
            return {}

        try:
            left_shoulder = landmarks[11]
            left_elbow = landmarks[13]
            left_wrist = landmarks[15]

            shoulder_angle = self.calculate_angle(left_shoulder, left_elbow, left_wrist)

            return {"shoulder_angle": shoulder_angle}

        except KeyError:
            return {}
