import streamlit as st
import pandas as pd
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from textblob import TextBlob

st.title("🧠 LLM-Based Product Feedback Analyzer")

uploaded_file = st.file_uploader("Upload Customer Feedback CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if 'feedback' not in df.columns:
        st.error("CSV must contain a 'feedback' column.")
    else:
        st.write("Sample Feedback Data", df.head())

        st.subheader("🔍 Topic Modeling with BERTopic")
        feedback = df['feedback'].astype(str).tolist()

        topic_model = BERTopic()
        topics, probs = topic_model.fit_transform(feedback)
        df['topic'] = topics
        st.write("Top Topics", topic_model.get_topic_info().head())

        st.subheader("😊 Sentiment Analysis")
        df['sentiment'] = df['feedback'].apply(lambda x: TextBlob(x).sentiment.polarity)
        st.write("Sample Sentiment Scores", df[['feedback', 'sentiment']].head())

        st.subheader("📊 Complaints by Segment")
        if 'segment' in df.columns:
            complaint_topics = df[df['sentiment'] < 0].groupby('segment')['topic'].value_counts().unstack().fillna(0)
            st.write("Top Complaint Topics by Segment", complaint_topics)
        else:
            st.info("Add a 'segment' column to your CSV for segment-level insights.")

        st.subheader("📈 Sentiment by Feature (Manual Tag Example)")
        if 'feature' in df.columns:
            sentiment_by_feature = df.groupby('feature')['sentiment'].mean().sort_values()
            st.bar_chart(sentiment_by_feature)
        else:
            st.info("Include a 'feature' column for sentiment-by-feature mapping.")
