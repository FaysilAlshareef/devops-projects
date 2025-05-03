# Use the official Node.js image as the base image
FROM node:14.15

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Clear npm cache and install dependencies
RUN npm cache clean --force && \
    npm install -g @angular/cli@11 && \
    npm install

# Copy the rest of the application code
COPY . .

# Build the Angular application
RUN npm run build --prod

# Add a health check for the container
HEALTHCHECK --interval=30s --timeout=3s \
  CMD node -e "require('http').get('http://localhost:4200', (res) => process.exit(res.statusCode === 200 ? 0 : 1))"

# Expose Angular dev server port
EXPOSE 4200

# Start the application using ng serve
CMD ["npm", "start", "--", "--host", "0.0.0.0", "--port", "4200"]