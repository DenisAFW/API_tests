import pytest
import requests
import yaml

S = requests.Session()

with open('config.yaml', encoding='utf-8') as fy:
    data = yaml.safe_load(fy)


@pytest.fixture()
def user_login():
    result = S.post(url=data['url'], data={'username': data['login'], 'password': data['passwd']})
    response_token = result.json()['token']
    # token = response_json.get('token')
    return response_token


@pytest.fixture()
def create_post():
    result = requests.post(url=data['posts'], headers={"X-Auth-Token": data['token']},
                           data={'username': data['login'],
                                 'password': data['passwd'],
                                 'title': 'Ромашки',
                                 'description': 'Beautiful',
                                 'content': 'O_o'})
    return result.json()['description']


@pytest.fixture()
def post_title():
    return 'ДЗ к Семинару 3'
