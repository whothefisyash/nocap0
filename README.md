# NoCap AI-Based Misinformation Discovery and Fact-Checking Application

## Overview

This application is designed to help users detect misinformation in text and tweets using AI and NLP techniques. The app enables users to input text or paste content from the clipboard, check tweets for misinformation, and get real-time fact-checking results.

## Features

- **Check through Text Input**: Users can enter text to be checked for misinformation.
- **Check Misinformation in Tweets**: The app can analyze tweets for potential misinformation.
- **Real-time Fact-Checking**: Integration with AI models to provide fact-checking results.
- **User-Friendly Interface**: Built with Streamlit for easy interaction.

## Technologies Used

- **AI Models**: Gemini API or any free large language model (LLM) for generating fact-checking results.
- **Frontend**: Streamlit for building the interactive interface.
- **Backend**: Python-based API for processing and returning fact-checking results.
- **External APIs**: Tweepy for interacting with Twitter to fetch tweets and check misinformation.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/whothefisyash/nocap0.git
   ```
   
2. Navigate to the project directory:
   ```bash
   cd misinformation-checker
   ```

3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Make sure to set up API keys and environment variables in a `.env` file for external services (like Tweepy, Gemini API, etc.).

## Usage

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Access the app through your browser at `http://localhost:8501`.

3. **Check Text**: Enter the text you want to analyze and click "Check Misinformation."
   
4. **Check Tweet**: Paste the tweet URL and click "Check Misinformation."

## Example Use Case

- **Text Input**: Paste a paragraph or sentence, and the app will provide real-time feedback on whether the statement contains potential misinformation.
- **Tweet Analysis**: Paste a tweet URL to check whether the tweet contains misinformation or misleading claims.
- **Browser Extension**: A browser extension that allows users to check any webpage or tweet in real time for misinformation.

## Contributing

Feel free to fork the repository and contribute to the project. Please create an issue or pull request with the changes you want to propose.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

