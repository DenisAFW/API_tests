# Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост,
# а потом проверяется его наличие на сервере по полю «описание».
# Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts
# с передачей параметров title, description, content.

import requests
import yaml

with open('config.yaml', encoding='utf-8') as fy:
    data = yaml.safe_load(fy)

S = requests.Session()


def test_step1(user_login, post_title):
    result = S.get(url=data['posts'], headers={'X-Auth-Token': user_login}, params={'owner': 'notMe'}).json()['data']
    result_title = [i['title'] for i in result]
    assert post_title in result_title, 'test 1 FAIL'


def test_step2(create_post):
    assert 'Beautiful' in create_post, "Test 2 FAIL"