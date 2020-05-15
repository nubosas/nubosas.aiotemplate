FROM python:3.8-slim as base

# PYTHONUNBUFFERED: https://docs.python.org/3.8/using/cmdline.html#envvar-PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV /srv/venv
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/ed77b63706ea721766a62ff22d3a251d8b4a6a30/wait-for-it.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/wait-for-it.sh && \
    pip install virtualenv


FROM base as compile-image

RUN apt-get update && apt-get install -y --allow-unauthenticated \
    build-essential \
    git && \
    python -m virtualenv ${VIRTUAL_ENV}

ENV PATH "${VIRTUAL_ENV}/bin:${PATH}"

# Install app dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install .


FROM base as build-image

COPY --from=compile-image ${VIRTUAL_ENV} ${VIRTUAL_ENV}

ENV PATH "${VIRTUAL_ENV}/bin:${PATH}"

CMD ["/app/run_app.sh"]


FROM compile-image

COPY dev-requirements.txt dev-requirements.txt

RUN pip install -r dev-requirements.txt

ENV PATH "${VIRTUAL_ENV}/bin:${PATH}"
CMD ["python", "-m", "pytest"]
