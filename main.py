import time
import datetime
import argparse
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# To parse the arguments
def getOptions(arg=None):
    if arg is None:
        arg = sys.argv[1:]
    parser = argparse.ArgumentParser(
        description="This bot helps users to mass report accounts with clickbaits or objectionable material.")
    parser.add_argument("-u", "--username", type=str, default="", help="Login Username.")
    parser.add_argument("-s", "--sleep", type=str, default="", help="Set the sleep time")
    parser.add_argument("-p", "--password", type=str, default="", help="Login Password")
    parser.add_argument("-b", "--bot", type=str, default="", help="The user you want to report.")
    parser.add_argument("-r", "--report", type=str, default="", help="The type of report you want.")
    parser.add_argument("-a", "--amount", type=str, default="", help="The amount of reports you want.")

    options = parser.parse_args(arg)

    return options


args = getOptions()

bot = args.bot
username = args.username
password = args.password
sleep = args.sleep
report = args.report
amount = args.amount


if username == "":
    username = input("Username: ")

if password == "":
    password = input("Password: ")

if sleep == "":
    sleep = int(input("Sleep Delay: "))

if bot == "":
    print("Please use @ before the username!")
    bot = input("The person you want to report: ")

if report == "":
    print("1 = Spam \n"
          "2 = Self Injury")
    report = int(input("Choose the type of report: "))

if amount == "":
    print("Please use an integer.")
    amount = int(input("How many times do you want it to report: "))

version = '1.2.3'

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()
# waits 30 seconds
driver.implicitly_wait(30)

# types the username in one character at a time with a pace of 0.05 seconds - username text box
for character in username:
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(character)
    time.sleep(0.05)

# types the password in one character at a time with a pace of 0.05 seconds - password text box
for character in password:
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(character)
    time.sleep(0.05)

# log in button
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
print(f"Logged in at {datetime.datetime.now()}")
# not now button
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, 'button.aOOlW:nth-child(2)').click()
time.sleep(1)
# search bar (top)
driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(bot)
time.sleep(sleep)
driver.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div['
                              '1]/a/div/div[2]/div[1]/div/div').click()
time.sleep(sleep)

# reporting the account
if amount <= 1:
    if report == 1:
        time.sleep(sleep)
        driver.find_element(By.CSS_SELECTOR, 'button.b5k4S:nth-child(1) > div:nth-child(1) > div:nth-child(1)').click()
        time.sleep(sleep)
        driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div/div/div[4]/button').click()
        print(f"Reported {username} with Spamming.")
    elif report == 2:
        time.sleep(sleep)
        driver.find_element(By.CSS_SELECTOR, 'button.b5k4S:nth-child(3) > div:nth-child(1) > div:nth-child(1)').click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'button.sqdOP:nth-child(5)').click()
        time.sleep(sleep)
        driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div/div/div[4]/button').click()
        print(f"Reported {username} with Self Injury.")
    else:
        print("Your report number did not equal 1 or 2.")
        driver.close()

# looping the reports
if amount >= 2:
    for integer in range(amount):
        if report == 1:
            time.sleep(sleep)
            driver.find_element(By.CSS_SELECTOR,
                                '.VMs3J > button:nth-child(1) > div:nth-child(1) > svg:nth-child(1)').click()
            time.sleep(sleep)
            driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/button[3]').click()
            time.sleep(sleep)
            driver.find_element(By.XPATH,
                                '/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
            time.sleep(sleep)
            driver.find_element(By.XPATH,
                                '/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]').click()
            time.sleep(sleep)
            driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]').\
                click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div/div/div[4]/button').click()
            time.sleep(sleep)
            print(f"Reported {username} with Spamming. Reported {amount} times.")
        elif report == 2:
            time.sleep(sleep)
            driver.find_element(By.CSS_SELECTOR,
                                '.VMs3J > button:nth-child(1) > div:nth-child(1) > svg:nth-child(1)').click()
            time.sleep(sleep)
            driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/button[3]').click()
            time.sleep(sleep)
            driver.find_element(By.XPATH,
                                '/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[2]/div').click()
            time.sleep(sleep)
            driver.find_element(By.XPATH,
                                '/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[1]/div/div[1]').click()
            time.sleep(sleep)
            driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/div/div/div/div[3]/button[3]/div/div[1]').\
                click()
            time.sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/div/div/button').click()
            time.sleep(sleep)
            driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div/div/div[4]/button').click()
            time.sleep(sleep)
            print(f"Reported {username} with Self Injury. Reported {amount} times.")
        else:
            print("Your report number did not equal 1 or 2.")
            driver.close()

driver.close()
print(f"Created by Abaios under the MIT Public License. Instagram Report Bot version {version}.")
