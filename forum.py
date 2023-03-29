import requests
import time
from loguru import logger

api_base_url = 'https://api.zelenka.guru' # URL Api
api_token = 'токен' # Token from forum
thread_ids = [4512549, 3870105, 4141642, 4677302, 4926839]  # List of topics
bump_interval = 43200  # The interval of raising the topic in seconds

headers = {'Authorization': f'Bearer {api_token}'}

def bump_thread(thread_id):
    url = f'{api_base_url}/threads/{thread_id}/bump'
    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200 and 'errors' not in response.json():
            logger.success(f'Тема {thread_id} успешно поднята!')
        else:
            logger.error(f'Не удалось поднять тему {thread_id}: {response.status_code} - {response.text}')
    except:
        logger.error('Запрос не был выполнен')


while True:
    for thread_id in thread_ids:
        bump_thread(thread_id)
        time.sleep(5)
    logger.info(f'Цикл окончен, ждем {bump_interval} секунд')
    time.sleep(bump_interval)
