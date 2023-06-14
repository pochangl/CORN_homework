import subprocess
from time import sleep
from contextlib import suppress


def has_changed():
    with suppress(subprocess.CalledProcessError):
        return subprocess.check_output(['git', 'diff']) or subprocess.check_output(['git', 'diff', '--staged'])


def upload():
    with suppress(subprocess.CalledProcessError):
        subprocess.run(['git', 'add', '--all'])
        subprocess.run(['git', 'commit', '-m', 'autocommit'])
        subprocess.run(['git', 'push'])
        print('uploaded')



with suppress(KeyboardInterrupt):
    while True:
        if has_changed():
            print('changed')
            upload()
        sleep(20)
