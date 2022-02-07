import time
import yaml
from selenium import webdriver


def main():
    conf = yaml.safe_load(open('config.yml'))
    USERNAME: str = conf['USERNAME']
    PASSWORD: str = conf['PASSWORD']
    BROWSER: str = conf['BROWSER']
    if USERNAME == 'yourusername' or PASSWORD == 'yourpassword':
        print('Set your credentials in the config.yml file.')
        input()
        return
    if BROWSER == 'firefox':
        driver = webdriver.Firefox(executable_path="geckodriver.exe")
    elif BROWSER == 'chrome':
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
    else:
        print('BROWSER must be set the chrome or firefox.')
        input()
        return
    driver.get("http://10.0.0.1/iclogin")
    try:
        driver.find_element_by_name('USERNAME').send_keys(USERNAME)
        driver.find_element_by_name('PASSWORD').send_keys(PASSWORD)
    except:
        pass
    driver.find_element_by_css_selector('input.gobutton').click()
    driver.get("http://10.0.0.1/mitm?id=68fd6f925fcc9356d6aaf4bee9db488403c5725c6797b4344335d39890d9f053Z6a61726564&location=https%3a%2f%2fduckduckgo.com%2f%3fq%3dnlIUASndoasnfnasfas%26t%3dvivaldi%26atb%3dv203-1")
    driver.find_element_by_xpath('/html/body/div[2]/form/input[2]').click()
    driver.close()


main()
