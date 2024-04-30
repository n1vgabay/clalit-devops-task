FROM python:alpine3.19

ARG USER=clalit
ENV HOME /home/$USER

RUN adduser -D -h $HOME $USER \
    && apk add --no-cache shadow \
    && chown -R $USER:$USER $HOME

COPY app/app.py app/requirements.txt /app/

WORKDIR /app
RUN apk add --no-cache libpq \
    && apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
    && pip install --no-cache-dir -r ./requirements.txt \
    && apk del .build-deps

USER $USER
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]