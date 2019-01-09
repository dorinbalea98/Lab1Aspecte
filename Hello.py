import time


def get_git_number(fileName):
    with open(fileName, 'r') as f:
        line = f.read()
    return line.replace('\n', '')


if __name__ == '__main__':
    gitNr = get_git_number('./VersionControlNumber.txt')
    print('Project version control number: ' + gitNr)
    print('Hello World')
    time.sleep(5)
