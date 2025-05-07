# LLM-Based Product Feedback Analyzer

This app allows product teams to analyze unstructured customer feedback using NLP and LLM-based topic modeling.

## 🔍 Features
- BERTopic for topic modeling on feedback text
- TextBlob for quick sentiment scoring
- Segment-level complaint identification
- Feature-wise sentiment comparison (if tagged)

## 📦 Stack
- Python, Pandas
- BERTopic
- TextBlob
- Streamlit

## ▶️ How to Run
```bash
pip install -r requirements.txt
streamlit run app/feedback_analyzer.py
```

Upload a CSV with at least a `feedback` column. Optionally include `segment` and `feature` columns for deeper analysis.
