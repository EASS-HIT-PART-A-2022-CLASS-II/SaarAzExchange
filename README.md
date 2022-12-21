# Exchange Rates API
aplication for currency exchange rates , choose your 'pivot' currency , and check his value in comparison to other currencys. 
# What in side
service 1 - backend using FastApi  
service 2 - frontend using "TBD"  
Database - JSON file with the currencys / API with currencys (TBD)  

# Design 
<img width="817" alt="Desgin" src="https://user-images.githubusercontent.com/48453080/208406747-dd9987bf-6713-46ec-aed6-2cfc4f051df5.png">


# How to run:

##### Docker Build:
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


