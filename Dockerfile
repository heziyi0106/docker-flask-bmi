# Use the official Python image as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install Flask
RUN pip install Flask==3.0.2 && pip install mysql-connector-python==8.0.33

# 將會將 01_bmi 文件夾中的所有內容複製到容器中的當前工作目錄中。
COPY . .

# 暴露應用程序運行的端口
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
