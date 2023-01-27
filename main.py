from app import magic8ball, clear, continue8ball, loadingscreen
from utils import whitetext

if __name__ == '__main__':
    loadingscreen(100, 0)

    whitetext('Welcome to the magic 8 ball! Would you like to ask me a question?')

    answer = input().lower().strip()

    if answer != 'yes':
        whitetext('Are you sure?')
        confirm = input().lower().strip()

        if confirm == 'yes':
            clear()
            exit()

    whitetext('\nOk! ask me a yes or no question!')
    input()

    magic8ball()
    continue8ball()
