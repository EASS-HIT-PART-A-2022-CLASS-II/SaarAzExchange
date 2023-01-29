# Exchange Rates API
aplication for currency exchange rates , choose your 'pivot' currency , and check his value in comparison to other currencys. 
# What in side
service 1 - backend using FastApi  
service 2 - frontend using Streamlit 
service 3 - Analytics cache using Redis 
Database - JSON file with the currencys  

# Design 
<img width="940" alt="Design" src="https://user-images.githubusercontent.com/48453080/215313043-ffceb3ee-60ff-4ebb-ace2-39c8c2d83216.png">


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
##### start reddis:
``
redis-server --appendonly yes
``

