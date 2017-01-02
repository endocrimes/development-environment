from fabric.api import *
from fabric.contrib.files import exists

env.user = "root"

@task
def install_or_update_dotfiles():
    if exists('~/.files.git'):
        run("git --work-tree=$HOME --git-dir=$HOME/.files.git pull origin master")
    else:
        run("apt-get install git -y &> /dev/null")
        run("git --work-tree=$HOME --git-dir=$HOME/.files.git init")
        run("git --work-tree=$HOME --git-dir=$HOME/.files.git remote add origin https://github.com/endocrimes/Dotfiles.git")
        run("git --work-tree=$HOME --git-dir=$HOME/.files.git pull origin master")

@task
def setup():
    run("apt-get update")
    run("apt-get upgrade -y")
    install_or_update_dotfiles()
    run(".config/os/ubuntu/install.sh")
