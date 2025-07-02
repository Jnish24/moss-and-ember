FROM node:18

# Create app directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN npm install

# Run unit test to generate lcov
RUN npm run test:unit || true

# Run SonarScanner
RUN npx sonar-scanner

## You can comment out the RUN npx sonar-scanner if you want to run it manually for debugging.
