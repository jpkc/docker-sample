# Content Test

# In this last test, we check that the API works as it should. We will test the
# following sentences with the alice account:
#   life is beautiful
#   that sucks

# For each version of the model, we should get a positive score for the first sentence and
# a negative score for the second sentence. The test will consist in checking the
# positivity or negativity of the score.


import os
import requests

api_address = 'TOY_MODEL'
api_port = 8000


def sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"


def content_test(api_address, api_port, test_case):
    r = requests.get(
        url='http://{address}:{port}/{entry_point}'.format(address=api_address,
                                                           port=api_port,
                                                           entry_point=test_case["entry_point"]),
        params=test_case
    )

    output = '''
    ============================
        Content test
    ============================
    request done at "/{entry_point}"
    | username="{username}"
    | password="{password}"
    Sentence = {sentence}
    Expected sentiment = {expected_sentiment}
    Score = {score}
    ==>  {test_status}
    '''

    if float(test_case["score"]) * float(r.json()["score"]) > 0:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'

    print(output.format(entry_point=test_case["entry_point"],
                        username=test_case["username"],
                        password=test_case["password"],
                        sentence=test_case["sentence"],
                        expected_sentiment=sentiment(r.json()["score"]),
                        score=r.json()["score"],
                        test_status=test_status))

    # printing in a file
    if os.environ.get('LOG') == "1":
        with open('/home/SHARED_STORAGE/api_test.log', 'a') as file:
            file.write(output.format(entry_point=test_case["entry_point"],
                                     username=test_case["username"],
                                     password=test_case["password"],
                                     sentence=test_case["sentence"],
                                     expected_sentiment=sentiment(r.json()["score"]),
                                     score=r.json()["score"],
                                     test_status=test_status))


authentication_test_vector = [
    {"username": "alice",
     "password": "wonderland",
     "score": 1,
     "entry_point": "v1/sentiment",
     "sentence": "life is beautiful"
     },
    {"username": "alice",
     "password": "wonderland",
     "score": -1,
     "entry_point": "v2/sentiment",
     "sentence": "that sucks"
     }]

for test in authentication_test_vector:
    content_test(api_address, api_port, test)
