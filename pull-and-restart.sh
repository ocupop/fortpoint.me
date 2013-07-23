#! /bin/bash

# This script:
# 1. Downloads the latest code from the remote repository
# 2. Changes to the branch specified in the first argument, defaulting to
#    "master" if unspecified
# 3. Restarts the webserver

repo_dir=/home/joelgkinney/fortpoint.me
static_src=$repo_dir/flask.fortpoint.me/static/
static_dest=/home/joelgkinney/webapps/fpl_static/
remote_name=origin
branch_name=ocupop-redesign

if [ $1 ]; then
    branch_name=$1
fi

cd $repo_dir
git fetch $remote_name
git checkout $remote_name/$branch_name

# Update static assets
# Delete existing media.
rm -rf $static_dest*
# Copy over media from project.
cp -R $static_src* $static_dest

# Restart Apache
/home/joelgkinney/webapps/fpl_flask/apache2/bin/restart
