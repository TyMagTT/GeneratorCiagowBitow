from components import (
    Register
)

from file_reader import (
    open_file
)

from errors import (
    NotJsonError
)

messages_pl = {
        'welcome': 'Witaj użytkowniku! Ten program służy do generowania ciągów bitów na podstawie rejestru',
        'load_file': 'Podaj ścieżkę prowadzącą do pliku z połączeniami: ',
        'again': 'Spróbuj ponownie:',
        'no_file': 'Nie odnaleniono pliku.',
        'not_json': 'Plik musi mieć rozszerzenie ".json".',
        'no_access': 'Nie masz dostępu do tego pliku.',
        'input_values': 'Podaj identyfikatory przerzutników, ktorym chcesz ustawić wartości początkowe, oddzielone przecinkiem i spacją (domyślnie false)',
        'key_error': 'Nie znaleziono przerzutnika o identyfikatorze:',
        'choose_replace': 'Aby zamienić podany identyfikator na inny wpisz: "replace"',
        'replace': 'Podaj poprawiony identyfikator: ',
        'choose_skip': 'Aby pominąć podany identyfikator wpisz: "skip"',
        'wrong_choice': 'Polecenie nie rozpoznane.',
        'input_value': 'Podaj wartość przerzutnika',
        'value_not_recognised': 'Błędna wartość, dostępne wartości:',
        'input_choices': '(True/true/1 lub False/false/0)',
        'choose_fixed': 'Aby wybrać konkretną długość ciągu do wygenerowania wpisz: "fixed"',
        'choose_loop': 'Aby wybrać generowanie aż ciąg się zapętli wpisz: "loop"',
        'fixed': 'Podaj liczbę ciągów które chcesz wygenerować: ',
        'not_int': 'Liczba bitów musi być liczbą całkowitą.',
    }


def load_file():
    print(messages_pl['welcome'])
    print(messages_pl['load_file'])
    loading = True
    while loading:
        path = input()
        try:
            flipflops, gates = open_file(path)
            loading = False
        except FileNotFoundError:
            error_message = f'{messages_pl['no_file']} {messages_pl['again']}'
            print(error_message)
        except NotJsonError:
            error_message = f'{messages_pl['not_json']} {messages_pl['again']}'
            print(error_message)
        except PermissionError:
            error_message = f'{messages_pl['no_access']} {messages_pl['again']}'
            print(error_message)
        except Exception as e:
            print(e)
    return Register(flipflops, gates)


def set_starting_values(register):
    print(messages_pl['input_values'])
    input_values = input()
    input_list = input_values.split(', ')
    for key in input_list:
        setting = True
        if key not in register.flipflops:
            correcting = True
            error_message = f'\n{messages_pl['key_error']} {key}\n'
            print(error_message)
            while correcting:
                print(messages_pl['choose_replace'])
                print(messages_pl['choose_skip'])
                choice = input()
                if choice == 'replace':
                    while correcting:
                        new_key = input(messages_pl['replace'])
                        if new_key in register.flipflops:
                            key = new_key
                            correcting = False
                        else:
                            error_message = f'\n{messages_pl['key_error']} {new_key} {messages_pl['again']}'
                            print(error_message)
                elif choice == 'skip':
                    correcting = False
                    setting = False
                else:
                    error_message = f'{messages_pl['wrong_choice']} {messages_pl['again']}'
                    print(error_message)
        while setting:
            msg = f'\n{messages_pl['input_value']} {key} {messages_pl['input_choices']}: '
            value = input(msg)
            if value == 'True' or value == 'true' or value == '1':
                register.set_value(key, True)
                setting = False
            elif value == 'False' or value == 'false' or value == '0':
                register.set_value(key, False)
                setting = False
            else:
                error_message = f'{messages_pl["value_not_recognised"]} {messages_pl["input_choices"]}'
                print(error_message)


def choose_mode():
    choosing_mode = True
    while choosing_mode:
        print('\n')
        print(messages_pl['choose_fixed'])
        print(messages_pl['choose_loop'])
        mode = input()
        if mode == 'fixed':
            setting_fixed = True
            while setting_fixed:
                print(messages_pl['fixed'])
                length = input()
                try:
                    length = int(length)
                    setting_fixed = False
                    choosing_mode = False
                except ValueError:
                    print(messages_pl['not_int'])
                return False, length
        elif mode == 'loop':
            choosing_mode = False
            return True, None
        else:
            error_message = f'{messages_pl['wrong_choice']} {messages_pl['again']}'
            print(error_message)


def generate_string_fixed(register, length):
    string_dict = {}
    while length > 0:
        string = ""
        for flipflop in register.flipflops.values():
            if flipflop.output():
                char = '1'
            else:
                char = '0'
            string += char
        if string in string_dict:
            string_dict[string] += 1
        else:
            string_dict[string] = 1
        register.step()
        length -= 1
    return string_dict


def generate_string_looping(register):
    looping = True
    string_dict = {}
    while looping:
        string = ""
        for flipflop in register.flipflops.values():
            if flipflop.output():
                char = '1'
            else:
                char = '0'
            string += char
        if string in string_dict:
            if string_dict[string] >= 2:
                looping = False
                return string_dict
            string_dict[string] += 1
        else:
            string_dict[string] = 1
        register.step()


def calculate_space_utilization(register, strings):
    flipflop_number = len(register.flipflops)
    max_combinations = pow(2, flipflop_number)
    generated_number = len(strings)
    return generated_number/max_combinations


def calculate_average_difference(register, strings):
    for string in strings:
        pass


def main():
    # load file
    # set starting values
    # choose output
    # mode (fixed number/until loop)
    # generate
    # save?
    # compare

    register = load_file()
    set_starting_values(register)
    looping, length = choose_mode()

    if looping:
        string_dict = generate_string_looping(register)
    else:
        string_dict = generate_string_fixed(register, length)

    print(string_dict)
    print(calculate_space_utilization(register, string_dict))


if __name__ == "__main__":
    main()
