#!/usr/bin/python3
"""
This is a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone
repo, using the function do_pack and distributes an archive
to your web servers, using the function do_deploy.
"""


from fabric.api import local, put, run, env
import os
from datetime import datetime


env.hosts = ['34.239.151.121', '3.239.91.139']

def do_pack():
    """
    Packs all web_static files into an archive.
    """
    time =  datetime.now().strftime("%Y%m%d%H%M%S")
    versions = '/root/AirBnB_clone_v2/versions'
    if not os.path.exists(versions):
        os.makedirs(versions)
    archive = 'versions/web_static_' + time + '.tgz'
    local("tar -cvzf {} web_static".format(archive))

def do_deploy(archive_path):
    """
    Deploys web_static archive onto the servers.
    """
    if not os.path.exists(archive_path):
        return False
    up = put(archive_path, '/tmp/')
    if up.failed:
        return False
    server_arch = '/tmp' + archive_path[-30:]
    deploy_path = '/data/web_static/releases' + archive_path[-30:-4] + '/'
    res = run('mkdir -p {}'.format(deploy_path))
    if res.failed:
        return False
    res = run('tar -zxf {} -C {}'.format(server_arch, deploy_path))
    if res.failed:
        return False
    res = run('rm {}'.format(server_arch))
    if res.failed:
        return False
    res = run('cp -r {}web_static/* {}'.format(deploy_path, deploy_path))
    if res.failed:
        return False
    res = run('rm -rf /data/web_static/current {}web_static/'.format(deploy_path))
    if res.failed:
        return False
    res = run('ln -s {} /data/web_static/current'.format(deploy_path))
    if res.failed:
        return False
    return True
