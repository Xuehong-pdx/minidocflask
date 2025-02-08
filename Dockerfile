FROM python:3.10-bullseye
ENV PYTHONUNBUFFERED=1
WORKDIR /minidoc

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "/minidoc/app.py"] 

