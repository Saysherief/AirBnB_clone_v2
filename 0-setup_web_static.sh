#!/usr/bin/env bash
# setup server for static deployment

sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/{releases,shared}
sudo mkdir -p /data/web_static/releases/test/
sudo tee /data/web_static/releases/test/index.html > /dev/null <<EOT
<!Doctype html>
<html>
	<body> It works </body>
</html>
EOT
if [ -e /data/web_static/current ] 
then
	sudo rm -rf /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R "$USER":"$USER" /data/

sudo tee /etc/nginx/sites-enabled/default > /dev/null << EOT

server {
	listen 80;
	server_name _;
	root /var/www/html;
	
	location / {
		try_files \$uri \$uri/ = 404;
	}


	location /hbnb_static {
		alias /data/web_static/current;
	}
}
EOT
sudo service nginx restart
