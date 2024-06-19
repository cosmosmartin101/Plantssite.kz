from pywebio.input import input
from pywebio.output import put_text
from pywebio import start_server

def main():
    name = input("What's your name?")
    put_text(f'Hello, {name}!')

if __name__ == '__main__':
    start_server(main, port=8080)