FROM python:3.11

WORKDIR /opt/app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

CMD ["sh", "-c", "streamlit run app.py"]