# 🎾 Swing Mind - Tennis Video Analysis Engine

Intelligent tennis video analysis core module providing pose detection, ball tracking, and action analysis.

## Overview

**Input:** Tennis video + configuration parameters  
**Output:** Structured analysis results (JSON) + annotated video (optional)

## Core Features

- ✅ **Pose Detection**: Human keypoint tracking using MediaPipe
- 🚧 **Ball Tracking**: Ball trajectory, speed, and landing point analysis
- 🚧 **Court Detection**: Coordinate system establishment and perspective transformation
- 🚧 **Shot Detection**: Automatic shot moment recognition
- 🚧 **Action Classification**: Forehand, backhand, and serve recognition
- 🚧 **Metrics Calculation**: Swing speed, angles, and body posture
- 🚧 **Quality Scoring**: Action quality assessment and suggestions

## Quick Start

### Installation

```bash
uv sync --dev
```

### Basic Usage

```python
from swing_mind import TennisAnalyzer

# Create analyzer
analyzer = TennisAnalyzer()

# Analyze video
result = analyzer.analyze('video.mp4')

# Print results
print(result['summary'])
```

## Project Structure

```
swing_mind/
├── README.md                 # Project documentation
├── ROADMAP.md               # Development roadmap
├── pyproject.toml           # Packaging and tool config
├── requirements.txt         # Runtime dependency snapshot (optional)
├── src/
│   └── swing_mind/          # Core package
│       ├── __init__.py
│       ├── analyzer.py
│       ├── pose/
│       ├── ball/
│       ├── court/
│       ├── shot/
│       ├── action/
│       ├── metrics/
│       └── utils/
├── tests/                   # Tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_pose.py
│   └── test_analyzer.py
├── examples/                # Examples
│   ├── basic_usage.py
│   └── pose_demo.py
└── docs/                    # Documentation
    └── api.md
```

## Tech Stack

- **Python 3.10+**
- **OpenCV** - Video processing
- **MediaPipe** - Pose estimation
- **NumPy** - Numerical computing
- **SciPy** - Scientific computing

## Development Status

Current version: **v0.1.0-alpha**  
Current progress: **Pose detection module in development**

See [ROADMAP.md](ROADMAP.md) for details

## Development Commands

```bash
uv run pytest
uv run ruff check src tests
uv run ruff format src tests examples
```

## License

MIT
