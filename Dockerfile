FROM python:3.7

WORKDIR /usr/src/app

COPY ./test/Task1_Test.py /usr/src/app
COPY ./ConsoleApp/Product.py /usr/src/app

RUN pip install pytest

COPY . .

CMD ["python", "Task1_Test.py"]