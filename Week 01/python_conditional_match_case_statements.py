# In python there is 'match case' statement, or we can say it as 'switch case'
# Match case feature is available in version 3.10 or above
# here is the example of http error codes and their response

# Doing that example first with if elif else statemetns
http_status = 600

if http_status == 200 or http_status == 201:
    print('Success')
elif http_status == 400:
    print('Bad request')
elif http_status == 404:
    print('Not Found')
elif http_status == 500 or http_status == 501:
    print('Server Error')
else:
    print('Unknown')


# now we are molding above if elif else statement example into match case
"""
match http_status:
    case 200 | 201:
        print('success')
    case 400:
        print('Bad Request')
    case 500 | 501:
        print('Server')
    case _:
        print('Unknown')
"""

