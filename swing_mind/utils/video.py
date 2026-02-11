"""
Video processing utilities
"""
import cv2
from typing import Dict, Any


class VideoProcessor:
    """Video processing helper."""
    
    @staticmethod
    def get_metadata(cap: cv2.VideoCapture) -> Dict[str, Any]:
        """
        Extract video metadata.
        
        Args:
            cap: OpenCV VideoCapture object
        
        Returns:
            {
                'width': int,
                'height': int,
                'fps': float,
                'frame_count': int,
                'duration': float,
            }
        """
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps if fps > 0 else 0
        
        return {
            'width': width,
            'height': height,
            'fps': fps,
            'frame_count': frame_count,
            'duration': duration,
        }
    
    @staticmethod
    def create_writer(output_path: str, 
                     width: int, 
                     height: int, 
                     fps: float,
                     fourcc: str = 'mp4v') -> cv2.VideoWriter:
        """
        Create video writer.
        
        Args:
            output_path: Output video path
            width: Frame width
            height: Frame height
            fps: Frames per second
            fourcc: Video codec (default: mp4v)
        
        Returns:
            VideoWriter object
        """
        fourcc_code = cv2.VideoWriter_fourcc(*fourcc)
        writer = cv2.VideoWriter(output_path, fourcc_code, fps, (width, height))
        return writer
