FROM python:3.11

# 設定工作目錄
WORKDIR /ISL

COPY ./requirements.txt .

# 安裝專案所需的依賴項
RUN pip install -r requirements.txt

WORKDIR /ISL
COPY . .