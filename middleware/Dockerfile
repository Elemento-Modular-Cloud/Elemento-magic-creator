FROM python:3.9-alpine

WORKDIR /middleware

COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src .

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
