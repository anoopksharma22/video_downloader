FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir --upgrade pip \
    && pip install streamlit yt-dlp ffmpeg-python

RUN apt-get update && apt-get install -y ffmpeg

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]