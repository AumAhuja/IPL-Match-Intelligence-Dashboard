"""
Configuration module for IPL 2026 Match Intelligence Dashboard
Centralized settings and path management
"""

from pathlib import Path
import os

# ============================================================================
# PROJECT PATHS
# ============================================================================

# Get the project root directory (parent of this file)
PROJECT_ROOT = Path(__file__).parent.absolute()

# Data directories
DATA_DIR = PROJECT_ROOT / 'ipl_2026_data'
NOTEBOOKS_DIR = PROJECT_ROOT / 'notebooks'
REPORTS_DIR = PROJECT_ROOT / 'reports'
VISUALIZATIONS_DIR = PROJECT_ROOT / 'visualizations'
SRC_DIR = PROJECT_ROOT / 'src'
DASHBOARD_DIR = PROJECT_ROOT / 'dashboard'

# ============================================================================
# DATA FILE PATHS
# ============================================================================

# CSV files
MATCHES_CSV = DATA_DIR / 'final_matches_data.csv'
DELIVERIES_CSV = DATA_DIR / 'final_ipl_2026_deliveries_data.csv'

# Backup paths (if files are renamed or moved)
MATCHES_CSV_ALT = DATA_DIR / 'matches.csv'
DELIVERIES_CSV_ALT = DATA_DIR / 'ipl_2026_deliveries.csv'

# ============================================================================
# APPLICATION SETTINGS
# ============================================================================

# Streamlit configuration
APP_TITLE = "IPL 2026 Match Intelligence Dashboard"
APP_ICON = "🏏"
APP_LAYOUT = "wide"

# Analysis parameters
MIN_BALLS_FACED = 50  # Minimum balls for strike rate calculation
MIN_OVERS_BOWLED = 2  # Minimum overs for bowling analysis

# Color scheme
PRIMARY_COLOR = "#1f4788"
SECONDARY_COLOR = "#185FA5"
SUCCESS_COLOR = "#28a745"
WARNING_COLOR = "#ffc107"
DANGER_COLOR = "#dc3545"

# ============================================================================
# DATABASE / CACHE SETTINGS
# ============================================================================

# Cache directory for processed data (if needed)
CACHE_DIR = PROJECT_ROOT / '.cache'
CACHE_DIR.mkdir(exist_ok=True)

# ============================================================================
# LOGGING SETTINGS
# ============================================================================

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = PROJECT_ROOT / 'logs' / 'app.log'
LOG_FILE.parent.mkdir(exist_ok=True)

# ============================================================================
# VALIDATION FUNCTIONS
# ============================================================================

def validate_data_files():
    """Validate that all required data files exist"""
    errors = []
    
    # Check primary files
    if not MATCHES_CSV.exists() and not MATCHES_CSV_ALT.exists():
        errors.append(f"Matches data not found at {MATCHES_CSV}")
    
    if not DELIVERIES_CSV.exists() and not DELIVERIES_CSV_ALT.exists():
        errors.append(f"Deliveries data not found at {DELIVERIES_CSV}")
    
    return errors

def get_data_file(primary_path, alt_path=None):
    """Get the correct path for a data file, checking primary and alternate locations"""
    if primary_path.exists():
        return primary_path
    elif alt_path and alt_path.exists():
        return alt_path
    else:
        raise FileNotFoundError(f"Data file not found. Checked: {primary_path}")

# ============================================================================
# ENVIRONMENT VARIABLES
# ============================================================================

# Load from .env file if it exists (for local development)
try:
    from dotenv import load_dotenv
    load_dotenv(PROJECT_ROOT / '.env')
except ImportError:
    pass

# Debug mode
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# ============================================================================
# PRINT CONFIG ON IMPORT (for debugging)
# ============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("IPL 2026 Dashboard Configuration")
    print("=" * 60)
    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Data Directory: {DATA_DIR}")
    print(f"Matches CSV: {MATCHES_CSV} (exists: {MATCHES_CSV.exists()})")
    print(f"Deliveries CSV: {DELIVERIES_CSV} (exists: {DELIVERIES_CSV.exists()})")
    print(f"Debug Mode: {DEBUG}")
    print("=" * 60)
    
    # Validate files
    errors = validate_data_files()
    if errors:
        print("⚠️  Configuration Issues:")
        for error in errors:
            print(f"  - {error}")
    else:
        print("✅ All data files found and accessible")
