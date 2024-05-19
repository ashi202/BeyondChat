import requests
import streamlit as st
from transformers import pipeline

# Initialize NLP pipeline for zero-shot text classification
nlp_pipeline = pipeline("zero-shot-classification")

def fetch_data(api_url):
    data = []
    page = 1
    while True:
        response = requests.get(f"{api_url}?page={page}")
        if response.status_code != 200:
            break
        page_data = response.json()
        
        if isinstance(page_data, dict):  # Handle single dictionary response
            page_data = [page_data]
        
        if not isinstance(page_data, list):
            st.error(f"Unexpected data type received from API. Expected a list, got {type(page_data)}")
            break
        
        data.extend(page_data)
        page += 1
        
        # Debug: Print API response
        print(f"API Response (Page {page}):", page_data)
        
    return data

def process_data(data):
    citations = []
    for item in data:
        response_text = item.get('response', '')
        sources = item.get('sources', [])
        for source in sources:
            context = source.get('context', '')
            # Use NLP pipeline to determine similarity or relevance
            result = nlp_pipeline(response_text, context, hypothesis_template="This text is about {}.")
            if result['labels'][0]['score'] > 0.5 and result['labels'][0]['label'] == 'LABEL_PRESENT':
                citation = {'id': source.get('id'), 'link': source.get('link', '')}
                citations.append(citation)
    return citations

def get_citations(api_url):
    data = fetch_data(api_url)
    citations = process_data(data)
    return citations

def main():
    st.title("API Data Fetcher and Processor")
    
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    
    if st.button('Fetch and Process Data'):
        with st.spinner('Fetching data...'):
            citations = get_citations(api_url)
        
        st.success('Data fetched and processed successfully!')
        
        if citations:
            st.markdown("### Citation Output")
            for citation in citations:
                st.write(citation)
        else:
            st.write("No citations found.")
        
        # Debug: Display fetched data
        st.write("Debug: Fetched data from API")
        st.write(fetch_data(api_url))

if __name__ == "__main__":
    main()
