# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY req.txt .
RUN pip install --no-cache-dir -r req.txt

# Copy the rest of the application code
COPY bot.py .

# Expose the port on which the app runs
EXPOSE 5000

# Command to run the application
CMD ["python", "bot.py"]
