FROM python:3.11

# 設定工作目錄
WORKDIR /ISL

COPY ./requirements.txt .

# 安裝專案所需的依賴項
RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN pip install -r requirements.txt

WORKDIR /ISL
COPY . .