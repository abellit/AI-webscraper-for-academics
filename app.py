import streamlit as st
from utils.scrapper import scrape_website, extract_main_content, clean_main_content, split_dom_content
from utils.parse import parse_with_ollama

# Streamlit app configuration
st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ")

# Scrape button fundtionality
if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    main_content = extract_main_content(result)
    cleaned_content = clean_main_content(main_content)
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

# Parsing functionality  
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse.")
    
    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing content...")
            dom_chunks = split_dom_content(st.session_state.dom_content)
            results = parse_with_ollama(dom_chunks, parse_description)
            st.write(results)

# Instructions and notes
st.markdown(""
    "### Instructions:\n"
    "1. Enter a valid website URL in the input box.\n"
    "2. Click the 'Scrape Site' button to fetch the website content.\n"
    "3. Review the DOM content in the expandable section.\n"
    "4. Provide a description of the information you want to extract in the text area.\n"
    "5. Click the 'Parse Content' button to extract the specified information.\n"
    "6. The parsed results will be displayed below the button.\n"
    "7. If no information matches the description, an empty string will be returned.\n"
    "8. Ensure the website is accessible and the URL is correct.\n"
    "9. If you encounter any issues, check the console for error messages.\n"
    "10. Enjoy using the AI Web Scraper!"
            "")

st.markdown("### Note: "
    "This application uses AI to parse content from websites. "
    "Ensure you have the necessary permissions to scrape the website content. "
    "The AI model may not always return accurate results, so review the output carefully. "
    "If you have any questions or feedback, please reach out to the developer."
    "Thank you for using the AI Web Scraper!")

links = """
<a href='https://www.google.com' target='_blank'>Google</a><br>
<a href='https://www.github.com' target='_blank'>GitHub</a><br>
<a href='https://www.python.org' target='_blank'>Python</a>
"""

st.markdown(links, unsafe_allow_html=True);




# st.markdown("""
# <style>
#     .stButton button {
#         background-color: #4CAF50; /* Green */
#         border: none;
#         color: white;
#         padding: 10px 20px;
#         text-align: center;
#         text-decoration: none;
#         display: inline-block;
#         font-size: 16px;
#         margin: 4px 2px;
#         cursor: pointer;
#     }   
            
# """)