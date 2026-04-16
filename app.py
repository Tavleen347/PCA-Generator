import streamlit as st

# 1. Set the title of the web page
st.set_page_config(page_title="CS Team PCA Generator", page_icon="📊")

# 2. Add a big header
st.title("📊 Automated PCA Generator")
st.write("Welcome to the internal tool for the CS Team! Let's build a report.")

# 3. Create a dropdown for the Brand Theme
brand_theme = st.selectbox(
    "Select the Brand Theme:",
    ("Nike", "Adidas", "Puma", "Under Armour")
)

# 4. Create a text box for the Campaign ID
campaign_id = st.text_input("Enter the Go-Live Campaign ID (e.g., CMP-1234):")

# 5. Create a button to trigger the action
if st.button("Fetch Campaign Data"):
    if campaign_id:
        # This is where we will eventually connect Google Sheets!
        st.success(f"Success! Looking up data for {campaign_id} using the {brand_theme} theme...")
        st.info("Right now, this is just a mockup. Next, we will connect this to Google Sheets!")
    else:
        st.error("Please enter a Campaign ID first.")
