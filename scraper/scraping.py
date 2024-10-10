from scraper.features import *
import pandas as pd
import requests
from bs4 import BeautifulSoup
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import time

def get_all_links():
    '''
    Will download the saved csv with all links and return a df containing 1 column with all links.
    '''
    all_links = pd.read_csv("data/import_links_houses_for_sale.csv")
    all_links.columns = ["houses & appartments"]  # Modified as there was a space at the end of the string

    return(all_links)

def create_df():
    '''
    Will create and return an empty dataframe with the needed columns
    '''

    columns = ["property_ID",
                "locality_name",
                "postal_code",
                "price",
                "type_of_property",
                "subtype_of_property",
                "type_of_sale",
                "nr_or_rooms",
                "living_area",
                "equiped_kitchen",
                "furnished",
                "open_fire",
                "terrace",
                "garden",
                "nr_of_facades",
                "swimming_pool",
                "state_of_building"]

    return pd.DataFrame(columns=columns)

def get_df(df, urls):
    '''
    Will loop through all the links in the dataframe and get the info per accommodation. It will return the df.
    '''
    immo_df = df

    # loop through the rows using iterrows()
    for index, row in urls.iterrows():
        scraped_dict = get_scraped_dict(row['houses & appartments'])

        row_data = add_features(scraped_dict, row['houses & appartments'])

        immo_df = immo_df._append(row_data, ignore_index=True)

    return immo_df


def  get_scraped_dict(url):
    '''
    Will get all info from a given url and return a dictionally with all this info. Return is all info stated in a list on the page on index 0 and the Immmowebcode on index 1.
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    text_blocks = soup.find_all("div", class_="text-block")

    ths_list = []
    tds_list = []
    feature_dict = {}

    for text_block in text_blocks:
        trs = text_block.find_all("tr")

        for tr in trs:
            if tr.find("th") != None and tr.find("td") != None:
                ths_list.append(tr.find("th").renderContents().strip().decode('UTF-8'))
                tds_list.append(tr.find("td").renderContents().strip().decode('UTF-8'))


    for i in range(0, len(tds_list)):
        feature_dict[ths_list[i]] = tds_list[i]

    # get alternative info which is elsewhere on the page
    property_ID = soup.find("div", class_="classified__header--immoweb-code")

    return [feature_dict, int(property_ID.text.split(": ")[1].strip())]


def add_features(data_list, url):
    data = data_list[0]

    if 'Aantal lijfrentetrekkers' in data:
        return None

    feature_dict = {}

    feature_dict["property_ID"] = data_list[1]

    feature_dict["locality_name"] = locality_name(data)

    feature_dict["postal_code"] = postal_code(data)

    feature_dict["price"] = price(data)

    feature_dict["type_of_property"] = type_of_property(url)

    feature_dict["subtype_of_property"] = subtype_of_property(url)

    feature_dict["type_of_sale"] = type_of_sale(data)

    feature_dict["nr_or_rooms"] = nr_or_rooms(data)

    feature_dict["living_area"] = living_area(data)

    feature_dict["equiped_kitchen"] = equiped_kitchen(data)

    feature_dict["furnished"] = furnished(data)

    feature_dict["open_fire"] = open_fire(data)

    feature_dict["terrace"] = terrace(data)

    feature_dict["garden"] = garden(data)

    feature_dict["nr_of_facades"] = nr_of_facades(data)

    feature_dict["swimming_pool"] = swimming_pool(data)

    feature_dict["state_of_building"] = state_of_building(data)

    return feature_dict










# Ignore below code: due to the split of my hard drive I didn't manage to get Selenium working. I might get back to it.

def accept_cookie(self):
    # options = Options()

    # #options.add_argument("--headless")
    # #options.add_argument("--window-size=1980,1020")
    print('stap 0')
    browser = webdriver.Chrome()
    print('stap 1')
    # #--| Parse or automation
    # url = "https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=1&orderBy=relevance"
    # print("stap 2")
    # browser.get(url)
    # print("stap 3")
    # # time.sleep(3)
    # # # Use BeautifulSoup
    # # soup = BeautifulSoup(browser.page_source, 'lxml')
    # # title = soup.find('h1', class_="page-title list-title ng-binding")
    # # print(title.text)
    # # print('-' * 40)
    # # # Use Selenium
    # # info = browser.find_elements_by_xpath("//div[@class='dir-property-list']//div[1]//div[1]//div[1]")
    # # print(info[0].text)

    # import webdriver_manager
    # from selenium.webdriver.chrome.service import Service
    # from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    # from selenium.webdriver.chrome.options import Options
    # from webdriver_manager.chrome import ChromeDriverManager

    # service = Service(ChromeDriverManager().install())
    # options = Options()
    # options.add_argument("--log-level=ALL")
    # caps = DesiredCapabilities.CHROME
    # caps['loggingPrefs'] = {'browserName': 'chrome'}

    # driver = webdriver.Chrome(service=service, options=options, desired_capabilities=caps)
    # selenium_grid_url = "http://198.0.0.1:4444/wd/hub"
    # capabilities = DesiredCapabilities.CHROME.copy()
    # capabilities['platform'] = "WINDOWS"
    # capabilities['version'] = "10"

    # Instantiate an instance of Remote WebDriver with the desired capabilities.
    # driver = webdriver.Remote(desired_capabilities=capabilities,
                            # command_executor=selenium_grid_url)
    print('passed')



# def get_urls_from_page(self, page, property_type):
#     url = f"https://www.immoweb.be/nl/zoeken/{property_type}/te-koop?countries=BE&page={page}&orderBy=newest"

#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, "html.parser")
#     print(soup.find_all(class_="card--result__title"))
#     # return soup
