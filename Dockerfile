FROM eclipse-temurin:21-alpine
RUN apk add --no-cache jq python3
RUN adduser -D -u 1000 minecraft

WORKDIR /server
USER minecraft
COPY setup.py setup.py
CMD ["python3", "./setup.py"]