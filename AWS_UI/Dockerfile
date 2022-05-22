FROM python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5001

CMD [ "python", "index.py" ]