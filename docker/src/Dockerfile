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
COPY ./pkg/common /app/pkg/common
COPY ./tasks /app/tasks
COPY ./pkg/models /app/pkg/models
COPY ./pkg/dv360 /app/pkg/dv360/
COPY ./requirements.txt /app/requirements.txt
COPY ./app.py /app/app.py
COPY ./.env /app/.env
RUN pip install --requirement requirements.txt
RUN ls
CMD [ "python", "app.py", "--gg_application_name=api-gg-logger", "--gg_application_logger=./logs/gg/log.txt", "--run_previous_report=False"]