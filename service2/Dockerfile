FROM python

LABEL authors="kk745"

RUN pip install mariadb

COPY service2/filter.py .
COPY data.csv .
WORKDIR .

CMD ["python", "filter.py"]