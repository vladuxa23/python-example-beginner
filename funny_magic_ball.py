import random

messages = ['Да',
            'Несомненно',
            'Спроси снова',
            'Мой ответ нет',
            'Очень сомнительно',
            'Это определенно так',
            'Перспективы не очень хорошие',
            'Ответ туманный. Попробуй снова',
            'Сконцентрируйся и спроси заново',
           ]
print(messages[random.randint(0, len(messages)-1)])    