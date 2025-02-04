import cv2
import mediapipe as mp
import numpy as np


class LivePose:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        self.mp_draw = mp.solutions.drawing_utils
        self.counter = 0
        self.stage = None
        self.prev_stage = None

    def calculate_angle(self, point1, point2, point3):
        """Calculate the angle between three points"""
        point1 = np.array([point1.x, point1.y])
        point2 = np.array([point2.x, point2.y])
        point3 = np.array([point3.x, point3.y])

        radians = np.arctan2(point3[1] - point2[1], point3[0] - point2[0]) - \
                  np.arctan2(point1[1] - point2[1], point1[0] - point2[0])
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        return angle

    def process_frame(self, frame, exercise_type):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(rgb_frame)

        if not results.pose_landmarks:
            return frame, ["No pose detected"]

        self.mp_draw.draw_landmarks(
            frame,
            results.pose_landmarks,
            self.mp_pose.POSE_CONNECTIONS
        )

        landmarks = results.pose_landmarks.landmark
        feedback = []

        exercise_configs = {
            'squat': {
                'landmarks': [24, 26, 28],  # RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE
                'threshold': {'min': 120, 'max': 160},
                'message': 'Bend your knees more',
                'count_threshold': {'down': 140, 'up': 160}
            },
            'arm_raise': {
                'landmarks': [11, 13, 15],  # LEFT_SHOULDER, LEFT_ELBOW, LEFT_WRIST
                'threshold': {'min': 150, 'max': 180},
                'message': 'Raise your arms higher',
                'count_threshold': {'down': 90, 'up': 160}
            },
            'pushup': {
                'landmarks': [12, 14, 16],  # RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST
                'threshold': {'min': 80, 'max': 110},
                'message': 'Lower your body until arms are at 90 degrees',
                'count_threshold': {'down': 90, 'up': 160}
            },
            'lunge': {
                'landmarks': [24, 26, 28],  # RIGHT_HIP, RIGHT_KNEE, RIGHT_ANKLE
                'threshold': {'min': 85, 'max': 95},
                'message': 'Bend your front knee to 90 degrees',
                'count_threshold': {'down': 90, 'up': 140}
            }
        }

        config = exercise_configs[exercise_type]

        # Calculate primary angle
        primary_angle = self.calculate_angle(
            landmarks[config['landmarks'][0]],
            landmarks[config['landmarks'][1]],
            landmarks[config['landmarks'][2]]
        )

        # For arm raise, also track right arm
        if exercise_type == 'arm_raise':
            # Calculate right arm angle (RIGHT_SHOULDER, RIGHT_ELBOW, RIGHT_WRIST)
            right_angle = self.calculate_angle(
                landmarks[12],
                landmarks[14],
                landmarks[16]
            )
            # Use the average of both arms
            angle = (primary_angle + right_angle) / 2
        else:
            angle = primary_angle

        # Count repetitions with adjusted logic
        if self.stage is None:
            self.stage = "up"  # Initialize stage

        if angle <= config['count_threshold']['down'] and self.stage == "up":
            self.stage = "down"
        elif angle >= config['count_threshold']['up'] and self.stage == "down":
            self.stage = "up"
            self.counter += 1

        # Draw counter and angle
        cv2.putText(frame, f"Angle: {int(angle)}",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2)
        cv2.putText(frame, f"Count: {self.counter}",
                    (10, 70), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2)
        cv2.putText(frame, f"Stage: {self.stage}",
                    (10, 110), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 255, 255), 2)

        # Check if angle is within threshold
        if angle < config['threshold']['min'] or angle > config['threshold']['max']:
            feedback.append(config['message'])

        # Exercise-specific additional checks
        if exercise_type == 'pushup':
            spine_angle = self.calculate_angle(
                landmarks[12],  # RIGHT_SHOULDER
                landmarks[24],  # RIGHT_HIP
                landmarks[28]  # RIGHT_ANKLE
            )
            if spine_angle < 160:
                feedback.append("Keep your body straight")

        elif exercise_type == 'lunge':
            back_knee_angle = self.calculate_angle(
                landmarks[23],  # LEFT_HIP
                landmarks[25],  # LEFT_KNEE
                landmarks[27]  # LEFT_ANKLE
            )
            if back_knee_angle > 100:
                feedback.append("Lower your back knee more")

        if not feedback:
            feedback.append("Good form!")

        return frame, feedback

    def reset_counter(self):
        """Reset the exercise counter and stage"""
        self.counter = 0
        self.stage = None