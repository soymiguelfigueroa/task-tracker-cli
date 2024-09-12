def get_config(environment='production'):
    if environment == 'test':
        return {
            'file_name': 'test_tasks.json',
        }
    elif environment == 'production':
        return {
            'file_name': 'tasks.json',
        }