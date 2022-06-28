from config import init_config
from interface.main_menu import main_menu
from tools import clear_console


def main():
    init_config()
    clear_console()
    main_menu()


if __name__ == "__main__":
    main()
