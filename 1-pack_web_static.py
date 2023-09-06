#!/usr/bin/python3
"""This generates a .tgz archive from the contents of the web_static folder."""

from fabric.api import local
from datetime import datetime


def do_pack():

    """
    Creates a compressed .tgz archive from the web_static folder contents.

    Returns:
        str: Path to the created archive if successful, None otherwise.
    """
    try:
        now = datetime.now()
        timestamp = now.strftime('%Y%m%d%H%M%S')
        archive_name = 'web_static_' + timestamp + '.tgz'
        local('mkdir -p versions')
        local('tar -cvzf versions/{} web_static'.format(archive_name))
        return 'versions/' + archive_name
    except Exception as e:
        return None
