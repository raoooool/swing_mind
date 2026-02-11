# 🎾 Swing Mind - 网球视频分析引擎

智能网球视频分析核心模块，提供姿态检测、球追踪、动作分析等功能。

## 项目概述

**输入：** 网球视频 + 配置参数  
**输出：** 结构化分析结果（JSON）+ 可视化视频（可选）

## 核心功能

- ✅ **姿态检测**：基于 MediaPipe 的人体关键点追踪
- 🚧 **网球追踪**：球的轨迹、速度、落点分析
- 🚧 **球场检测**：坐标系统建立、透视变换
- 🚧 **击球检测**：自动识别击球时刻
- 🚧 **动作分类**：正手、反手、发球识别
- 🚧 **参数计算**：挥拍速度、角度、身体姿态等
- 🚧 **质量评分**：动作质量评估与建议

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 基础使用

```python
from swing_mind import TennisAnalyzer

# 创建分析器
analyzer = TennisAnalyzer()

# 分析视频
result = analyzer.analyze('video.mp4')

# 输出结果
print(result['summary'])
```

## 项目结构

```
swing_mind/
├── README.md                 # 项目说明
├── ROADMAP.md               # 开发计划
├── requirements.txt         # 依赖列表
├── setup.py                 # 安装配置
├── swing_mind/              # 核心模块
│   ├── __init__.py
│   ├── analyzer.py          # 主分析器
│   ├── pose/                # 姿态检测模块
│   │   ├── __init__.py
│   │   ├── detector.py      # MediaPipe 姿态检测
│   │   └── utils.py         # 工具函数
│   ├── ball/                # 球追踪模块
│   │   ├── __init__.py
│   │   ├── tracker.py       # 球追踪
│   │   └── detector.py      # 球检测
│   ├── court/               # 球场检测模块
│   │   ├── __init__.py
│   │   └── detector.py      # 球场检测
│   ├── shot/                # 击球检测模块
│   │   ├── __init__.py
│   │   └── detector.py      # 击球检测
│   ├── action/              # 动作分类模块
│   │   ├── __init__.py
│   │   └── classifier.py    # 动作分类
│   ├── metrics/             # 参数计算模块
│   │   ├── __init__.py
│   │   └── calculator.py    # 参数计算
│   └── utils/               # 通用工具
│       ├── __init__.py
│       ├── video.py         # 视频处理
│       └── geometry.py      # 几何计算
├── tests/                   # 测试
│   ├── __init__.py
│   ├── test_pose.py
│   └── test_analyzer.py
├── examples/                # 示例
│   ├── basic_usage.py
│   └── pose_demo.py
└── docs/                    # 文档
    └── api.md
```

## 技术栈

- **Python 3.10+**
- **OpenCV** - 视频处理
- **MediaPipe** - 姿态估计
- **NumPy** - 数值计算
- **SciPy** - 科学计算

## 开发状态

当前版本：**v0.1.0-alpha**  
当前进度：**姿态检测模块开发中**

详见 [ROADMAP.md](ROADMAP.md)

## License

MIT
