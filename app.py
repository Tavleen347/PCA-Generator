import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

# 1. Page Configuration
st.set_page_config(page_title="CS Team PCA Generator", page_icon="📊", layout="wide")
st.title("📊 Automated PCA AI Agent")
st.write("Upload all Go-Live and Power BI Report files to generate the PCA narrative.")

# 2. Configure the AI Brain using the Secret Key
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash') # We use the fast, smart model
except Exception as e:
    st.warning("⚠️ AI not connected yet. Please add your GEMINI_API_KEY to the Streamlit Secrets.")

# 3. Sidebar for Settings
with st.sidebar:
    st.header("Campaign Settings")
    brand_theme = st.selectbox("Brand Theme:", ("McDonald's", "Petronas", "Nike", "Adidas"))
    platform = st.selectbox("Platform:", ("YouTube Mirrors", "TikTok", "Meta", "CTV"))

# 4. Bulk File Uploader
uploaded_files = st.file_uploader(
    "Drag & Drop ALL Campaign Files here (Go-Live & Reports)", 
    type=["csv", "xlsx"], 
    accept_multiple_files=True
)

st.markdown("---")

# 5. The "Generate Insights" Engine
if st.button("🧠 Analyze Data & Generate PCA Insights", type="primary"):
    if uploaded_files:
        if "GEMINI_API_KEY" not in st.secrets:
            st.error("Please add your Gemini API Key in the settings first!")
        else:
            with st.spinner("The AI is reading your files and drafting the PCA..."):
                
                # A. Read all the uploaded files into one massive text summary for the AI
                all_data_text = ""
                for file in uploaded_files:
                    if file.name.endswith('.csv'):
                        df = pd.read_csv(file)
                    else:
                        df = pd.read_excel(file)
                    
                    all_data_text += f"\n\n--- FILE: {file.name} ---\n"
                    # We only send the top 10 rows of each file to the AI to save memory, 
                    # which is usually enough to understand the totals and top performers.
                    all_data_text += df.head(10).to_string() 

                # B. The "Prompt" - Instructions for the AI
                prompt = f"""
                You are an expert Media Analyst for an ad tech company. 
                You are writing a Post Campaign Analysis (PCA) presentation for a {brand_theme} campaign running on {platform}.
                
                I am providing you with the raw data extracted from our Go-Live sheet and our Power BI reporting dashboard.
                
                RAW DATA:
                {all_data_text}
                
                Based ONLY on the data provided above, draft the narrative text for the PCA slides. 
                Format your response clearly with the following sections:
                
                1. Objective & Strategy: Summarize the target audience, the budget/booked views, and the contextual targeting strategy used.
                2. Performance Highlights: Highlight the Delivered Views vs Booked Views. Call out the overall VTR (View-Through Rate) and VCR (Video Completion Rate). Mention which demographic or context performed the best.
                3. Recommendations: Give 2 professional recommendations for the next campaign based on the data.
                
                Keep the tone professional, analytical, and ready to be pasted into a presentation deck. Do not make up numbers.
                """
                
                # C. Send to AI and get response
                try:
                    response = model.generate_content(prompt)
                    
                    # D. Display the Results!
                    st.success("PCA Narrative Generated Successfully!")
                    st.write(response.text)
                    
                except Exception as e:
                    st.error(f"Error generating insights: {e}")
    else:
        st.warning("Please upload the campaign files first.")
