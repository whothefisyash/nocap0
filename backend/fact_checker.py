import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

def check_misinformation(text):
    """Use Gemini to check if the text is true or false, and provide a detailed explanation."""
    try:
        # Create a prompt asking Gemini to check the claim and give a thorough explanation
        prompt = f"""
        Please verify the following statement: "{text}"
        - Provide a detailed analysis of whether this statement is true or false.
        - If the statement is true, explain why it is true with supporting evidence.
        - If the statement is false or misleading, explain why it is false, and correct it with factual details.
        - If the statement is unverifiable, explain why it cannot be verified with available information.
        - Include references to reputable sources or facts wherever applicable.
        """

        # Call the Gemini API with the provided text
        response = model.generate_content(prompt)
        
        # Debugging: Print the raw response to understand its structure
        print(f"Raw response from Gemini: {response}")

        if response:
            # Retrieve the generated response from Gemini
            explanation = response.text.strip()

            # Check if the explanation contains certain keywords to determine truthfulness
            if "true" in explanation.lower():
                verdict = "true"
            elif "false" in explanation.lower() or "misleading" in explanation.lower():
                verdict = "false"
            else:
                verdict = "unverifiable"
            
            # Return the verdict and explanation from Gemini
            return verdict, explanation
        else:
            return "Error", "No response received from Gemini API."

    except Exception as e:
        return "Error", f"An error occurred while processing the statement: {str(e)}"
