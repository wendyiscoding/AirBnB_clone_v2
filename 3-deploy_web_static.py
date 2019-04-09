#!/usr/bin/python3
"""
creates and distributes an archive to your web servers
"""
from datetime import datetime
from fabric.api import *
import os
import re

env.hosts = ['104.196.153.49', '35.231.85.9']
env.user = 'ubuntu'


def do_pack():
    """
    compresses files, generating a .tgz archive from contents of
        web_static folder of AirBnB Clone repo
    Return:
        name of archive created, or None if unsuccessful
    """
    local('mkdir -p versions')
    zeit = datetime.now().strftime('%Y%m%d%H%M%S')
    try:
        local('tar -cvzf versions/web_static_{}.tgz web_static'.format(zeit))
        return '/versions/web_static_{}.tgz'.format(zeit)
    except:
        return None


@runs_once
def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    """
    if not os.path.exists(archive_path) and not os.path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp")
        """modify path as needed"""
        no_v_or_ext = archive_path[9:-5]
        no_v = archive_path[9:]
        pathname = "/data/web_static/releases/{}/".format(no_v_or_ext)
        run('sudo mkdir -p {}'.format(pathname))
        run('sudo tar -xzf /tmp/{} -C {}'.format(no_v, pathname))
        run('sudo rm /tmp/{}'.format(no_v))
        run('sudo mv {}web_static/* {}'.format(pathname, pathname))
        run('sudo rm -rf {}web_static'.format(pathname))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -sf {} /data/web_static/current'.format(pathname))
        return True
    except:
        return False


def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive)
