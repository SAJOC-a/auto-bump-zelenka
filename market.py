import requests
import time
from loguru import logger

api_base_url = 'https://api.lzt.market' # URL Api
api_token = 'токен' # Token from forum
item_Ids = [43888272]  # List of accounts
bump_interval = 43200  # The interval of raising accounts in seconds

headers = {'Authorization': f'Bearer {api_token}'}

def bump_thread(itemId):
    url = f'{api_base_url}/{itemId}/bump'
    try:
        response = requests.post(url, headers=headers)

        if response.status_code == 200 and 'errors' not in response.json():
            logger.success(f'Аккаунт {itemId} успешно поднят!')
        else:
            logger.error(f'Не удалось поднять аккаунт {itemId}: {response.status_code} - {response.json()}')
    except:
        logger.error('Запрос не был выполнен')


while True:
    for itemId in item_Ids:
        bump_thread(itemId)
        time.sleep(5)
    logger.info(f'Цикл окончен, ждем {bump_interval} секунд')
    time.sleep(bump_interval)
