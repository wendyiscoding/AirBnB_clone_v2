#!/usr/bin/python3
"""
do_pack generates a .tgz archive from the contents of the web_static folder of
AirBnB Clone repo
"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """
    compresses files
    Return:
        name of archive created, or None if unsuccessful
    """
    local('mkdir -p versions')
    zeit = datetime.now().strftime('%Y%m%d%H%M%S')
    try:
        local('tar -cvzf versions/web_static_{}.tgz web_static'.format(zeit))
        return 'versions/web_static_{}.tgz'.format(zeit)
    except:
        return None
