# from gigachat import GigaChat
# import os
# from dotenv import load_dotenv
#
# def get_gigachat_token():
#     load_dotenv()
#     api_key = os.getenv('GIGACHAT_API_KEY')
#     giga = GigaChat(
#         credentials=api_key,
#         ca_bundle_file='russian_trusted_root_ca.cer'
#     )
#     token = giga.get_token()
#     print(f"Токен: {token}")
#     return token
#
# if __name__ == "__main__":
#     get_gigachat_token()

from gigachat import GigaChat
import os
from datetime import datetime
from dotenv import load_dotenv

def get_gigachat_token():
    load_dotenv()
    api_key = os.getenv('GIGACHAT_API_KEY')
    giga = GigaChat(
        credentials=api_key,
        ca_bundle_file='russian_trusted_root_ca.cer'
    )
    token_response = giga.get_token()
    token = token_response.access_token
    expires_at = token_response.expires_at

    # Отладка (можно удалить после проверки)
    # print("DEBUG: expires_at =", expires_at, "type =", type(expires_at))

    # Если значение выглядит как миллисекунды — конвертируем в секунды
    if isinstance(expires_at, int) and expires_at > 10_000_000_000:
        expires_at = expires_at / 1000.0

    try:
        expire_time_formatted = datetime.fromtimestamp(expires_at).strftime("%Y-%m-%d %H:%M:%S")
    except (OSError, ValueError, TypeError) as e:
        # На случай, если всё ещё некорректно
        expire_time_formatted = "Неизвестно (ошибка преобразования времени)"

    return token, expire_time_formatted

if __name__ == "__main__":
    token, expire_time = get_gigachat_token()
    print(f"Токен: {token}")
    print(f"Действителен до: {expire_time}")