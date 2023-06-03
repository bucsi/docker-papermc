FROM eclipse-temurin:17-alpine
WORKDIR /server
RUN apk add --no-cache jq python3
COPY setup.py setup.py
CMD ["python3", "./setup.py"]