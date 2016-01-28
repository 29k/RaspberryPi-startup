#setting nginx and gunicorn on Pi

#Objective
headless step by step install and setting guide

#Requirement
1. None;

#Content
###install gunicorn
  ```
  sudo pip install gunicorn
  ```
###install nginx
  ```
  sudo apt-get install nginx
  ```
###create nginx.conf
  ```
  cd /etc/nginx/sites-enabled/
  touch nginx.conf
  sudo nano nginx.conf
  ```
  modify nginx.conf content with
  ```
  server {
    # the port your site will be served on
    listen      80;
    # the domain name it will serve for
    server_name .domain.tld ip.adress;   # substitute by your FQDN and machine's IP address
    charset     utf-8;

    #Max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /var/www/path/to/your/project/media;      # your Django project's media files
    }

    location /static  {
        alias /var/www/path/to/your/project/our_static;      # your Django project's media files
    }

    location /assets {
        alias /var/www/path/to/your/project/static;     # your Django project's static files
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
  ```

###start nginx server
  ```
  sudo /etc/init.d/nginx start
  ```
###restart nginx server
  ```
  sudo /etc/init.d/nginx restart
  ```

###start djangoapp via  gunicorn
  ```
  cd /var/www/path/to/your/project/where_is_manage.py
  sudo gunicorn myproject.wsgi
  ```

#reference resource
1. [set up Django, Nginx and Gunicorn in a Virtualenv controled by Supervisor](https://gist.github.com/Atem18/4696071)
2. [Installing Django on a Raspberry Pi](http://www.hackedexistence.com/project/raspi/django-on-raspberry-pi.html)


#Issue
