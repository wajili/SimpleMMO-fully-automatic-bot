import undetected_chromedriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException
import requests
from requests.structures import CaseInsensitiveDict
import matplotlib.pyplot as plt
from torch.autograd import Variable
from PIL import Image
import os
import utils
import torchvision.transforms as transforms
import numpy as np
import torch
import torch.nn as nn
import verifier
import cv2

TEMP_PATH = "./temporary"
UNKNOWN_IMAGE_PATH = "./unknown"

def main():
    driver = get_driver()
    driver.get("https://web.simple-mmo.com/login")
    email = input("email:")
    password = input("password:")
    assert "SimpleMMO" in driver.title
    login(driver,email,password)
    travel(driver)
    take_step(driver)


def login(driver,email,password):
    element = driver.find_element(By.NAME, "email")
    element.clear()
    element.send_keys(email)
    element = driver.find_element(By.NAME, "password")
    element.clear()
    element.send_keys(password)
    element.send_keys(Keys.RETURN)


def get_driver():
    chrome_options = Options()
    chrome_options.binary_location = 'home/wjl/Downloads/chrome/Linux_x64_1097615_chrome-linux/chrome-linux/chrome'
    #chrome_options.add_experimental_option("binary_location", 'home/wjl/Downloads/chrome/Linux_x64_1097615_chrome-linux/chrome-linux/chrome')
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver
    # assert "No results found." not in driver.page_source
    # driver.close()


def travel(driver):
    driver.get("https://web.simple-mmo.com/travel")
    assert "Travel" in driver.title


def take_step(driver):
    assert "Travel" in driver.title

    while True:
        element = driver.find_element(By.ID, "step_button")
        element.click()
        time.sleep(2)
        not_machine(driver)
        not_machine2(driver)
        attack(driver)
        #wave(driver)
        collect(driver)

def store_images(driver):
    img_dir = os.listdir(FILE_PATH)
    for img_name in img_dir:
        current_time = time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime())
        img = cv2.imread(os.path.join(TEMP_PATH, "/", img_name))
        cv2.imwrite(UNKNOWN_IMAGE_PATH + "/" + current_time + ".png", img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        time.sleep(2)
                
                
def not_machine(driver):
    try:
        driver.find_element(By.LINK_TEXT, '"pesky machine"').click()
        #a=input('sb')
        for counter in range(2):
            try:
                time.sleep(2)
                main_window = driver.window_handles[0]
                bot_window = driver.window_handles[1]
                driver.switch_to.window(bot_window)
                time.sleep(2)

                assert "Player Verification" in driver.title
                es1 = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div/div[3]/div[1]/img")
                es2 = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div/div[3]/div[2]/img")
                es3 = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div/div[3]/div[3]/img")
                es4 = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div/div[3]/div[4]/img")
                es1.screenshot(os.path.join(TEMP_PATH, "/", "img1.png"))
                es2.screenshot(os.path.join(TEMP_PATH, "/", "img2.png"))
                es3.screenshot(os.path.join(TEMP_PATH, "/", "img3.png"))
                es4.screenshot(os.path.join(TEMP_PATH, "/", "img4.png"))
                time.sleep(20)
                element = driver.find_element(By.CSS_SELECTOR, ".text-2xl")
                item = element.text.lower()
                prediction = verifier.simmmover("./temporary", item)

                if prediction == 'img1':
                    es1.click()
                elif prediction == 'img2':
                    es2.click()
                elif prediction == 'img3':
                    es3.click()
                elif prediction == 'img4':
                    es4.click()
            
                time.sleep(3)
                try:
                    driver.find_element(By.LINK_TEXT, "Retry").click()
                    current_time = time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime())
                    print("failed####" + " " + item + " " + current_time)
                    store_images(driver)
                    if counter >= 1:
                        b = input('sb')
                    continue
            
                except NoSuchElementException:
                    driver.find_element(By.ID, "swal2-title")
                    driver.close()
                    driver.switch_to.window(main_window)
                    #store_images(driver)
                    current_time = time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime())
                    print("success!!!" + " " + current_time)
                    return
                    
            except NoSuchElementException:
                continue
    except NoSuchElementException:
        return


