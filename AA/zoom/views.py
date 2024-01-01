from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = "https://aa-intergroup.org/meetings/"

# Set up a Selenium WebDriver (make sure to download the appropriate driver for your browser)
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Needed for headless mode in some environments
driver = webdriver.Chrome(options=options)
# Open the webpage
driver.get(url)
element_present = EC.presence_of_element_located((By.CSS_SELECTOR, '.chakra-heading'))
WebDriverWait(driver, timeout=10).until(element_present)

# Wait for the specific element to be present (adjust the timeout as needed)

# Get the HTML content after the page has loaded
html = driver.page_source

# Close the browser window
driver.quit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Print the entire HTML content of the webpage
links = [a['href'] for h2 in soup.find_all('h2', class_='chakra-heading') for a in h2.find_all('a')]

    # Save the links to a text file
with open('links_output.txt', 'w', encoding='utf-8') as file:
    for link in links:
        file.write('https://aa-intergroup.org'+link + '\n')
def home(request):
    return render(request, 'zoom/index.html')
# Create your views here.
