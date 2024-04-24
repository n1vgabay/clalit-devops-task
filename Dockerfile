FROM python:alpine3.19

ARG USER=clalit
ENV HOME /home/$USER

RUN apk update \
    && apk add --no-cache shadow \
    && adduser -D -h $HOME $USER \
    && chown -R $USER:$USER $HOME
USER $USER
WORKDIR $HOME

COPY app/app.py app/requirements.txt ./app/
RUN pip install --no-cache-dir -r ./app/requirements.txt

EXPOSE 5000
WORKDIR $HOME/app

CMD ["python", "app.py"]