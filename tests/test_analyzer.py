"""
Unit tests for analyzer
"""
import pytest
from swing_mind import TennisAnalyzer


def test_analyzer_init():
    """Test analyzer initialization."""
    analyzer = TennisAnalyzer()
    assert analyzer is not None


def test_analyzer_with_config():
    """Test analyzer with custom config."""
    config = {
        'output_video': True,
        'fps': 30,
    }
    analyzer = TennisAnalyzer(config)
    assert analyzer.config == config
