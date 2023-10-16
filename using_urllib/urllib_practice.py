import urllib.request, urllib.error

fhand =  urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())



# Counting the number of times the word appears
print('Counting the number of times the word appears')
fhand2 = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand2:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1


print(counts)
