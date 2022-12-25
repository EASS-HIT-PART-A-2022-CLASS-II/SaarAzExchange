# Exchange Rates API
aplication for currency exchange rates , choose your 'pivot' currency , and check his value in comparison to other currencys. 
# What in side
service 1 - backend using FastApi  
service 2 - frontend using "TBD"  
Database - JSON file with the currencys / API with currencys (TBD)  

# Design 
<img width="790" alt="Design" src="https://user-images.githubusercontent.com/48453080/208944058-387182e5-88e8-4c41-9916-78a9380b42e5.png">



# How to run:

##### Docker Build: (make sure you are in the app directory)
``
docker build -t fastapi .
``
##### Docker Run:
``
docker run -d -p 8080:8080 fastapi
``
##### run all test using pytest:
``
pytest unit_tests.py
``
##### run Frontend (Streamlit) service: (make sure you are in the frontend directory)
``
streamlit run ui.py
``

##### Build Docker Compose with Backend (8080 fastapi) + Frontend (8051 streamlit)
``
DOCKER_BUILDKIT=0 docker-compose up -d --build
``


