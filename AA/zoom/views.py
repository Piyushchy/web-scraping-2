from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def scrape_website(url):
    # Set up a Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    # Open the webpage
    driver.get(url)
    
    # Wait for the presence of 'chakra-heading'
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.chakra-heading'))
    WebDriverWait(driver, timeout=10).until(element_present)

    # Get the HTML content after the page has loaded
    html = driver.page_source

    # Close the browser window
    driver.quit()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all div elements with class 'chakra-text css-18zq59p' and extract text content
 # Find all div elements with class 'chakra-text css-18zq59p' and extract text content
    chakra_text_elements = soup.find_all('p', class_='chakra-text')

    # Save the text to a text file
    with open('chakra_text_contents_output.txt', 'w', encoding='utf-8') as file:
        for text_content in chakra_text_elements:
            file.write(text_content.get_text(strip=True) + 'lol')
       

    # Find all links within h2 elements with class 'chakra-heading'
    links = [a['href'] for h2 in soup.find_all('h2', class_='chakra-heading') for a in h2.find_all('a')]

    # Save the links to a text file
    with open('links_output.txt', 'w', encoding='utf-8') as file:
        for link in links:
            file.write('https://aa-intergroup.org' + link + '\n')

# Call the function with the URL
scrape_website("https://aa-intergroup.org/meetings/")

def home(request):
    return render(request, 'zoom/index.html')
# Create your views here.
