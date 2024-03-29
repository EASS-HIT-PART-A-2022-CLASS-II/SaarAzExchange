FROM python:3.9
RUN pip install httpx
RUN pip install FastAPI
RUN pip install "uvicorn[standard]"
RUN pip install requests
RUN pip install redis
RUN pip install forex-python


WORKDIR /app
COPY . .

CMD ["bash", "./start.sh"]
