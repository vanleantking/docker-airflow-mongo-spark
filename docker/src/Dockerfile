FROM python:3.11

# config timezone
RUN pip install --upgrade pip
RUN apt-get update -y
ENV TZ="Asia/Ho_Chi_Minh"
RUN apt-get install -y ca-certificates
RUN apt-get install -y tzdata

WORKDIR /app
COPY ./logs/gg /app/logs/gg
COPY ./data /app/data
COPY ./.env /app/.env
COPY ./src/pkg /app/pkg
COPY ./src/app.py /app/app.py
COPY ./requirements.txt /app/requirements.txt
RUN pip install --requirement requirements.txt
RUN ls
CMD [ "python", "app.py", "--gg_application_name=api-gg-logger", "--gg_application_logger=./logs/gg/log.txt", "--run_previous_report=False"]