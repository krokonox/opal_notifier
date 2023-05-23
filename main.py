import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from telegram import Bot

# Set up Telegram bot
telegram_bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
bot = Bot(token=telegram_bot_token)

# Set up Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)

# Scraping function
def scrape_website():
    driver.get('https://example.com')  # Replace with your university website URL
    # Perform scraping and extract necessary information
    # ...

# Compare function
def compare_data(new_data):
    # Compare new data with previously stored data
    # ...

# Main loop
while True:
    # Scrape the website
    new_data = scrape_website()

    # Compare data to detect changes
    if compare_data(new_data):
        # Send notification
        bot.send_message(chat_id='YOUR_CHAT_ID', text='Changes detected!')

    # Wait for an hour before scraping again
    time.sleep(3600)
