FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt remove python3-rpi.gpio && apt install python3-rpi-lgpio && apt-get install -y \
    gcc \
    libc-dev \
    libjpeg-dev \
    python3-pil \
    zlib1g-dev \
    libgpiod-dev \
    swig \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "Main.py"]