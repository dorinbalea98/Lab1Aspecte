import os
import sys
from subprocess import Popen, PIPE


def get_git_number():
    process = Popen(['git', 'show'], stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    stdout = stdout.decode('utf-8')
    return stdout.split('\n')[0].replace('commit ', '')


def build_project():
    process = Popen(['pyinstaller', '--onefile', str(sys.argv[1] + '.py')])
    stdout, stderr = process.communicate()
    print('\nBuild was successfull!')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Not enough parameters provided!')
        sys.exit(0)
    gitNr = get_git_number()
    os.system('echo ' + gitNr + ' > ./dist/VersionControlNumber.txt')
    build_project()
    sys.exit(0)
