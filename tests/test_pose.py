"""
Unit tests for pose detector
"""
import pytest
import numpy as np
from swing_mind.pose import PoseDetector


def test_pose_detector_init():
    """Test pose detector initialization."""
    detector = PoseDetector()
    assert detector is not None


def test_pose_detector_empty_frame():
    """Test detection on empty frame."""
    detector = PoseDetector()
    
    # Create black frame
    frame = np.zeros((480, 640, 3), dtype=np.uint8)
    
    result = detector.detect(frame)
    
    assert 'detected' in result
    assert 'keypoints' in result
    assert 'angles' in result


def test_angle_calculation():
    """Test angle calculation between points."""
    # Right angle (90 degrees)
    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    p3 = np.array([1, 1])
    
    angle = PoseDetector._angle_between_points(p1, p2, p3)
    
    assert abs(angle - 90.0) < 1.0  # Allow small error


def test_angle_between_vectors():
    """Test angle between vectors."""
    v1 = np.array([1, 0])
    v2 = np.array([0, 1])
    
    angle = PoseDetector._angle_between_vectors(v1, v2)
    
    assert abs(angle - 90.0) < 1.0
