"""
IPL 2026 Analysis Module
Comprehensive cricket analytics functions for IPL data

This package provides utilities for analyzing IPL match data including:
- Batting analysis and player statistics
- Bowling analysis and performance metrics
- Venue-specific analysis
- Team performance evaluation
- Impact scoring and player rankings
- Correlation analysis
"""

__version__ = "1.0.0"
__author__ = "Data Analytics Team"

# Import commonly used functions for easier access
try:
    from .batting_analysis import *
    from .bowling_analysis import *
    from .venue_analysis import *
    from .toss_analysis import *
    from .correlations import *
    from .impact_score import *
    from .feature_engineering import *
    from .data_cleaning import *
except ImportError as e:
    print(f"Warning: Could not import some modules: {e}")

__all__ = [
    'batting_analysis',
    'bowling_analysis',
    'venue_analysis',
    'toss_analysis',
    'correlations',
    'impact_score',
    'feature_engineering',
    'data_cleaning',
]
