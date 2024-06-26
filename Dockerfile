FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir app
COPY /pyproject.toml /app
COPY . .

# install psycopg
# jpeg-dev and musl-dev zlib zlib-dev in case you will use Pillow

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN poetry config virtualenvs.create false
RUN poetry install
RUN apk del .tmp-build-deps

WORKDIR /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web

USER user

ENTRYPOINT [ "sh", "/entrypoint.sh" ]