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
    soup = BeautifulSoup(html, 'lxml')

    # Find all div elements with class 'chakra-text css-18zq59p' and extract text content
    chakra_text_elements = soup.find_all('p', class_='chakra-text')
    paragraph_list = [text_content.get_text(strip=True) for text_content in chakra_text_elements]
    elements = soup.find_all(class_='css-46p1lt')
    text_list = []
  
    # Extract text from each div and append to the list
    for div_element in elements:
        div_text = '\n'.join([p.get_text(strip=True) for p in div_element.find_all('p')])
        text_list.append(div_text)

    # Extract and print the text with HTML tags
    for element in elements:
        print(element.prettify())
    # Find all links within h2 elements with class 'chakra-heading'
    links = [a['href'] for h2 in soup.find_all('h2', class_='chakra-heading') for a in h2.find_all('a')]
    title = [link[10:] for link in links]
    # Create a list of complete URLs
    linkarray = ['https://aa-intergroup.org' + link for link in links]
    content_list = []
    # Return a dictionary containing the extracted data
    # return {'links': linkarray, 'posts': paragraph_list,'titles':title}
    for i in range (5):
        content_list.append({
            'link': linkarray[i],
            'title': title[i],
            'paragraph': elements[i],
        })
    return content_list
# Call the function with the URL and store the result in the 'content' variable
content = scrape_website('https://aa-intergroup.org/meetings/')
def home(request):
    # Pass the 'content' variable to the template
    return render(request, 'zoom/index.html', {'content':content})
