from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Selenium configuration
options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')

# Don't open chrome each time I run the code...
options.add_argument('--headless')

service = Service("C:/Program Files/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# base url for traversing categories...
base_url_trendyol = 'https://www.trendyol.com/en/'


def TrendyolParser():
    # for fetching male and female links two different branches of links
    male_categories = [
        'Sweaters',
        'Cardigans',
        'Shirts',
        'Coats',
        'Jeans',
        'Sweatsuits',
        'Pajama sets',
        'Shoes & Accessories',
        'Swimshorts',
        'Sweatshirts',
        'T-Shirts',
        'Blazers',
        'Jackets',
        'Pants',
        'Sweatpants',
        'Boxers',
        'Sportswear',
    ]

    # links for male and female clothing

    url_male = 'https://www.trendyol.com/en/campaign/list/men'
    url_female = 'https://www.trendyol.com/en/campaign/list/women'

    driver.get(url_male)

    time.sleep(1)

    found = driver.find_elements(by=By.CLASS_NAME, value="subcategory-items")

    page_source = driver.page_source

    # Requirement -> pip install lxml, if you run into problems here
    soup = BeautifulSoup(page_source, 'html.parser')

    subcategory_items = soup.find_all('div', class_='category-menu-wrapper')

    clothing_subsection = subcategory_items[1]

    clothing_hrefs = clothing_subsection.find_all('a')

    clothing_links = [i['href'] for i in clothing_hrefs if not str(i['href']).startswith("sr?") and not i['href'] == '']

    time.sleep(1)

    # Check it with the selenium here again. Ye cool.
    driver.get(base_url_trendyol + clothing_links[0])
    # Have some rest..
    time.sleep(5)





def boyner_parser(link,file_count):

    driver.get(link)
    time.sleep(1)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    total_products_num = soup.find_all("span", class_='grey')[-1].extract()

    total_products_num = int(total_products_num.get_text().replace("(","").replace(")",""))
    print(total_products_num)
    print(total_products_num//45)

    # 45 products in 1 page.
    for i in range(1, total_products_num//45 + 2):

        driver.get(link + str(i))
        print(link + str(i))
        time.sleep(1)
        page_source = driver.page_source

        # Requirement -> pip install lxml, if you run into problems here
        soup = BeautifulSoup(page_source, 'html.parser')

        product_list_depot = soup.find_all("div", class_='imgDepot')
        print(f"------------------------PAGE {i}------------------------")


        file_name = str(file_count) + '.txt'
        with open(file_name, 'a') as f:
            for item in product_list_depot:
                for img_section in item.findAll('img'):
                    f.write(img_section['data-imgsrc'])
                    f.write('\n')

boyner_url_list = [
    'https://www.boyner.com.tr/erkek-t-shirt-modelleri-c-200107/',
    'https://www.boyner.com.tr/erkek-gomlek-modelleri-c-200104/',
    'https://www.boyner.com.tr/erkek-pantolon-modelleri-c-200105/',
    'https://www.boyner.com.tr/erkek-jean-c-200109/',
    'https://www.boyner.com.tr/erkek-ceket-yelek-modelleri-c-200103/',
    'https://www.boyner.com.tr/erkek-sort-c-3302071/',
]

