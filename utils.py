import requests


def print_tasks():
    response = requests.get('http://127.0.0.1:5000/tasks')
    tasks = response.json()['tasks']
    for task in tasks:
        print(f"ID: {task['id']}, Задача: {task['title']}, "
              f"Статус: {'Сделана' if task['done'] else 'Не сделана'}")


def create_task(title: str):
    new_task = {'title': title}
    response = requests.post('http://localhost:5000/tasks', json=new_task)

    if response.status_code == 201:
        print('Задача создана!')
    else:
        print('Ошибка при создании задачи.')


def make_task_done(task_id: int):
    response = requests.put(f'http://localhost:5000/tasks/{task_id}',
                            json={'done': True})

    if response.status_code == 200:
        print('Статус задачи изменен!')
    else:
        print('Ошибка при изменении статуса задачи.')


def del_task(task_id: int):
    response = requests.delete(f'http://localhost:5000/tasks/{task_id}')

    if response.status_code == 200:
        print('Задача удалена!')
    else:
        print('Ошибка при удалении задачи.')
