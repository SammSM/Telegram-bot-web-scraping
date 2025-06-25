import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time
import json
import os
import re


def parse_data(vehicle_type):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")


    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("https://auto.am/")

        vehicle_types_dict={
            'car': 'Մարդատար',
            'bus': 'Ավտոբուս',
            'truck': 'Բեռնատար',
            'moto': 'Մոտոտեխնիկա'
        }

        vehicle_dict={
            'car': [], 
            'bus': [],
            'truck': [],
            'moto': []
        }


        vehicles = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{vehicle_types_dict[vehicle_type]}')]"))
        )
        vehicles.click()

        driver.find_element(By.CSS_SELECTOR, "#search-btn").click()

        vehicle_list = driver.find_elements(By.XPATH, "//div[contains(@class, 'pad-top-6 pad-bot-6 makeflex makebetween')]")
        vehicle_list = vehicle_list[:min(11, len(vehicle_list))]

        for j in vehicle_list:
            model=j.find_element(By.CSS_SELECTOR, 'div.card-content > a > div > span').text
            vehicle_dict[vehicle_type].append(model)


        with open(f'{vehicle_type}.json', 'w', encoding="utf-8") as file:
            json.dump(vehicle_dict, file, ensure_ascii=False, indent=4)


        for i in range(0, len(vehicle_list)):
            
            vehicle_id =vehicle_list[i].get_attribute("innerHTML")
            match = re.search(r'<!--\s*ID:\s*(\d+)', vehicle_id)
            card = driver.find_element(By.ID, f"ad-{match.group(1)}")

            img = card.find_element(By.CSS_SELECTOR, "div.card-image a img")
            img_url = img.get_attribute("src")


            if img_url.startswith("/"):
                img_url = "https://auto.am/" + img_url

            response = requests.get(img_url)
            if response.status_code == 200:
                with open(f"{vehicle_type}/{i}.jpg", "wb") as f:
                    f.write(response.content)
            else:
                print("Error!")

    except Exception as ex:
        print(ex.__class__.__name__)
    finally:
        driver.close()
        driver.quit()
    