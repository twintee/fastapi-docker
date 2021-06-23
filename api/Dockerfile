ARG BASE_IMAGE=python:3.8-slim-buster
FROM $BASE_IMAGE

# system update & package install
RUN apt-get -y update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    openssl \
    libssl-dev \
    libmariadb-dev-compat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add Tini
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# 一般ユーザーアカウントを追加
ARG USER_NAME=app
ARG USER_UID=1000
ARG PASSWD=password

RUN useradd -m -s /bin/bash -u $USER_UID $USER_NAME && \
    gpasswd -a $USER_NAME sudo && \
    echo "${USER_NAME}:${PASSWD}" | chpasswd && \
    echo "${USER_NAME} ALL=(ALL) ALL" >> /etc/sudoers

WORKDIR /app

# FastAPIのソースコードなどをコンテナ内へCOPY
# COPY ./app /app/app
COPY ./pyproject.toml /app/pyproject.toml
# local環境で使用しているpoetry.lockファイルがあればそれも追加する
# COPY ./poetry.lock /app/poetry.lock
RUN chown -R ${USER_NAME}:${USER_NAME} /app

USER $USER_NAME
COPY ./app/home/* /home/$USER_NAME/
ENV PATH $PATH:/home/${USER_NAME}/.local/bin

# poetry & database & キャッシュ削除
RUN python3 -m pip install --user --upgrade pip && \
    python3 -m pip install poetry --user && \
    poetry config virtualenvs.in-project true && \
    poetry install && \
    rm -rf ~/.cache/pip/* && \
    rm -rf ~/.cache/pypoetry/*

# Poetryで作った仮想環境にPATHを通しておく（予めpoetryのconfigを設定して仮想環境のPATHを一意にしておく）
ENV PATH=/app/.venv/bin:$PATH

EXPOSE 8000

# Execute
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
