# Healthkku  
 > 코로나-19로 인해 헬스장에 가지 못하거나 시간이 없어 운동을 하지 못하는 사람들을 위해 개발한 홈트레이닝 웹사이트입니다.  
 > 이 프로젝트는 MIT 라이센스 조항에 따라 라이선스가 부여됩니다.  

# 구현 과정
이 웹서비스는 크게 세 파트로 나뉘는데,
필요한 운동을 골라 영상을 보며 따라할 수 있는 workout 페이지,
운동 목적과 적정 열량에 따라 식단을 구분해서 보여주는 diet 페이지,
건강 관련 뉴스를 크롤링해서 보여주는 news 페이지로,
각각의 페이지의 html template을 만들어 정보를 텍스트, 이미지 및 영상 미디어로 담고 django를 통해 url 연결, 페이지 간의 이동을 구현했다.
 
## 사용방법:   
### visual studio code  
terminal에서 django 설치 후 manage.py가 있는 디렉토리로 이동하고 아래의 코드를 이용해 페이지 실행
```
python -m pip install django
python manage.py runserve
```   

먼저 메인페이지에 접속하여 회원가입 절차를 진행한다. 상단의 nav bar를 보면 workout, diet, news, 총 세가지의 카테고리가 존재한다.   
 
 workout 페이지에서는 본인의 운동능력 수준에 맞게 루틴을 선택할 수 있다. 또한, 하단에는 가장 기초적인 운동인 팔굽혀펴기, 플랭크, 스쿼트를 배울 수 있는 영상이 존재한다.  
  
 diet 페이지에서는 다이어트를 위해 적절한 식단을 제공한다. 버튼을 누르면 식단에 대한 상세한 정보가 제공된다.  

 news 페이지에서는 최근의 유용한 건강정보를 모아 헬스 뉴스 레터를 제공한다.  




## Purpose  

## Screenshot  
![image](https://user-images.githubusercontent.com/80010823/143768986-71da4e8a-80e8-49af-98ab-fa5d935079ed.png)  

## Demo Video Link  

