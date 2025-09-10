import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Function to scrape a website and return its HTML content
def scrape_website(website):
    print("Launchine chrome browser...")

    chrome_driver_path = r"C:\Users\uwabo\OneDrive\Documents\Portfolio Projects\Web Scraper\chromedriver\chromedriver-win64\chromedriver.exe"
    options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service=Service(
    #     chrome_driver_path), options=options)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()

# Function to extract the main content from the HTML
def extract_main_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    main_content = soup.body
    if main_content:
        return main_content.get_text(strip=True)
    else:
        return "No main content found."

# Function to clean the extracted main content
def clean_main_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content

# Function to split the DOM content into smaller chunks for easier processing
def split_dom_content(dom_content, max_length=5000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]
    st.write("Scraping completed.")