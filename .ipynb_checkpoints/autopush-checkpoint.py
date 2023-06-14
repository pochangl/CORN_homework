import subprocess
from time import sleep
from contextlib import suppress


def has_changed():
    with suppress(subprocess.CalledProcessError):
        output = subprocess.check_output(['git', 'diff'])
        return output


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
