#!/bin/bash
# Professor Corrects - One-Click Activation
echo "🎓 Activating Professor Corrects..."
cd "$(dirname "$0")"
source venv/bin/activate 2>/dev/null || echo "Note: No virtualenv found, using global python."
pip install -r requirements.txt --quiet
streamlit run streamlit_professor_corrects.py
