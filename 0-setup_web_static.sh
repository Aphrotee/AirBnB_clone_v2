#!/usr/bin/env bash
# Sets up my web servers for the deployment of web_static.
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
sudo service nginx start
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo 'Hello World' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/
sudo sed -i '/server_name _;$/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tdisable_symlinks off;\n\t}' /etc/nginx/sites-enabled/default
sudo nginx -t
sudo nginx -s reload
