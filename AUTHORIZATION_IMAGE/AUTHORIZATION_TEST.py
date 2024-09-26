# Authorization Test

# In this second test, we will verify that our user authorization logic is working properly.
# We know that bob only has access to v1 while alice has access to both versions. For each of the users,
# we will make a query on the /v1/sentiment and /v2/sentiment entry points: we must then provide the
# arguments username, password and sentence which contains the sentence to be analyzed.


import os
import requests

api_address = "TOY_MODEL"
entry_point = "permissions"
api_port = 8000


def authorization_test(entry_point, api_address, api_port, test_case):
    r = requests.get(
        url='http://{address}:{port}/{entry_point}'.format(address=api_address,
                                                           port=api_port,
                                                           entry_point=entry_point),
        params=test_case
    )
    output = '''
    ============================
        Authorization test
    ============================
    request done at "/{entry_point}"
    | username="{username}"
    | password="{password}"
    Permission Requested = {expected_permission}
    Permissions Available = {available_permissions}
    Permission status = {permission_result}
    ==>  {test_status}
    '''

    if test_case["result"]:
        if test_case["permission"] in r.json()["permissions"]:
            test_status = 'SUCCESS'
        else:
            test_status = 'FAILURE'
    else:
        if test_case["permission"] in r.json()["permissions"]:
            test_status = 'FAILURE'
        else:
            test_status = 'SUCCESS'

    print(output.format(entry_point=entry_point,
                        username=test_case["username"],
                        password=test_case["password"],
                        expected_permission=test_case["permission"],
                        available_permissions=r.json()["permissions"],
                        permission_result=test_case["result"],
                        test_status=test_status))
    # printing in a file
    if os.environ.get('LOG') == "1":
        with open('/home/SHARED_STORAGE/api_test.log', 'a') as file:
            file.write(output.format(entry_point=entry_point,
                                     username=test_case["username"],
                                     password=test_case["password"],
                                     expected_permission=test_case["permission"],
                                     available_permissions=r.json()["permissions"],
                                     permission_result=test_case["result"],
                                     test_status=test_status))


authentication_test_vector = [
    {"username": "bob",
     "password": "builder",
     "result": True,
     "permission": "v1"
     },
    {"username": "bob",
     "password": "builder",
     "result": False,
     "permission": "v2"
     },
    {"username": "alice",
     "password": "wonderland",
     "result": True,
     "permission": "v1"
     },
    {"username": "alice",
     "password": "wonderland",
     "result": True,
     "permission": "v2"
     }]

for test in authentication_test_vector:
    authorization_test(entry_point, api_address, api_port, test)
