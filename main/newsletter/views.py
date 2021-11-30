# from django.shortcuts import render

# def newspage(request):
#     return render(request, 'template.html')

# # 크롤링 파트
# import os 
# from urllib.parse import urlparse 
# import requests 
# from bs4 import BeautifulSoup 
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', "main.settings") 
# import django 
# django.setup()
# from newsletter.models import NewsData
# #pip install bs4 필요

# def health_news(): 
#     headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.52 Whale/3.12.129.29 Safari/537.36"}
#     result = [] 
#     url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=103&sid2=241' 
#     req = requests.get(url, headers=headers) 
#     html = req.text 
#     status = req.status_code
#     can_run = req.ok
#     soup = BeautifulSoup(html, 'html.parser') 
#     web_page_url_root = "https://news.naver.com/" 
#     news_list = soup.select( 
#         'main_content > div.list_body.newsflash_body > ul.type06_headline > li:nth-child(1) > dl > dt:nth-child(2) > a'    
#     )
#     global title_list, url_list
#     result_list = []
#     url_list = []
#     for news in news_list:
#         i = 0
#         result_list[i] = news.text
#         result_list[i+10] = news.get('href')
#         i += 1
#         if i==10: break
#     return result_list
# if __name__ == '__main__':
#     health_news()
# print(health_news()[0])