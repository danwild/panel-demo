FROM python:3.9.1

WORKDIR /app/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/

EXPOSE 5006

CMD panel serve --show panel_app.py
