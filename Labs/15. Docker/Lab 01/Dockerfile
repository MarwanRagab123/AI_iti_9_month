FROM python:3.9-slim as bu

WORKDIR /build

COPY test.py .


FROM python:3.9-alpine

WORKDIR /app
COPY --from=bu /build/test.py .

CMD ["python","test.py"]

