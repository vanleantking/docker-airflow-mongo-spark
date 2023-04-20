FROM 'mongo:5.0'
COPY ./docker/mongo/init_mongodb.sh /etc/init_mongodb.sh
RUN chmod +x /etc/init_mongodb.sh
ENTRYPOINT ["sh", "/etc/init_mongodb.sh"]
