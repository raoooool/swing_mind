# Swing Mind API Documentation

## TennisAnalyzer

Main analysis engine.

### Constructor

```python
TennisAnalyzer(config: Optional[Dict[str, Any]] = None)
```

**Parameters:**
- `config`: Configuration dictionary (optional)

### Methods

#### analyze()

```python
analyze(video_path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]
```

Analyze a tennis video.

**Parameters:**
- `video_path`: Path to video file
- `params`: Analysis parameters (optional)

**Returns:**
- Analysis result dictionary

---

## PoseDetector

Human pose detection using MediaPipe.

### Constructor

```python
PoseDetector(
    min_detection_confidence: float = 0.5,
    min_tracking_confidence: float = 0.5
)
```

### Methods

#### detect()

```python
detect(frame: np.ndarray) -> Dict[str, Any]
```

Detect pose in a single frame.

**Returns:**
```python
{
    'detected': bool,
    'keypoints': List[Dict],  # 33 keypoints
    'angles': Dict,           # Body angles
}
```

#### draw_pose()

```python
draw_pose(frame: np.ndarray, pose_result: Dict[str, Any]) -> np.ndarray
```

Draw pose landmarks on frame.

---

## Keypoint Names

MediaPipe provides 33 keypoints:

- Face: nose, eyes, ears, mouth
- Upper body: shoulders, elbows, wrists, hands
- Lower body: hips, knees, ankles, feet

See `PoseDetector.KEYPOINT_NAMES` for full list.

---

## Angles

Calculated angles:
- `right_elbow`: Right elbow angle
- `left_elbow`: Left elbow angle
- `right_knee`: Right knee angle
- `left_knee`: Left knee angle
- `shoulder_rotation`: Shoulder rotation angle
