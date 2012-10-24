'''To use this file, just create a settings_local.py folder in the same
directory with contents like this:

HOSTS = ["blah"]

Where "blah" is the name of Joel's server in your ssh config.
'''
from fabric.api import *

import settings_local


env.update(
    use_ssh_config=True,
    hosts=settings_local.HOSTS,
    repo_dir='/home/joelgkinney/fortpoint.me',
    )


def pull():
    run('cd %(repo_dir)s && git pull' % env)


def restart_apache():
    run('/home/joelgkinney/webapps/fpl_flask/apache2/bin/restart')


def move_static():
    src = '/home/joelgkinney/fortpoint.me/flask.fortpoint.me/static/*'
    dest = '/home/joelgkinney/webapps/static/'

    # Delete existing media.
    run('rm -rf %s*' % dest)

    # Copy over media from project.
    run('cp -R %s %s' % (src, dest))


def deploy():
    pull()
    move_static()
    restart_apache()
