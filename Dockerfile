FROM python:3.8.5-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080 8501

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port 8080 & streamlit run streamlit.py --server.port 8501 --server.address 0.0.0.0"]
