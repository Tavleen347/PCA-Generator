import streamlit as st
import pandas as pd

# 1. Set the title of the web page
st.set_page_config(page_title="CS Team PCA Generator", page_icon="📊")
st.title("📊 Automated PCA Generator")

st.write("Welcome to the internal tool for the CS Team! Upload a Go-Live file to begin.")

# 2. Create the UI Elements
brand_theme = st.selectbox(
    "Select the Brand Theme:", 
    ("McDonald's", "Nike", "Adidas", "Puma", "Under Armour")
)

# 3. Create the File Uploader (Accepts both CSV and Excel)
uploaded_file = st.file_uploader("Upload your Go-Live Campaign File (.csv or .xlsx)", type=["csv", "xlsx"])

# 4. Trigger the Data Pull
if st.button("Read Campaign Data"):
    if uploaded_file is not None:
        try:
            st.info("Reading the file...")
            
            # Use Pandas to read the file based on its extension
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.success("Success! The app can see your data.")
            
            # Display a preview of the data on the screen
            st.write("### Data Preview")
            st.dataframe(df)
            
            st.info("Right now, the app is just reading the raw file. The next step is connecting the AI brain to make sense of it!")
            
        except Exception as e:
            st.error(f"An error occurred while reading the file: {e}")
    else:
        st.error("Please upload a file first.")
