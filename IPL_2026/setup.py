"""
Setup script for IPL 2026 Match Intelligence Dashboard
Enables pip install -e . for development
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="ipl-2026-dashboard",
    version="1.0.0",
    description="Comprehensive IPL 2026 Match Intelligence Dashboard with analysis, visualizations, and interactive exploration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Data Analytics Team",
    author_email="analytics@example.com",
    url="https://github.com/yourusername/ipl-2026-dashboard",
    license="MIT",
    
    packages=find_packages(),
    
    install_requires=[
        "streamlit>=1.28.0",
        "pandas>=2.0.0",
        "plotly>=5.15.0",
        "matplotlib>=3.8.0",
        "seaborn>=0.12.0",
        "numpy>=1.24.0",
        "jupyter>=1.0.0",
        "ipykernel>=6.25.0",
        "scikit-learn>=1.3.0",
        "scipy>=1.11.0",
    ],
    
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "pylint>=2.17.0",
        ],
        "notebooks": [
            "jupyter>=1.0.0",
            "ipykernel>=6.25.0",
        ],
    },
    
    python_requires=">=3.8",
    
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    
    keywords="ipl cricket analytics dashboard visualization data-science",
    
    project_urls={
        "Bug Reports": "https://github.com/yourusername/ipl-2026-dashboard/issues",
        "Source": "https://github.com/yourusername/ipl-2026-dashboard",
    },
)
