FROM python:3.9

WORKDIR /app

COPY flask_app/ /app/
COPY models/vectorizer.pkl /app/models/vectorizer.pkl

RUN pip install -r requirements.txt
RUN python -m nltk.downloader stopwords wordnet

EXPOSE 7860

CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
