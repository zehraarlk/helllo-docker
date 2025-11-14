# 1. Python tabanlı imaj
FROM python:3.10-slim

# 2. Çalışma dizini oluştur
WORKDIR /app

# 3. Sadece gereksinim dosyasını kopyala ve paketleri kur
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 4. Uygulama dosyalarının tamamını kopyala
COPY . /app/

# 5. Uygulamayı başlat
CMD ["python", "web_service.py"]
