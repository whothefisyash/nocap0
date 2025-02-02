import streamlit as st
import sys
import os
import base64
from dotenv import load_dotenv

# Add the backend directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

# Now you can import from backend
from twitter_utils import fetch_tweet_text
from fact_checker import check_misinformation

# Function to encode the image in base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Path to the logo image
logo_path = "assets/logo.jpg"

# Convert image to base64
logo_base64 = get_base64_image(logo_path)

# Display logo and title
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{logo_base64}" style="width: 120px; vertical-align: middle;"/> 
        <h1 style="font-size: 50px; margin: 0px;">NoCap</h1>
        <p style="font-size: 18px; color: grey;"><i>🔥 No Lies. No Cap. Just Facts.</i></p>
    </div>
    """, 
    unsafe_allow_html=True
)




# Option to choose between Text Input or Tweet URL
option = st.radio("Choose an option:", ["Enter Text", "Check Tweet URL"])

def display_credibility_info(verdict, explanation):
    """Display the verdict and detailed explanation."""
    st.write(f"### Verdict: {verdict.upper()}")
    st.write("### Detailed Explanation:")
    st.write(explanation)

# If user chooses "Enter Text"
if option == "Check Text":
    text_input = st.text_area("Paste your text here:", height=200)
    
    # Fact check the entered text
    if st.button("Check Misinformation"):
        if text_input:
            # Fact check and handle the returned values
            result = check_misinformation(text_input)  # Returns tuple (verdict, explanation)

            if isinstance(result, tuple) and len(result) == 2:
                verdict, explanation = result
                display_credibility_info(verdict, explanation)
            else:
                # If the response format is unexpected, print the raw response for debugging
                st.error(f"Error: Unexpected response from fact-checker. Raw response: {result}")
        else:
            st.error("Please enter some text to check.")
            
# If user chooses "Check Tweet URL"
elif option == "Check X URL":
    tweet_url = st.text_input("Enter a X URL or X ID:", placeholder="https://x.com/user/status/1753564897654323200")

    # Check the misinformation for the tweet
    if st.button("Check Misinformation"):
        if tweet_url:
            tweet_text = fetch_tweet_text(tweet_url)
            st.write("🔍 **Extracted Tweet:**")
            st.info(tweet_text)

            # Fact check and handle the returned values
            result = check_misinformation(tweet_text)  # Returns tuple (verdict, explanation)
            
            if isinstance(result, tuple) and len(result) == 2:
                verdict, explanation = result
                display_credibility_info(verdict, explanation)
            else:
                st.error(f"Error: Unexpected response from fact-checker. Raw response: {result}")
        else:
            st.error("Please enter a valid Tweet URL or ID.")