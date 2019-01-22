"""
This script does the same thing as the following linux pipeline:
for i in ../*/*py; do grep ^import $i|sed 's/import //g' ;
done | sort | uniq -c | sort -nr
"""
import os
import re
import fnmatch
from collections import Counter


def main():
    file_pattern = '../*/*.py'
    search_pattern = r'^import '

    py_files = gen_files(file_pattern)
    lines = gen_lines(py_files)
    grep_lines = gen_grep(search_pattern, lines)
    package_name = gen_count(grep_lines)

    for line in package_name:
        print(line)


def gen_files(pattern):
    """Generate files that match a given filename pattern."""
    for root, dirs, files in os.walk(pattern.split('/')[0]):
        for filename in fnmatch.filter(files, pattern.split('/')[2]):
            yield os.path.join(root, filename)


def gen_lines(files):
    """Generate lines from all files."""
    for file in files:
        with open(file, 'r') as fin:
            for line in fin.readlines():
                yield line


def gen_grep(pattern, lines):
    """Generate all lines that match the regex pattern."""
    for line in lines:
        if re.search(pattern, line):
            yield line


def gen_count(lines):
    """Generate sorted package names and counts used."""
    lines = list(lines)
    lines = [line.split()[1] for line in lines]
    c = Counter(lines)
    for package, count in c.most_common():
        yield '{} {}'.format(count, package)


if __name__ == '__main__':
    main()
