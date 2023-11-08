FROM python

LABEL authors="kk745"

RUN pip install mariadb

COPY service2/filter.py .
COPY service2/data.csv .
WORKDIR .

CMD ["python", "filter.py"]