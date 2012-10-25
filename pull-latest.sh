#! /bin/bash

repo_dir=/home/joelgkinney/fortpoint.me
src=/home/joelgkinney/fortpoint.me/flask.fortpoint.me/static/*
dest=/home/joelgkinney/webapps/static/

cd $repo_dir && git pull

# Update static assets
# Delete existing media.
rm -rf $dest
# Copy over media from project.
cp -R $src $dest

# Restart Apache
/home/joelgkinney/webapps/fpl_flask/apache2/bin/restart
