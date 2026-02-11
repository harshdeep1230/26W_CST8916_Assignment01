# Use a lightweight version of Python
FROM python:3.9-slim

# Set the folder inside the container where your code will live
WORKDIR /app

# Copy everything from your computer folder into the container
COPY . .

# Run the command to install the library you listed in requirements.txt
RUN pip install -r requirements.txt

# Tell the container to listen on port 8080
EXPOSE 8080

# The final command to start your app
CMD ["python", "app.py"]