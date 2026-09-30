
import requests
import sys

def request_word_from_api(category, wd_length):
    url = 'https://random-words-api.kushcreates.com/api'
    try:
        if wd_length == 'any':
            request_string = {'language': 'en', 'category': category, 'type': 'lowercase', 'words': 1}
        else:
            request_string = {'language': 'en', 'category': category, 'length': wd_length, 'type': 'lowercase', 'words': 1}
        request_params = request_string
        response = requests.get(url, headers={"Accept": "application/json"}, params=request_params)
        if response.ok:
            data = response.json()
            # print(data)
            if data is None:
                print(f'There are no {wd_length} words in the {category} category.')
                return None
            else:
                word = (data[0]['word'])
            return word
        else:
            print(f'Encountered an error: HTTP Status Code: {response.status_code}')
            print(f"Please try again later")
            sys.exit(0)
    except requests.exceptions.ConnectionError  as e:
        print(f"Connection failed! The server might be down or your internet is disconnected.")
        print(f"Details: {e}")
        sys.exit(0)
    except requests.exceptions.Timeout:
        print("The request timed out.")
        sys.exit(0)
    except requests.exceptions.RequestException as e:
        print(f"A generic requests error occurred: {e}")
        sys.exit(0)