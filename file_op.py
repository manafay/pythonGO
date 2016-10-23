
def words(file): return file.read().split()

def chars(file): return file.read()

def lines(file): return file.readlines()

def count(func, file):
    with open(file) as inf:
        return len(func(inf))

print(count(words, 'entry.py'),count(chars, 'entry.py'),count(lines, 'entry.py'))

