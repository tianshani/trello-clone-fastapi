FROM python:3.12.3-slim

WORKDIR /trello-app

COPY ./requirements.txt /trello-app/requirements.txt

# ENV PYTHONDONTWRITEBYTECODE=1

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /trello-app/app

# EXPOSE 6969

# RUN echo hellofromdocker

CMD [ "fastapi", "run", "app/main.py", "--port", "80" ]
