"""
MediaPipe Pose Detector
"""
import cv2
import mediapipe as mp
import numpy as np
from typing import Dict, Any, List, Optional


class PoseDetector:
    """
    Human pose detection using MediaPipe.
    
    Detects 33 body keypoints and calculates body angles.
    """
    
    # MediaPipe keypoint names
    KEYPOINT_NAMES = [
        'nose', 'left_eye_inner', 'left_eye', 'left_eye_outer',
        'right_eye_inner', 'right_eye', 'right_eye_outer',
        'left_ear', 'right_ear', 'mouth_left', 'mouth_right',
        'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
        'left_wrist', 'right_wrist', 'left_pinky', 'right_pinky',
        'left_index', 'right_index', 'left_thumb', 'right_thumb',
        'left_hip', 'right_hip', 'left_knee', 'right_knee',
        'left_ankle', 'right_ankle', 'left_heel', 'right_heel',
        'left_foot_index', 'right_foot_index'
    ]
    
    def __init__(self, 
                 min_detection_confidence: float = 0.5,
                 min_tracking_confidence: float = 0.5):
        """
        Initialize pose detector.
        
        Args:
            min_detection_confidence: Minimum confidence for detection
            min_tracking_confidence: Minimum confidence for tracking
        """
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        
        self.pose = self.mp_pose.Pose(
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence,
            model_complexity=1,  # 0=lite, 1=full, 2=heavy
        )
    
    def detect(self, frame: np.ndarray) -> Dict[str, Any]:
        """
        Detect pose in a single frame.
        
        Args:
            frame: Input image (BGR format)
        
        Returns:
            {
                'detected': bool,
                'keypoints': List[Dict],  # [{'id', 'name', 'x', 'y', 'z', 'visibility'}]
                'angles': Dict,           # Body angles
            }
        """
        # Convert BGR to RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process
        results = self.pose.process(image_rgb)
        
        if not results.pose_landmarks:
            return {
                'detected': False,
                'keypoints': [],
                'angles': {},
            }
        
        # Extract keypoints
        keypoints = self._extract_keypoints(results.pose_landmarks, frame.shape)
        
        # Calculate angles
        angles = self._calculate_angles(keypoints)
        
        return {
            'detected': True,
            'keypoints': keypoints,
            'angles': angles,
        }
    
    def _extract_keypoints(self, landmarks, image_shape) -> List[Dict[str, Any]]:
        """Extract keypoints from MediaPipe landmarks."""
        h, w = image_shape[:2]
        keypoints = []
        
        for idx, landmark in enumerate(landmarks.landmark):
            keypoints.append({
                'id': idx,
                'name': self.KEYPOINT_NAMES[idx],
                'x': landmark.x * w,
                'y': landmark.y * h,
                'z': landmark.z,
                'visibility': landmark.visibility,
            })
        
        return keypoints
    
    def _calculate_angles(self, keypoints: List[Dict]) -> Dict[str, float]:
        """
        Calculate body angles.
        
        Returns angles in degrees.
        """
        angles = {}
        
        # Helper to get keypoint by name
        def get_point(name: str) -> Optional[np.ndarray]:
            for kp in keypoints:
                if kp['name'] == name:
                    return np.array([kp['x'], kp['y']])
            return None
        
        # Right elbow angle (shoulder-elbow-wrist)
        r_shoulder = get_point('right_shoulder')
        r_elbow = get_point('right_elbow')
        r_wrist = get_point('right_wrist')
        
        if r_shoulder is not None and r_elbow is not None and r_wrist is not None:
            angles['right_elbow'] = self._angle_between_points(r_shoulder, r_elbow, r_wrist)
        
        # Left elbow angle
        l_shoulder = get_point('left_shoulder')
        l_elbow = get_point('left_elbow')
        l_wrist = get_point('left_wrist')
        
        if l_shoulder is not None and l_elbow is not None and l_wrist is not None:
            angles['left_elbow'] = self._angle_between_points(l_shoulder, l_elbow, l_wrist)
        
        # Right knee angle (hip-knee-ankle)
        r_hip = get_point('right_hip')
        r_knee = get_point('right_knee')
        r_ankle = get_point('right_ankle')
        
        if r_hip is not None and r_knee is not None and r_ankle is not None:
            angles['right_knee'] = self._angle_between_points(r_hip, r_knee, r_ankle)
        
        # Left knee angle
        l_hip = get_point('left_hip')
        l_knee = get_point('left_knee')
        l_ankle = get_point('left_ankle')
        
        if l_hip is not None and l_knee is not None and l_ankle is not None:
            angles['left_knee'] = self._angle_between_points(l_hip, l_knee, l_ankle)
        
        # Shoulder rotation (angle between shoulders and horizontal)
        if r_shoulder is not None and l_shoulder is not None:
            shoulder_vec = r_shoulder - l_shoulder
            horizontal = np.array([1, 0])
            angles['shoulder_rotation'] = self._angle_between_vectors(shoulder_vec, horizontal)
        
        return angles
    
    @staticmethod
    def _angle_between_points(p1: np.ndarray, p2: np.ndarray, p3: np.ndarray) -> float:
        """
        Calculate angle at p2 formed by p1-p2-p3.
        
        Returns angle in degrees.
        """
        v1 = p1 - p2
        v2 = p3 - p2
        
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-6)
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        angle = np.arccos(cos_angle)
        
        return np.degrees(angle)
    
    @staticmethod
    def _angle_between_vectors(v1: np.ndarray, v2: np.ndarray) -> float:
        """Calculate angle between two vectors in degrees."""
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-6)
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        angle = np.arccos(cos_angle)
        return np.degrees(angle)
    
    def draw_pose(self, frame: np.ndarray, pose_result: Dict[str, Any]) -> np.ndarray:
        """
        Draw pose landmarks on frame.
        
        Args:
            frame: Input image
            pose_result: Result from detect()
        
        Returns:
            Annotated image
        """
        if not pose_result['detected']:
            return frame
        
        annotated = frame.copy()
        
        # Draw keypoints
        for kp in pose_result['keypoints']:
            if kp['visibility'] > 0.5:
                cv2.circle(annotated, 
                          (int(kp['x']), int(kp['y'])), 
                          5, (0, 255, 0), -1)
        
        # Draw angles
        y_offset = 30
        for name, angle in pose_result['angles'].items():
            text = f"{name}: {angle:.1f}°"
            cv2.putText(annotated, text, (10, y_offset),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            y_offset += 25
        
        return annotated
    
    def __del__(self):
        """Cleanup."""
        if hasattr(self, 'pose'):
            self.pose.close()
