# Installation & Setup Guide

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

---

## 🚀 Quick Start (Recommended)

### 1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/ipl-2026-dashboard.git
cd ipl-2026-dashboard
```

### 2. **Create Virtual Environment**
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Run the Dashboard**
```bash
cd dashboard
streamlit run streamlit_app.py
```

The dashboard will open at `http://localhost:8501`

---

## 📓 Run Jupyter Notebook

```bash
# Activate virtual environment (if not already)
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Start Jupyter
jupyter notebook

# Navigate to notebooks/IPL_2026_Complete_Analysis.ipynb
```

---

## 📊 View PDF Report

```bash
# Open the report directly
open reports/final_report.pdf           # macOS
xdg-open reports/final_report.pdf       # Linux
start reports/final_report.pdf          # Windows
```

---

## 🔧 Development Installation

For contributing to the project:

```bash
# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Now you can modify code and changes take effect immediately
```

---

## ✅ Verify Installation

Test that everything is set up correctly:

```bash
python config.py
```

Expected output:
```
============================================================
IPL 2026 Dashboard Configuration
============================================================
Project Root: /path/to/ipl-2026-dashboard
Data Directory: /path/to/ipl-2026-dashboard/ipl_2026_data
Matches CSV: /path/to/ipl-2026-dashboard/ipl_2026_data/final_matches_data.csv (exists: True)
Deliveries CSV: /path/to/ipl-2026-dashboard/ipl_2026_data/final_ipl_2026_deliveries_data.csv (exists: True)
Debug Mode: False
============================================================
✅ All data files found and accessible
```

---

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'streamlit'`
**Solution**: Make sure you've activated the virtual environment and installed requirements.txt
```bash
source venv/bin/activate  # Activate venv
pip install -r requirements.txt
```

### Issue: `FileNotFoundError: Data file not found`
**Solution**: Ensure you're running commands from the project root directory
```bash
# Navigate to project root
cd ipl-2026-dashboard

# Then run streamlit
cd dashboard
streamlit run streamlit_app.py
```

### Issue: Port 8501 already in use
**Solution**: Streamlit will automatically try another port. Or specify a different port:
```bash
streamlit run streamlit_app.py --server.port 8502
```

### Issue: Jupyter kernel not found
**Solution**: Install and activate the kernel
```bash
python -m ipykernel install --user --name ipl-env --display-name "IPL 2026"
```

---

## 📦 Dependencies Overview

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.28.1 | Interactive web dashboard |
| pandas | 2.1.0 | Data manipulation and analysis |
| plotly | 5.17.0 | Interactive visualizations |
| matplotlib | 3.8.0 | Static plots and visualizations |
| seaborn | 0.12.2 | Statistical data visualization |
| numpy | 1.24.3 | Numerical computations |
| jupyter | 1.0.0 | Notebook environment |
| scikit-learn | 1.3.1 | Machine learning utilities |
| scipy | 1.11.3 | Scientific computing |

---

## 🔄 Updating Dependencies

To update all packages to their latest compatible versions:

```bash
pip install --upgrade -r requirements.txt
```

To update a specific package:

```bash
pip install --upgrade streamlit
```

---

## 💻 Running on Different Systems

### macOS
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd dashboard && streamlit run streamlit_app.py
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd dashboard && streamlit run streamlit_app.py
```

### Windows (PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
cd dashboard
streamlit run streamlit_app.py
```

---

## 🌐 Deploying to Cloud

### Heroku
1. Create `Procfile`:
```
web: cd dashboard && streamlit run streamlit_app.py --logger.level=error
```

2. Deploy:
```bash
git push heroku main
```

### Streamlit Cloud
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Select your repository and file
4. It deploys automatically!

### AWS/GCP/Azure
See deployment guides in each cloud provider's documentation.

---

## 📞 Getting Help

1. Check this guide's troubleshooting section
2. Review README.md for project overview
3. See QUICK_START.md for usage examples
4. Check PROJECT_SUMMARY.md for detailed documentation

---

## ✨ You're All Set!

Your IPL 2026 Dashboard is now ready to use. Start with one of these:

- 📊 **Interactive Exploration**: `streamlit run dashboard/streamlit_app.py`
- 📓 **Deep Analysis**: `jupyter notebook notebooks/IPL_2026_Complete_Analysis.ipynb`
- 📈 **Quick Summary**: Open `reports/final_report.pdf`

Happy analyzing! 🏏📊
