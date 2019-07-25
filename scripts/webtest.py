from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd

options = Options()
options.headless = True
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
#options.add_argument('--disable-dev-shm-usage')
# for loop starts
df = pd.read_csv("files/northkorea_kp.csv")
value = df['host'].tolist()
pageload = open('ubuntu_northkorea_pl.txt', 'w')
driver = webdriver.Firefox()
for i in value:
    #hyperlink = "https://dns.brokelings.com/dns-query?name={}&record=A".format(i)
    hyperlink = "https://{}".format(i)
    #driver = webdriver.Chrome(chrome_options=options)
    #driver = webdriver.Firefox(options=options)
    driver.get(hyperlink)

    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    domComplete = driver.execute_script("return window.performance.timing.domComplete")
    loadeventEnd = driver.execute_script("return window.performance.timing.loadEventEnd")

    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart
    pageloadPerformance_calc = loadeventEnd - navigationStart

    #print("Back End: %s" % backendPerformance_calc)
    #print("Front End: %s" % frontendPerformance_calc)
    print("Page Load: %s" % pageloadPerformance_calc)
    #print(loadeventEnd)
    pageload.write("{},{},{},{}\n".format(i, pageloadPerformance_calc, backendPerformance_calc, frontendPerformance_calc))
driver.quit()
# for loop ends
