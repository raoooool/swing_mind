"""
Pose detection demo with webcam or video file
"""
import cv2
import sys
from swing_mind.pose import PoseDetector


def main():
    # Get video source (0 for webcam, or path to video file)
    source = sys.argv[1] if len(sys.argv) > 1 else 0
    
    # Initialize detector
    detector = PoseDetector()
    
    # Open video
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        print(f"Error: Cannot open video source: {source}")
        return
    
    print("Press 'q' to quit")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect pose
        result = detector.detect(frame)
        
        # Draw pose
        annotated = detector.draw_pose(frame, result)
        
        # Show result
        cv2.imshow('Pose Detection', annotated)
        
        # Quit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