def not_machine2(driver):

    try:
        driver.find_element(By.LINK_TEXT, "Perform Verification").click()
        #a=input('sb')
        for counter in range(2):
            try:
                time.sleep(2)
                main_window = driver.window_handles[0]
                bot_window = driver.window_handles[1]
                driver.switch_to.window(bot_window)
                time.sleep(2)

                assert "Player Verification" in driver.title
                es1 = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div/div[3]/div[1]/img")
                es2 = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div/div[3]/div[2]/img")
                es3 = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div/div[3]/div[3]/img")
                es4 = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div/div[3]/div[4]/img")
                es1.screenshot(os.path.join(TEMP_PATH, "/", "img1.png"))
                es2.screenshot(os.path.join(TEMP_PATH, "/", "img2.png"))
                es3.screenshot(os.path.join(TEMP_PATH, "/", "img3.png"))
                es4.screenshot(os.path.join(TEMP_PATH, "/", "img4.png"))
                time.sleep(20)
                element = driver.find_element(By.CSS_SELECTOR, ".text-2xl")
                item = element.text.lower()
                prediction = verifier.simmmover("./temporary", item)

                if prediction == 'img1':
                    es1.click()
                elif prediction == 'img2':
                    es2.click()
                elif prediction == 'img3':
                    es3.click()
                elif prediction == 'img4':
                    es4.click()
            
                time.sleep(3)
                try:
                    driver.find_element(By.LINK_TEXT, "Retry").click()
                    current_time = time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime())
                    print("failed####" + " " + item + " " + current_time)
                    store_images(driver)
                    if counter >= 1:
                        b = input('sb')
                    continue
            
                except NoSuchElementException:
                    driver.find_element(By.ID, "swal2-title")
                    driver.close()
                    driver.switch_to.window(main_window)
                    #store_images(driver)
                    current_time = time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime())
                    print("success!!!" + " " + current_time)
                    return
                    
            except NoSuchElementException:
                continue
    except NoSuchElementException:
        return

def not_machine3(driver):
    try:
        deter = 0
        driver.find_element(By.LINK_TEXT, "Press here to verify").click()
        #a=input('sb')
        for counter in range(2):
            try:
                time.sleep(2)
                main_window = driver.window_handles[0]
                bot_window = driver.window_handles[1]
                driver.switch_to.window(bot_window)
                time.sleep(2)

                assert "Player Verification" in driver.title
                es1 = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div/div[3]/div[1]/img")
                es2 = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div/div[3]/div[2]/img")
                es3 = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div/div[3]/div[3]/img")
                es4 = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div/div[3]/div[4]/img")
                es1.screenshot(os.path.join(TEMP_PATH, "/", "img1.png"))
                es2.screenshot(os.path.join(TEMP_PATH, "/", "img2.png"))
                es3.screenshot(os.path.join(TEMP_PATH, "/", "img3.png"))
                es4.screenshot(os.path.join(TEMP_PATH, "/", "img4.png"))
                time.sleep(20)
                element = driver.find_element(By.CSS_SELECTOR, ".text-2xl")
                item = element.text.lower()
                prediction = verifier.simmmover(TEMP_PATH, item)

                if prediction == 'img1':
                    es1.click()
                elif prediction == 'img2':
                    es2.click()
                elif prediction == 'img3':
                    es3.click()
                elif prediction == 'img4':
                    es4.click()
            
                time.sleep(3)
                try:
                    driver.find_element(By.LINK_TEXT, "Retry").click()
                    current_time = time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime())
                    print("failed####" + " " + item + " " + current_time)
                    store_images(driver)
                    if counter >= 1:
                        b = input('sb')
                    continue
            
                except NoSuchElementException:
                    driver.find_element(By.ID, "swal2-title")
                    driver.close()
                    driver.switch_to.window(main_window)
                    driver.get("https://web.simple-mmo.com/travel")
                    time.sleep(2)
                    #store_images(driver)
                    deter = 1
                    current_time = time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime())
                    print("success!!!" + " " + current_time)
                    return deter
                    
            except NoSuchElementException:
                continue
    except NoSuchElementException:
        return deter


#def wave(driver):
#    try:
#        element = driver.find_element("xpath",
#            "/html/body/div[1]/div[3]/main/div[2]/div/div[2]/div/div/div[6]/div[1]/div/div[2]/div/div[3]/span/button"
#        )
#        element.click()
#        attack_mob(driver)
#    except NoSuchElementException:
#        return

def attack(driver):
    try:
        element = driver.find_element("xpath",
            "/html/body/div[1]/div[3]/main/div[2]/div/div[2]/div/div/div[6]/div[1]/div/div[2]/div/span[2]/a[1]"
        )
        element.click()
        attack_mob(driver)
    except NoSuchElementException:
        return

def collect(driver):
    try:
        element = driver.find_element("xpath",
            "/html/body/div[1]/div[3]/main/div[2]/div/div[2]/div/div/div[6]/div[1]/div/div[2]/div/div[2]/button"
        )
        element.click()
        collect_mob(driver)
    except NoSuchElementException:
        return

def collect_mob(driver):
    #assert "Attacking" in driver.title

    while True:

        try:
            time.sleep(2)
            driver.find_element(By.ID, "crafting_button").click()
        except NoSuchElementException:
            return

def attack_mob(driver):
    #assert "Attacking" in driver.title
    element = driver.find_element("xpath", "/html/body/div[1]/div[3]/main/div[2]/div/div[2]/div[2]/button[1]")

    while True:

        try:
            time.sleep(2)
            deter = not_machine3(driver)
            if deter == 1:
                return
            driver.find_element(By.LINK_TEXT, "End Battle").click()
            break
        except NoSuchElementException:
            element.click()
                



if __name__ == "__main__":
    main()
