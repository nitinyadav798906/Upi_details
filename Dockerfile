# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY req.txt .
RUN pip install --no-cache-dir -r req.txt

# Copy the bot script
COPY bot.py .

# Environment variable for the bot token
ENV TELEGRAM_BOT_TOKEN=7854424887:AAF1Mhu6tPz6rkso5eW1IHKGq8cYx9QCBhY

# Run the bot
CMD ["python", "bot.py"]
