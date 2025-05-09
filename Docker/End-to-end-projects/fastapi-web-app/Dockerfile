FROM python:3.11-alpine AS builder

WORKDIR /app

# Update sqlite-libs first
RUN apk update && \
    apk upgrade sqlite-libs && \
    apk add --no-cache \
    build-base \
    postgresql-dev

# Install pip and setuptools with fixed version
RUN pip install --no-cache-dir -U pip setuptools>=70.0.0

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir uvicorn

COPY ./app ./app

# Stage 2: Create the production image
FROM python:3.11-alpine

WORKDIR /app

# Update sqlite-libs in the final image
RUN apk update && \
    apk upgrade sqlite-libs

# Copy Python packages and executables from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Copy application code
COPY --from=builder /app /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]