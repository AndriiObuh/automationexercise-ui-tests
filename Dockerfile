# 1. Base image
FROM python:3.12-slim

# 2. Update packages and install Chrome and ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    chromium \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# 3. Set working directory inside the container
WORKDIR /app

# 4. Copy requirements.txt into the container
COPY requirements.txt .

# 5. Install all Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the entire project into the container
COPY . .

# 7. Set environment variables so Selenium can find Chrome
ENV CHROME_BIN=/usr/bin/chromium
ENV PATH="$PATH:/usr/lib/chromium/"

# 8. Default command when container runs
CMD ["pytest", "-v", "--alluredir=allure-results"]
