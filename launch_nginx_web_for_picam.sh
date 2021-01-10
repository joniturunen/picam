#!/bin/bash
docker run -it --rm -d -p 80:80 --env TZ=Europe/Helsinki --name web -v $PWD/tmp:/usr/share/nginx/html -v $PWD/confs/picam.conf:/etc/nginx/conf.d/default.conf nginx


