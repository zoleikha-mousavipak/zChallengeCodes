import csv


def mydef(request):
    with open('pokemon.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


f=open('pokemon.csv', newline='')
mydef(request=f)