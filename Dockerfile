FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update && DEBIAN_FRONTEND=noninteractive apt -y upgrade
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN useradd --create-home snake
WORKDIR /home/snake
USER snake
COPY src src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "6660"]
