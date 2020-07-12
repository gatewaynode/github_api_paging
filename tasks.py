from invoke import task
from invoke import run
import os
from pprint import pprint
import datetime
import shutil
import logging
import traceback


@task
def project(ctx):
    project_name = input("What is the project name?  ").replace(" ", "_")
    run(f"mv -v new.py {project_name}.py")
    author_name = input("What alias are we going to use?  ")
    print(author_name)
    run(f"sed -i 's/<AUTHOR>/{author_name}/1' LICENSE.txt")
    run(f"sed -i 's/<AUTHOR>/{author_name}/1' {project_name}.py")
    run(
        f"THIS_DATE=`date +%Y`; sed -i 's/<YEAR>/{datetime.date.today().year}/1' LICENSE.txt"
    )
    run("mv -v _.gitignore .gitignore")


@task
def virtualenv(ctx):
    run("virtualenv --prompt ')-- GITHUB --( ' env --python python3.8")
    run("env/bin/pip install -r requirements-dev.txt")
    print("\nVirtualENV Setup Complete.  Now run: source env/bin/activate\n")


@task
def clean(ctx):
    run("rm -rvf __pycache__")
    run("rm -rvf src/__pycache__")


@task
def build(ctx):
    run("cp requirements-dev.txt requirements.txt")
    # @todo filter out known development packages
    # @todo create docker image
