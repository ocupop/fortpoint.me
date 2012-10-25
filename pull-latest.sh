#! /bin/bash

repo_dir=/home/joelgkinney/fortpoint.me
static_src=/home/joelgkinney/fortpoint.me/flask.fortpoint.me/static/
static_dest=/home/joelgkinney/webapps/static/

cd $repo_dir && git pull

# Update static assets
# Delete existing media.
rm -rf $static_dest*
# Copy over media from project.
cp -R $static_src* $static_dest

# Restart Apache
/home/joelgkinney/webapps/fpl_flask/apache2/bin/restart
