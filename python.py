import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import telebot

# Токен вашего бота
bot_token = '6410884762:AAHdIxXaJtvkYwAjR48hPHB5Wrc5KivQy3c'
bot = telebot.TeleBot(bot_token)

# Функция, которая выполняет ваш код при команде /start
@bot.message_handler(commands=['start'])
def start(message):
    # Весь ваш код здесь
    credentials_file_path = 'data.txt'

    with open(credentials_file_path, 'r') as file:
        lines = file.readlines()
        email = lines[0].strip()
        password = lines[1].strip()

    # Создание опций для включения headless mode
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')  # Добавлено для устранения проблемы с отображением окна браузера

    # Использование опций при создании объекта WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://id2.rtu.lv/openam/UI/Login?module=LDAP&locale=lv")

    email_input = driver.find_element(By.NAME, "IDToken1")
    email_input.send_keys(email)

    password_input = driver.find_element(By.NAME, "IDToken2")
    password_input.send_keys(password)

    submit_button = driver.find_element(By.NAME, "Login.Submit")
    submit_button.click()

    student_button = driver.find_element(By.XPATH, "//span[@class='portal-tabGroup-label' and text()='Studentiem']")
    student_button.click()

    estudiju_link = driver.find_element(By.XPATH, "//a[@href='https://estudijas.rtu.lv/index.php']")
    estudiju_link.click()

    # Wait for the page to load
    time.sleep(1)

    # Get the page source after the redirect
    page_source = driver.page_source

    # Use BeautifulSoup to parse the page source
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the relevant elements
    event_list_items = soup.find_all('li', class_='media')

    # Iterate through the items and extract the information
    for item in event_list_items:
        # Check if the elements are present before accessing their attributes
        course_element = item.find('small', class_='text-muted')
        activity_element = item.find('h6')

        if course_element and activity_element:
            course_name = course_element.text.strip()
            activity_title = activity_element.text.strip()
            message_text = f"Course: {course_name}\nActivity Title: {activity_title}\n"
            # Отправляем сообщение боту
            bot.send_message(message.chat.id, message_text)

    # Close the browser
    driver.quit()

# Запуск бота
bot.polling()