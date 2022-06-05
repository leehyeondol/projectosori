# 이 파일 root 파일에 넣고 models.py와 연동해 주면 됨
# 수정 중인 코드 주석 처리하였음

from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "osori.settings")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

# outfit의 models.py에 맞게 아래 코드 수정

import django
django.setup()

from outfit.models import musinsa_model
#from .models import musinsa_model
musinsa = "https://www.musinsa.com/mz/brandsnap?p=1"

# headers = {
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}


def get_request(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_musinsa_images(soup):
    list_items = soup.select('div.articleImg>a>img')
    list_images = [i.attrs['src'] for i in list_items[:3]]
    return list_images

# 링크 스크래핑 함수


def get_musinsa_links(soup):
    list_items = soup.select('div.articleImg>a')
    list_links = ["https://www.musinsa.com" + i.attrs['href']
                  for i in list_items[:3]]

    return list_links

# 무신사 크롤링 함수


def get_musinsa_data():

    result = []
    i = 0
    soup = get_request(musinsa)
    list_links = get_musinsa_links(soup)
    list_images = get_musinsa_images(soup)

    for link, image in zip(list_links, list_images):
        i += 1

        musinsa_obj = {
            'musinsa_image': image,
            'musinsa_link': link,
            'musinsa_key': i
        }
        result.append(musinsa_obj)

    return result


if __name__ == '__main__':
    musinsa_data = get_musinsa_data()
    # mixxo_data = get_mixxo_data(get_request(mixxo))

    # musinsa object
    for item in musinsa_data:
        musinsa_model(musinsa_image=item['musinsa_image'],
                musinsa_link=item['musinsa_link'], musinsa_key=item['musinsa_key']).save()

