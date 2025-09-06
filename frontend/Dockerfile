# Using Nginx image to serve static files
FROM nginx:alpine

# Copy the frontend files to Nginx's default directory
COPY . /usr/share/nginx/html

# Exposing port 80
EXPOSE 80

# Nginx's default command already serves the files
CMD ["nginx", "-g", "daemon off;"]
