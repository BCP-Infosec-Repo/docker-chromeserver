# Run latest alpine container
FROM debian:latest

# Copy latest ChromeDriver to drivers directory
COPY chromedriver /drivers/

# Set execution permissions on driver
RUN chmod +x /drivers/chromedriver

# Install dependencies
RUN apt-get update && apt-get install libnss3 libx11-6 libglib2.0 -y

# Add low-privileged user
RUN useradd chromedriver

# Change running process
ARG port=9515

# Store port variable
ENV BIND_PORT ${port}

# Expose default port
EXPOSE ${BIND_PORT}

# Change working directory
WORKDIR /drivers

# Run as chromedriver user
USER chromedriver

# Run Chromedriver server and allow remote binds
ENTRYPOINT ./chromedriver --whitelisted-ips="" --port=${BIND_PORT}
