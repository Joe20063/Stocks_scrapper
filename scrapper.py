from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_stock(link, stocks):
    PATH = "/home/youssef/Downloads/chromedriver"

    driver = webdriver.Chrome(PATH)

    driver.get(link)

    # This will take the stocks price that you want.
    for stock in stocks:
	# This will take the search bar that we will write the stock in
        search_bar = driver.find_element_by_xpath("/html/body/c-wiz/div/div[3]/div[3]/div/div/div/div[1]/input[2]")

        # This will click the search bar and type the stock name in
	search_bar.click()
        search_bar.send_keys(stock)
        time.sleep(5)
        # This will take the link of stock from the search results and navigate to the stock page
	stock_link = driver.find_element_by_class_name("onRPD")
        stock_link.click()
        time.sleep(15)
        # This will take the stock price of the stock page and print it into the termainal
	stock_sallary = driver.find_element_by_class_name('kf1m0')
        print(f"{stock} in US Stock is: {stock_sallary.text}")
        # This will return it to the main web page
	driver.get(link)
        time.sleep(10)


