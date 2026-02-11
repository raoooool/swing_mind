"""
Basic usage example
"""
from swing_mind import TennisAnalyzer
import json


def main():
    # Create analyzer
    analyzer = TennisAnalyzer()
    
    # Analyze video
    print("Analyzing video...")
    result = analyzer.analyze('test_video.mp4')
    
    # Print summary
    print("\n=== Analysis Summary ===")
    print(f"Duration: {result['summary']['duration']:.2f}s")
    print(f"Total frames: {result['summary']['total_frames']}")
    
    # Print first frame pose
    if result['frames']:
        first_frame = result['frames'][0]
        if first_frame['pose']['detected']:
            print("\n=== First Frame Pose ===")
            print(f"Keypoints detected: {len(first_frame['pose']['keypoints'])}")
            print("Angles:")
            for name, angle in first_frame['pose']['angles'].items():
                print(f"  {name}: {angle:.1f}°")
    
    # Save full result
    with open('result.json', 'w') as f:
        json.dump(result, f, indent=2)
    print("\nFull result saved to result.json")


if __name__ == '__main__':
    main()
