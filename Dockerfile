FROM python:3.10-bullseye
ENV PYTHONUNBUFFERED=1
WORKDIR /minidoc

RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates iputils-ping telnet dnsutils iproute2 && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt
COPY my_openssl.cnf /usr/lib/ssl/openssl.cnf
RUN rm /etc/ssl/openssl.cnf 

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001
