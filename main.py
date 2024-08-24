import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def take_full_page_screenshot(url, output_file):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")

    # Initialize WebDriver with WebDriver Manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the webpage
        driver.get(url)

        # Give the page some time to fully load
        time.sleep(2)  # Adjust if necessary

        # Set the window size to the full page height
        total_height = driver.execute_script("return document.body.scrollHeight")
        driver.set_window_size(1920, total_height)

        # Take the screenshot
        driver.save_screenshot(output_file)
        print(f"Screenshot saved to {output_file}")

    finally:
        # Close the browser
        driver.quit()

def main():
    # Setup command-line argument parsing
    parser = argparse.ArgumentParser(description="Take a full-page screenshot of a webpage.")
    parser.add_argument("url", help="The URL of the webpage to capture.")
    parser.add_argument("output_file", help="The filename to save the screenshot as.")
    
    args = parser.parse_args()

    # Take the screenshot
    take_full_page_screenshot(args.url, args.output_file)

if __name__ == "__main__":
    main()
