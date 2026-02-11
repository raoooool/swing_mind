"""
Main Tennis Analyzer
"""
import cv2
from typing import Dict, Any, Optional
from .pose.detector import PoseDetector
from .utils.video import VideoProcessor


class TennisAnalyzer:
    """
    Main tennis video analysis engine.
    
    Example:
        >>> analyzer = TennisAnalyzer()
        >>> result = analyzer.analyze('video.mp4')
        >>> print(result['summary'])
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the analyzer.
        
        Args:
            config: Configuration dictionary
                {
                    'pose_model': 'mediapipe',  # Pose estimation model
                    'output_video': True,        # Generate annotated video
                    'fps': 30,                   # Processing FPS
                }
        """
        self.config = config or {}
        
        # Initialize modules
        self.pose_detector = PoseDetector()
        self.video_processor = VideoProcessor()
        
    def analyze(self, video_path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Analyze a tennis video.
        
        Args:
            video_path: Path to video file
            params: Analysis parameters
                {
                    'fps': 30,                    # Processing FPS
                    'roi': [x1, y1, x2, y2],     # Region of interest
                    'player_side': 'right',       # Player position
                }
        
        Returns:
            Analysis result dictionary:
            {
                'metadata': {...},      # Video info
                'frames': [...],        # Per-frame analysis
                'actions': [...],       # Action segments
                'summary': {...},       # Overall summary
            }
        """
        params = params or {}
        
        # Open video
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError(f"Cannot open video: {video_path}")
        
        # Get video metadata
        metadata = self.video_processor.get_metadata(cap)
        
        # Process frames
        frames = []
        frame_id = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            # Pose detection
            pose_result = self.pose_detector.detect(frame)
            
            # Store frame result
            frames.append({
                'frame_id': frame_id,
                'timestamp': frame_id / metadata['fps'],
                'pose': pose_result,
            })
            
            frame_id += 1
        
        cap.release()
        
        # Generate summary
        summary = self._generate_summary(frames)
        
        return {
            'metadata': metadata,
            'frames': frames,
            'summary': summary,
        }
    
    def _generate_summary(self, frames: list) -> Dict[str, Any]:
        """Generate analysis summary."""
        return {
            'total_frames': len(frames),
            'duration': frames[-1]['timestamp'] if frames else 0,
        }
