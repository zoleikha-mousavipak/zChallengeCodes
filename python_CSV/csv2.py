# import csv
# from django.http import HttpResponse
#
#
# def mycsv():
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="pokemon.csv"'
#
#     writer = csv.writer(response)
#     writer.writerow(['first row', 'foo', 'bar'])
#     writer.writerow(['first row2', 'foo2', 'bar2'])
#
#     return response
#
# mycsv()


import csv
from django.http import HttpResponse


def some_view():
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

some_view()

