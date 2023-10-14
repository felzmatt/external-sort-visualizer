FROM python:3.10
WORKDIR /app
COPY . .
RUN cd /app && pip install --no-cache -r requirements.txt
CMD [ "python", "/app/sorter/main.py" ]