betsy_info = {'Name': 'Betsy Foobar',
              'Phone': 'x8012',
              'Street': '1600 Grand Avenue',
              'City': 'Saint Paul',
              'State': 'MN',
              'Email': 'bfoobar@macalester.edu'}

tom_info = {'Name': 'Tom Riddle',
            'Phone': 'x8512',
            'Street': '1600 Grand Avenue',
            'City': 'Saint Paul',
            'State': 'MN',
            'Email': 'triddle@macalester.edu'}

print(betsy_info['Name'] + "'s phone:", betsy_info['Phone'])
print(tom_info['Name'] + "'s email:", tom_info['Email'])

address_book = [ betsy_info, tom_info,
                {'Name': 'Susan Fox',
                 'Phone': 'x6553',
                 'Street': '1600 Grand Avenue',
                 'City': 'Saint Paul',
                 'State': 'MN',
                 'Email': 'fox@macalester.edu'} ]

print(address_book)

address_book[3] = {'Name': "Gabby", "Phone": "911", "Street": "1600 Grand Avenue", "City": "Saint Paul", "State": "MN"}
address_book[4] = {"Name": "John", "Phone": "125", "Street": "1600 Grand Avenue", "City": "Saint Paul", "State": "MN"}

def filter_by_city(city, book):
    only_city = filter(lambda item: item["City"] == city, book)
    return only_city

print(filter_by_city("Saint Paul", address_book))
