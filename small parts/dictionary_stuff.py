# contacts = {'bill': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}


# for bill in contacts:
#     print(bill)


# my_subjects = {'CP1401', 'CP1404', 'MA1000'}
# your_subjects = {'CP1404', 'MA1008', 'NM1010'}

# print(my_subjects - your_subjects)  #what my_sub has that your_sub dosnt have
# print(my_subjects | your_subjects)  #all of them
# print(my_subjects & your_subjects)  # what they have in common
# print(my_subjects ^ your_subjects)  #ones they dont share collectively

places = {
    "place_01": {
        "city":'Lima',
        "country": 'Peru', 
        "piority": 3, 
        "visted_status":"n"
        },
    "place_02":{
        "city": 'Ackland',
        "country": 'New Zealand',
        "piority": 1,
        "visited_status":"n",
    },
    "place_03":{
        "city": 'Rome',
        "country": 'Italy',
        "piority": 12,
        "visited_status":"n",
        }
}
for x in range(1,(len(places)+1)):
    print(places["place_0{}".format(x)])