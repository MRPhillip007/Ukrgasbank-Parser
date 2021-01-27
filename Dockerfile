FROM python:3.8

RUN mkdir -p /usr/src/app/

RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install lxml

WORKDIR /usr/src/app/

COPY UkrgasBank.py /usr/src/app/
CMD ["python", "UkrgasBank.py"]
