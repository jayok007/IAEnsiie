FROM python:3.7.1-stretch

WORKDIR /app

COPY . .
RUN make install
RUN pip3 install gunicorn

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

EXPOSE 5000

ENTRYPOINT ["make", "run"]
