FROM python:3.8.3
LABEL authors="mhmd"

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /usr/src/app
RUN pip install --prefer-binary --no-cache-dir --upgrade -r requirements.txt
# copy project
COPY . /usr/src/app

EXPOSE 8000

CMD ["gunicorn", "interview_task.wsgi"]