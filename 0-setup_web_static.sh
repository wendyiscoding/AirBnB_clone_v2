#!/usr/bin/env bash
# set up web servers for deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "HTML file to test Nginx configuration" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
new_string="location /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tindex index.html index.htm;\n\t}"
file=$"/etc/nginx/sites-available/default"
sudo sed -i "29i $new_string" $file
sudo service nginx restart
