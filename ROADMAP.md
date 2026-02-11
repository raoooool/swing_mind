# 🎾 Swing Mind - Development Roadmap

## Project Goal

Build a zero-training, high-performance tennis video analysis core engine providing pose detection, ball tracking, and action analysis.

---

## Core Modules

### 1. Pose Detection
**Technology:** MediaPipe Pose  
**Features:**
- Real-time tracking of 33 body keypoints
- Swing trajectory extraction
- Body posture parameters (knee angle, shoulder rotation, etc.)
- Foundation data for action classification

**Output:**
```json
{
  "keypoints": [
    {"id": 0, "name": "nose", "x": 320, "y": 240, "z": 0.1, "visibility": 0.99},
    ...
  ],
  "angles": {
    "right_elbow": 135,
    "right_knee": 145,
    "shoulder_rotation": 45
  }
}
```

---

### 2. Ball Tracking
**Technology:** OpenCV color detection + motion detection  
**Features:**
- Real-time ball position detection
- Trajectory tracking
- Speed calculation
- Landing point prediction

**Output:**
```json
{
  "trajectory": [
    {"frame": 0, "x": 100, "y": 200, "visible": true},
    ...
  ],
  "speed": 85.5,  // km/h
  "landing_point": {"x": 450, "y": 380}
}
```

---

### 3. Court Detection
**Technology:** Hough transform + perspective transformation  
**Features:**
- Automatic court boundary detection
- Coordinate system establishment
- Pixel coordinates → real distance conversion
- Out-of-bounds detection

**Output:**
```json
{
  "court_lines": [...],
  "transform_matrix": [...],
  "real_world_coords": {
    "ball_landing": {"x": 5.2, "y": 8.3}  // meters
  }
}
```

---

### 4. Shot Detection
**Technology:** Collision detection + ball speed change  
**Features:**
- Automatic shot moment recognition
- Shot type classification (forehand/backhand/serve/volley)
- Video segmentation by shots

**Output:**
```json
{
  "shots": [
    {
      "frame": 125,
      "timestamp": 4.17,
      "type": "forehand",
      "contact_point": {"x": 200, "y": 300}
    },
    ...
  ]
}
```

---

### 5. Action Classification
**Technology:** Rule-based classification engine  
**Features:**
- Forehand/backhand/serve/volley recognition
- Action phase division (preparation-contact-follow-through)
- Action feature extraction

**Rule Examples:**
- Forehand: Right hand on right side + forward swing
- Backhand: Right hand crosses body centerline + left swing
- Serve: Arm raised high + downward swing

---

### 6. Metrics Calculation
**Technology:** NumPy geometric calculations  
**Features:**

**Swing Metrics:**
- Swing speed (m/s or km/h)
- Swing angle (degrees)
- Contact height (meters)
- Follow-through distance (meters)

**Body Metrics:**
- Knee bend angle
- Weight transfer
- Shoulder rotation angle
- Footwork movement distance

**Ball Metrics:**
- Ball speed (before/after contact)
- Spin estimation (via trajectory curvature)
- Landing accuracy
- Flight time

**Output:**
```json
{
  "swing_speed": 120,  // km/h
  "swing_angle": 45,
  "contact_height": 1.2,  // meters
  "knee_angle": 135,
  "ball_speed_before": 60,
  "ball_speed_after": 85
}
```

---

### 7. Quality Scoring
**Technology:** Rule engine + standard action comparison  
**Features:**
- Action quality score (0-100)
- Dimension-wise scoring (posture, contact point, follow-through, etc.)
- Improvement suggestions

**Output:**
```json
{
  "overall_score": 78,
  "breakdown": {
    "posture": 85,
    "contact_point": 70,
    "follow_through": 80
  },
  "suggestions": [
    "Contact point could be higher",
    "Follow-through incomplete"
  ]
}
```

---

## Development Plan

### **Phase 1: MVP (Current)**
**Timeline:** Week 1-2  
**Goal:** Basic framework + pose detection

- [x] Project scaffolding
- [x] MediaPipe pose detection integration
- [x] Video reading and processing
- [x] Keypoint visualization
- [x] Basic angle calculation
- [x] Unit tests

**Deliverables:**
- Runnable pose detection demo
- Keypoint JSON output
- Annotated visualization video

---

### **Phase 2: Ball Tracking**
**Timeline:** Week 3  
**Goal:** Tennis ball detection and tracking

- [ ] Color detection implementation
- [ ] Motion detection implementation
- [ ] Trajectory tracking algorithm
- [ ] Speed calculation
- [ ] Shot detection (simple version)

**Deliverables:**
- Ball tracking demo
- Trajectory visualization
- Speed output

---

### **Phase 3: Metrics Calculation**
**Timeline:** Week 4  
**Goal:** Basic parameter extraction

- [ ] Swing speed calculation
- [ ] Body angle calculation
- [ ] Contact point detection
- [ ] Aggregated metrics output

**Deliverables:**
- Complete metrics JSON
- Metrics visualization

---

### **Phase 4: Court Detection**
**Timeline:** Week 5  
**Goal:** Coordinate system establishment

- [ ] Court line detection
- [ ] Perspective transformation
- [ ] Coordinate conversion
- [ ] Out-of-bounds detection

---

### **Phase 5: Action Classification**
**Timeline:** Week 6  
**Goal:** Action recognition

- [ ] Rule engine design
- [ ] Forehand/backhand classification
- [ ] Serve recognition
- [ ] Action phase division

---

### **Phase 6: Quality Scoring**
**Timeline:** Week 7+  
**Goal:** Professional-level analysis

- [ ] Scoring algorithm design
- [ ] Standard action library
- [ ] Comparison algorithm (DTW)
- [ ] Improvement suggestion generation

---

## Technology Selection

| Module | Technology | Reason | Training Required |
|--------|-----------|--------|-------------------|
| Pose Detection | MediaPipe Pose | Pre-trained, fast, accurate | ❌ No training |
| Ball Tracking | OpenCV color+motion detection | Simple, robust, CPU-friendly | ❌ No training |
| Court Detection | Hough transform | Classic algorithm, stable | ❌ No training |
| Shot Detection | Collision detection + rules | Real-time, accurate | ❌ No training |
| Action Classification | Rule engine | Interpretable, easy to debug | ❌ No training |
| Metrics Calculation | NumPy geometric calculations | Precise, fast | ❌ No training |

**Core Principle: Zero training, all pre-trained models + traditional CV**

---

## Performance Goals

- **Processing Speed:** 5-10 FPS (CPU) / 20-30 FPS (GPU)
- **Memory Usage:** < 2GB
- **Accuracy:**
  - Pose detection: > 95%
  - Ball tracking: > 90%
  - Shot detection: > 85%

---

## Future Extensions

### **Advanced Features**
- Multi-angle fusion
- 3D reconstruction
- Real-time feedback (< 1 second latency)
- Comparative analysis (multiple players)

### **Statistical Analysis**
- Heatmaps (movement range, landing distribution)
- Trend analysis (fatigue, speed decay)
- Match report generation

### **Deep Learning Enhancement**
- Train custom racket detection model
- Action quality scoring model
- Tactical analysis

---

## Reference Projects

- **ArtLabss/tennis-tracking** - Ball tracking reference
- **avivcaspi/TennisProject** - Comprehensive analysis reference
- **Google MediaPipe** - Pose estimation
- **TrackNet** - Ball tracking paper implementation

---

## Current Status

**Version:** v0.1.0-alpha  
**Progress:** Phase 1 - Pose detection in development  
**Last Updated:** 2026-02-11
