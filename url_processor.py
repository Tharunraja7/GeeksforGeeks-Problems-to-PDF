import requests
import json

def convert_geeksforgeeks_url(input_url):
    difficulty_mapping = {'School': '-2', 'Basic': '-1', 'Easy': '0', 'Medium': '1', 'Hard': '2'}
    for difficulty, value in difficulty_mapping.items():
        input_url = input_url.replace(difficulty, value)
    return input_url

def process_url(input_user_url):
    base_url = "https://practiceapi.geeksforgeeks.org/api/vr/problems/?pageMode=explore&page={page}"
    concatenated_url = base_url + '&' + convert_geeksforgeeks_url(input_user_url)

    urls = []
    page = 1
    while True:
        url = concatenated_url.format(page=page)
        response = requests.get(url)
        data = json.loads(response.text)

        if 'results' in data:
            for result in data['results']:
                urls.append(result['problem_url'])
        else:
            break

        if data.get('next'):
            page += 1
        else:
            break

    return urls
