FROM python:3.11.3-slim-buster

# Set the working directory
WORKDIR /app

# Copy application files
COPY src/ /app/
COPY entrypoint.sh /app/

# Install Poetry and project dependencies
RUN pip3 install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

# Make the entrypoint script executable
RUN chmod +x entrypoint.sh

# Expose port 8000
EXPOSE 8000

# Set the entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]