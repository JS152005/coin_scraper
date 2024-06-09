import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class CoinMarketCap:
    def __init__(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.base_url = "https://coinmarketcap.com/currencies/"
        self.timeout = 10  # seconds

    def get_coin_data(self, coin):
        url = f"{self.base_url}{coin}/"
        self.driver.get(url)
        data = {}
        try:
            # Wait for the page to load
            WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@class, "priceValue")]')))
            data['price'] = self.driver.find_element(By.XPATH, '//*[contains(@class, "priceValue")]').text
            data['price_change'] = self.driver.find_element(By.XPATH, '//*[contains(@class, "sc-15yy2pl-0 feeyND")]').text
            data['market_cap'] = self.driver.find_element(By.XPATH, '//*[contains(text(), "Market Cap")]/following-sibling::div').text
            data['market_cap_rank'] = self.driver.find_element(By.XPATH, '//*[contains(text(), "Market Cap Rank")]/following-sibling::div').text
            data['volume'] = self.driver.find_element(By.XPATH, '//*[contains(text(), "Volume 24h")]/following-sibling::div').text
            data['volume_rank'] = self.driver.find_element(By.XPATH, '//*[contains(text(), "Volume / Market Cap")]/following-sibling::div').text
            data['volume_change'] = self.driver.find_element(By.XPATH, '//*[contains(text(), "Volume 24h")]/following-sibling::div').text
            data['circulating_supply'] = self.driver.find_element(By.XPATH, '//*[contains(text(), "Circulating Supply")]/following-sibling::div').text
            data['total_supply'] = self.driver.find_element(By.XPATH, '//*[contains(text(), "Total Supply")]/following-sibling::div').text
            data['diluted_market_cap'] = self.driver.find_element(By.XPATH, '//*[contains(text(), "Fully Diluted Market Cap")]/following-sibling::div').text
            data['contracts'] = self._get_contracts()
            data['official_links'] = self._get_official_links()
            data['socials'] = self._get_social_links()
        except TimeoutException:
            data['error'] = 'Timeout error: page took too long to load'
        except Exception as e:
            data['error'] = str(e)
        return data

    def _get_contracts(self):
        contracts = []
        contract_elements = self.driver.find_elements(By.XPATH, '//*[contains(text(), "Contracts")]/following-sibling::div')
        for elem in contract_elements:
            contract = {
                "name": elem.find_element(By.TAG_NAME, 'span').text,
                "address": elem.find_element(By.TAG_NAME, 'a').text
            }
            contracts.append(contract)
        return contracts

    def _get_official_links(self):
        official_links = []
        link_elements = self.driver.find_elements(By.XPATH, '//*[contains(text(), "Official Links")]/following-sibling::ul/li')
        for elem in link_elements:
            link = {
                "name": elem.find_element(By.TAG_NAME, 'span').text,
                "link": elem.find_element(By.TAG_NAME, 'a').get_attribute('href')
            }
            official_links.append(link)
        return official_links

    def _get_social_links(self):
        social_links = []
        social_elements = self.driver.find_elements(By.XPATH, '//*[contains(text(), "Socials")]/following-sibling::ul/li')
        for elem in social_elements:
            link = {
                "name": elem.find_element(By.TAG_NAME, 'span').text,
                "url": elem.find_element(By.TAG_NAME, 'a').get_attribute('href')
            }
            social_links.append(link)
        return social_links