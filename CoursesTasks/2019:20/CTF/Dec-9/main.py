from random import randrange

hello_message = '''Hello, i am joke machine. Type 'commands' to get list of commands'''

allowed_commands = ['get_joke', 'help', 'exit', 'debug']


def get_flag():
    f = open('flag.txt', 'r')
    data = f.readlines()
    f.close()
    return ''.join(data)


def get_joke():
    jokes = [
        'Can a kangaroo jump higher than a house? Of course, a house doesntt jump at all.',
        ' Anton, do you think I’m a bad mother?\n My name is Paul.',
        'My wife’s cooking is so bad we usually pray after our food',
        '''What is the longest word in the English language? 'Smiles'.  Because there is a mile between its first and 
        last letters. '''
    ]
    return jokes[randrange(0, len(jokes))]


def get_help():
    return hello_message


def debug():
    f = open('main.py')
    data = f.readlines()
    f.close()
    return ''.join(data)


def commands():
    return ', '.join(allowed_commands)


def e_exit():
    return 'Bye-bye!!Seeeya!'


all_commands = {
    'get_joke': get_joke, 'help': get_help, 'exit': e_exit, 'debug': debug, 'get_flag': get_flag, 'commands': commands
}

not_allowed_tokens = ['get_flag']


def validate_user_data(client_data):
    bad_data = False
    error_message = 'Bad commands: '
    for i in not_allowed_tokens:
        if i in client_data:
            client_data = client_data.replace(i, '')
            error_message += i + ", "
            bad_data = True
    return bad_data, error_message, client_data


def main():
    print(hello_message)
    print('>', end=' ')
    command = input()
    while command != 'exit' and len(command) > 0:
        flag, message, command = validate_user_data(command)
        if flag:
            print(message)
        if command in all_commands.keys():
            print(all_commands[command]())
        else:
            print('Bad command')
        print('>', end=' ')
        command = input()

main()
