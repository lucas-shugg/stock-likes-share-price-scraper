############################################################################


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def getnyseSoup(ticker):
    url = "https://au.finance.yahoo.com/quote/" + ticker + "?p=" + ticker + "&.tsrc=fin-srch"
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    # Try getting xpath element if not specified scroll and wait as necessary
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "")))
    except:
        pass
    finally:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

    return soup

def getSharePrice(nyse_soup):
    sharePrice = nyse_soup.find_all("span", class_= "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")


    sharePrice = [_.text for _ in sharePrice]
    sharePrice = sharePrice[0]

    print("The share price is", sharePrice)

    return float(sharePrice)





if __name__ == '__main__':

    # Page name is the string in the ur of page after www.facebook.com/
    pageName = "TESLAOfficialPage"
    soup = getnyseSoup("https://au.finance.yahoo.com/quote/TSLA?p=TSLA&.tsrc=fin-srch")

    print(getSharePrice(soup))


#############################################################


