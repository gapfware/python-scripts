from sys import argv
import clipboard
import json


SAVED_DATA = 'clipboard.json'


def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except:
        return {}


def main():
    data = load_data(SAVED_DATA)
    if len(argv) == 2:
        command = argv[1]
        if command == '-save':
            key = input('Enter a key: ')
            data[key] = clipboard.paste()
            save_data(SAVED_DATA, data)
            print('Saved.')
        elif command == '-load':
            key = input('Enter a key: ')
            if key in data:
                clipboard.copy(data[key])
                print('Data copy to clipboard.')
            else:
                print('Key does not exist.')
        elif command == '-list':
            print(data)
        else:
            print('Unknown command')
    else:
        print(f'Cantidad de parametros incorrectos')


if __name__ == '__main__':
    main()
