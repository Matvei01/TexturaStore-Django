FROM python:3.11-slim

WORKDIR /usr/src/store

RUN apt-get update && apt-get install -y netcat-openbsd

RUN mkdir media

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN sed -i 's/\r$//g' /usr/src/store/entrypoint.sh
RUN chmod +x /usr/src/store/entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]