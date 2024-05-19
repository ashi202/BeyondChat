API Data Fetcher and Processor
This Streamlit application demonstrates how to fetch and process data from an API (https://devapi.beyondchats.com/api/get_message_with_sources) using Python's requests library and transformers from Hugging Face for zero-shot text classification.

Features
-Fetches data from a paginated API endpoint.
-Processes fetched data using a zero-shot text classification pipeline to identify relevant citations.
-Displays citations found based on specified criteria.
-Provides debugging information to verify fetched data.

Prerequisites
-Python 3.x installed on your system.
-pip package manager to install Python packages.

Installation
-Clone the repository to your local machine:
   git clone <repository_url>
   cd <repository_name>
-Install dependencies using pip:
   pip install -r requirements.txt


Usage
-Run the Streamlit app:
   python -m streamlit run beyondchats.py 
          or
   streamlit run app.py
   
-Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

-Click on the "Fetch and Process Data" button to initiate the data fetching and processing process.

-Wait for the app to fetch data from the API and process it. Once complete, the citations found will be displayed.

Application Structure
-beyondchats.py: Main application script containing Streamlit UI and data processing logic.
-requirements.txt: List of Python packages required for the application.

Libraries Used
-requests: HTTP library for making API requests.
-streamlit: Open-source Python library used to create web applications.
-transformers: Library from Hugging Face for natural language processing (NLP) tasks.

Troubleshooting
-If encountering issues with dependencies or running the app, ensure that all required packages are installed using pip install -r requirements.txt.



If facing issue

-Simply copy code of beyondchats.py.
-Paste in vs code by making file name beyondchats.py
-In terminal write  python -m streamlit run beyondchats.py.
-In new window project is opened.
