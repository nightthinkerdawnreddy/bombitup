from selenium import webdriver
import time 
from selenium.common.exceptions import NoSuchElementException
options = webdriver.ChromeOptions()
options.headless=True
def flipkart(number):

    driver = webdriver.Chrome(executable_path="/home/bhas/Desktop/djangoprojects/bombitup/send/chromedriver",options=options)
    driver.get("https://www.flipkart.com/")
    time.sleep(2)
    #number='8639697489'
    mobile=driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
    mobile.send_keys(number)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[5]/button").click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button").click()
        time.sleep(2)
    except NoSuchElementException:
        print("clicked")
        time.sleep(5)
    driver.close()
def dominos(number):
    driver = webdriver.Chrome(executable_path="/home/bhas/Desktop/djangoprojects/bombitup/send/chromedriver",options=options)
    driver.get("https://pizzaonline.dominos.co.in/?#!/customer/login/")
    time.sleep(2)
    #number='9014562586'
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div/div[3]/div[2]/div[1]/div[2]').click()
    time.sleep(2)
    numberfield=driver.find_element_by_name("loginNumber")
    numberfield.send_keys(number)
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[1]/div/div[3]/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input').click()
    time.sleep(2)
    print("yes it is working")
    driver.close()
def netmeds(number):
    driver = webdriver.Chrome(executable_path="/home/bhas/Desktop/djangoprojects/bombitup/send/chromedriver")
    driver.get("https://www.netmeds.com/customer/account/login")
    time.sleep(2)
    #number = "9014562586"
    mobile = driver.find_element_by_id("loginfirst_mobileno")
    mobile.send_keys(number)
    driver.find_element_by_xpath('//*[@id="app"]/main/app-login/div[1]/div/div[1]/div[2]/div/div[1]/form/div[2]/button[1]').click()
    time.sleep(5)
    driver.close()
def appolo(number):
    driver = webdriver.Chrome(executable_path="/home/bhas/Desktop/djangoprojects/bombitup/send/chromedriver",options=options)
    driver.get("https://www.apollo247.com/")
    #driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[1]/img").click()
    driver.find_element_by_id('loginPopup').click()
    time.sleep(2)
    #number="9014562586"
    numberelement=driver.find_element_by_name("mobileNumber")
    numberelement.send_keys(number)
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div/div/form/div[2]/button').click()
    time.sleep(2)
    driver.close()
def kartra():
    driver = webdriver.Chrome(executable_path="/home/bhas/Desktop/djangoprojects/bombitup/send/chromedriver",options=options)
    driver.get("https://home.kartra.com/index#utm_source=aff_link&utm_medium=affiliate&utm_content=14-day_trial&utm_campaign=product_index")

def mainfunction(number,noofmessages):
    i = 0
    while i <= noofmessages:
        flipkart(number)
        i += 1
        if i<=noofmessages:
            dominos(number)
            i += 1
        if i<= noofmessages:
            netmeds(number)
            i += 1
        if i<= noofmessages:
            appolo(number)
netmeds("9542279921")


    






