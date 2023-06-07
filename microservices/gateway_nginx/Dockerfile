FROM nginx:latest

RUN apt-get update -y && apt-get install -y netcat

# Copy the custom Nginx configuration file to the container
COPY default.conf /etc/nginx/conf.d/
COPY wait_for_mongo_express.sh /app/wait_for_mongo_express.sh
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/wait_for_mongo_express.sh

# Expose port 80 for incoming traffic
EXPOSE 80

# Start Nginx in the foreground when the container starts
# CMD ["nginx", "-g", "daemon off;"]
ENTRYPOINT [ "/app/entrypoint.sh" ]