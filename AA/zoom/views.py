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
print(soup.prettify())
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

def home(request):
    return render(request, 'zoom/index.html')
# Create your views here.
