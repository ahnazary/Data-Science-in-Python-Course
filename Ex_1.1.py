import os
import re


def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    return re.findall("[A-Z]{1}[a-z]*", simple_string)


def grades():
    projectPath = os.path.abspath(os.path.dirname(__file__))
    path = projectPath + "/grades.txt"
    with open(path, "r") as file:
        grades = file.read()

    result = []
    for item in re.finditer("(?P<student>[A-Z]{1}[a-z]*\ [A-Z]{1}[a-z]*)(:\ )(?P<grade>[B]{1})", grades):
        result.append(item.groupdict().get('student'))
    return result


def logs():
    projectPath = os.path.abspath(os.path.dirname(__file__))
    path = projectPath + "/logdata.txt"
    with open(path, "r") as file:
        logdata = file.read()

    result = []
    pattern = """
    (?P<host>[\d\.]+)
    (\ -\ )
    (?P<user_name>[\w-]*)
    (\ \[)
    (?P<time>[\w\./:\ -]*)
    (\]\ ")
    (?P<request>[^"]+)
    """
    for item in re.finditer(pattern, logdata, re.VERBOSE):
        result.append(item.groupdict())
    return result

for item in logs():
    print(item)
print(len(logs()))
