# LLM-Based Product Feedback Analyzer

🔍 Overview
Built an interactive Streamlit app that ingests unstructured customer feedback and applies NLP and LLM-based techniques to surface actionable insights for product and CX teams.

##The app helps identify:

- Top themes and complaints using BERTopic for topic modeling

- Customer sentiment using TextBlob

- Segment-specific issues and product pain points

- Sentiment trends mapped to features for roadmap planning

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
Or 
Click https://llm-based-app-feedback-analyzer.streamlit.app/

Upload a CSV with at least a `feedback` column. Optionally include `segment` and `feature` columns for deeper analysis.
