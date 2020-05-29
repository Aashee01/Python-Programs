#generator to generate square of top ten number

#top ten perfect squaree


def topten():

    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1


value=topten()
for i in value:
    print(i)