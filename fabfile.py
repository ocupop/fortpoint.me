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

def deploy(branch_name="master"):
    run('%s/pull-and-restart.sh %s' % (env.repo_dir, branch_name))
