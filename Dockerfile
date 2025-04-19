FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy your application code
COPY . /app/

# Make sure to expose the port you're running the app on
EXPOSE 8000

# Command to run the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
