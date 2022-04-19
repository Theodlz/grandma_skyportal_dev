import pathlib
import subprocess

from launcher.commands.build import build
from launcher.config import check_config_exists


def run(
    init: bool = False,
    repo: str = "origin",
    branch: str = "master",
    do_update: bool = False,
    test: bool = False,
):
    """🚀 Launch Grandma SkyPortal"""
    if init:
        build(
            init=init,
            repo=repo,
            branch=branch,
            do_update=do_update,
        )

    # create common docker network (if it does not exist yet)
    if test:
        cmd = subprocess.Popen(
            ["make", "run_testing"],
            cwd="skyportal"
        )
        cmd.communicate()
    else:
        cmd = subprocess.Popen(
            ["make", "run"],
            cwd="skyportal"
        )
        cmd.communicate()
