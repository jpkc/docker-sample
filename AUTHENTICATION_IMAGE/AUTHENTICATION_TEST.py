# Authentication Test

# In this first test, we are going to check that the identification logic works well.

# To do this, we will need to make GET requests on the /permissions entry point.
# We know that two users exist alice and bob and their passwords are wonderland and builder.
# We'll try a 3rd test with a password that doesn't work: clementine and mandarine.

# The first two requests should return a 200 error code while the third should return a 403 error code.

import os
import requests

api_address = 'TOY_MODEL'
entry_point = "permissions"
api_port = 8000


def authentication_test(entry_point, api_address, api_port, test_case):
    r = requests.get(
        url='http://{address}:{port}/{entry_point}'.format(address=api_address,
                                                           port=api_port,
                                                           entry_point=entry_point),
        params=test_case
    )
    output = '''
    ============================
        Authentication test
    ============================
    request done at "/{entry_point}"
    | username="{username}"
    | password="{password}"
    expected result = {expected_result}
    actual result = {status_code}
    ==>  {test_status}
    '''

    status_code = r.status_code

    if status_code == test_case["response"]:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'

    print(output.format(entry_point=entry_point,
                        username=test_case["username"],
                        password=test_case["password"],
                        expected_result=test_case["response"],
                        status_code=status_code,
                        test_status=test_status))
    # printing in a file
    if os.environ.get('LOG') == "1":
        with open('/home/SHARED_STORAGE/api_test.log', 'a') as file:
            file.write(output.format(entry_point=entry_point,
                                     username=test_case["username"],
                                     password=test_case["password"],
                                     expected_result=test_case["response"],
                                     status_code=status_code,
                                     test_status=test_status))


authentication_test_vector = [
    {"entry_point": "permissions",
     "username": "bob",
     "password": "builder",
     "response": 200
     },
    {"entry_point": "permissions",
     "username": "alice",
     "password": "wonderland",
     "response": 200
     },
    {"entry_point": "permissions",
     "username": "clementine",
     "password": "mandarine",
     "response": 403
     }]

for test in authentication_test_vector:
    authentication_test(entry_point, api_address, api_port, test)
