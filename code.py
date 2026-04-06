import streamlit as st
import os

# Set page config for a professional look
st.set_page_config(page_title="HigherMarks Dashboard", layout="centered")

st.title("Question Analytics")

# Define the path to your image
image_path = "assets/2.png"

# Check if the file exists to avoid app crashes
if os.path.exists(image_path):
    st.success("Question 2 Loaded Successfully")
    
    # Using columns to center the image or add metadata later
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # use_container_width=True makes it responsive for mobile/desktop
        st.image(image_path, caption="Mathematics - Question 02", use_container_width=True)
        
    with col2:
        st.write("### Quick Stats")
        st.metric(label="Difficulty", value="Medium")
        st.metric(label="Avg. Time", value="150s")
else:
    st.error(f"Error: {image_path} not found. Please check your folder structure.")