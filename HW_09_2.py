notebook = {"Tania":['8446353', '83746453']}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Not enough params. Print help'
    return inner


def help(*args):
    return '''Hello, thats your notebook!
    To adding a new contact - type add
    To change a contact type - change
    To close the app type - exite, close, good bye
    To show someone phone type - phone
    To show all contactstype - show all'''

@input_error
def add(*args):
    for i in args:
        notebook.update(i)
    return f'The person has been added to your notebook'

def exit(*args):
    return 'Good Bye!'

def no_command(*args):
    return 'Unknown command, try again'

def show_all(*args):
    return '\n'.join([f'{k} : {", ".join(v)}' for k, v in notebook.items()])

def hello(*args):
    return 'How can I help you?'

def phone(*kwargs):
    for name in kwargs:
        for name, phone in notebook.items():
            if name:
                return f'That\'s the contacts what you are looking for - {phone}'


COMMANDS = {
            add: ['add', 'change'],
            exit: ['exit', 'good bye', 'close'],
            show_all: ['show all'],
            hello: ['hello', 'help'],
            phone: ['phone']
            }

def command_handler(text):
    for command, kword_list in COMMANDS.items():
        for kword in kword_list:
            if text.startswith(kword):
                clear_text = text.replace(kword, '').strip()
                if clear_text:             
                    list_of_param = clear_text.split()
                    name = list_of_param[0]              
                    contacts = list_of_param[1:]               
                    return command, {name: contacts}
                else:
                    return command, clear_text
    return no_command, None

def main():
    print(help())
    while True:
        user_input = input('>>> ').lower()
        command, data = command_handler(user_input)
        print(command(data))
        if command == exit:
            break


if __name__ == '__main__':
    main()   