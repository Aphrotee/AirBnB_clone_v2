#!/usr/bin/python3
"""
This is a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone
repo, using the function do_pack.
"""


from fabric.api import local
import os
from datetime import datetime


def do_pack():
    """
    Packs all web_static files into an archive.
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    versions = '/root/AirBnB_clone_v2/versions'
    if not os.path.exists(versions):
        os.makedirs(versions)
    archive = 'versions/web_static_' + time + '.tgz'
    local("tar -cvzf {} web_static".format(archive))
    if os.path.exists(archive):
        return archive
    else:
        return
