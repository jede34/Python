def send_data(data):
    pass

def process_data(input_data, send_data_fn):
    updated_data = input_data.copy()

    send_data_fn(updated_data)

process_data({'name': 'Ivan'}, send_data)