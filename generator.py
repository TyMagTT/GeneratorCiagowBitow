from components import (
    Register
)

from file_reader import (
    open_file
)

from errors import (
    NotJsonError
)

msg_pl = {
        'welcome': 'Witaj użytkowniku! Ten program generuje ciągi bitów.',
        'load_file': 'Podaj ścieżkę prowadzącą do pliku z połączeniami: ',
        'again': 'Spróbuj ponownie:',
        'no_file': 'Nie odnaleniono pliku.',
        'not_json': 'Plik musi mieć rozszerzenie ".json".',
        'no_access': 'Nie masz dostępu do tego pliku.',
        'input_values1': 'Podaj identyfikatory przerzutników,',
        'input_values2': 'ktorym chcesz ustawić wartości początkowe,',
        'input_values3': 'oddzielone przecinkiem i spacją (domyślnie false)',
        'key_error': 'Nie znaleziono przerzutnika o identyfikatorze:',
        'msg_replace': 'Aby zamienić podane id na inne wpisz: "replace"',
        'replace': 'Podaj poprawiony identyfikator: ',
        'msg_skip': 'Aby pominąć podany identyfikator wpisz: "skip"',
        'wrong_choice': 'Polecenie nie rozpoznane.',
        'input_value': 'Podaj wartość przerzutnika',
        'value_not_recognised': 'Błędna wartość, dostępne wartości:',
        'input_choices': '(True/true/1 lub False/false/0)',
        'msg_fixed': 'Aby wybrać ilość ciągów do wygenerowania wpisz: "fixed"',
        'msg_loop': 'Aby wybrać generowanie aż ciąg się zapętli wpisz: "loop"',
        'fixed': 'Podaj liczbę ciągów które chcesz wygenerować: ',
        'not_int': 'Liczba bitów musi być liczbą całkowitą.',
        'generated_strings': 'Wygenerowane ciągi:',
        'space_utilization': 'Stopień wykorzystania przestrzeni:',
        'avg_difference': 'Średnia liczba bitów różniących się między ciągami:',
        'save': 'Zapisać wyniki? "yes" jeśli tak, "no" jeśli nie'
    }


def load_file():
    print(msg_pl['welcome'])
    print(msg_pl['load_file'])
    loading = True
    while loading:
        path = input()
        try:
            flipflops, gates = open_file(path)
            loading = False
        except FileNotFoundError:
            error_message = f'{msg_pl['no_file']} {msg_pl['again']}'
            print(error_message)
        except NotJsonError:
            error_message = f'{msg_pl['not_json']} {msg_pl['again']}'
            print(error_message)
        except PermissionError:
            error_message = f'{msg_pl['no_access']} {msg_pl['again']}'
            print(error_message)
    return Register(flipflops, gates)


def set_starting_values(register):
    msg = f'{msg_pl['input_values1']} {msg_pl['input_values2']}'
    msg = f'{msg} {msg_pl['input_values3']}'
    print(msg)
    input_values = input()
    input_list = input_values.split(', ')
    for key in input_list:
        setting = True
        if key not in register.flipflops:
            correcting = True
            error_message = f'{msg_pl['key_error']} {key}'
            print(error_message)
            while correcting:
                print(msg_pl['msg_replace'])
                print(msg_pl['msg_skip'])
                choice = input()
                if choice == 'replace':
                    while correcting:
                        new_key = input(msg_pl['replace'])
                        if new_key in register.flipflops:
                            key = new_key
                            correcting = False
                        else:
                            error_message = f'{msg_pl['key_error']} {new_key} {msg_pl['again']}'
                            print(error_message)
                elif choice == 'skip':
                    correcting = False
                    setting = False
                else:
                    error_message = f'{msg_pl['wrong_choice']} {msg_pl['again']}'
                    print(error_message)
        while setting:
            msg = f'{msg_pl['input_value']} {key} {msg_pl['input_choices']}: '
            value = input(msg)
            if value == 'True' or value == 'true' or value == '1':
                register.set_value(key, True)
                setting = False
            elif value == 'False' or value == 'false' or value == '0':
                register.set_value(key, False)
                setting = False
            else:
                error_message = f'{msg_pl["value_not_recognised"]} {msg_pl["input_choices"]}'
                print(error_message)


def choose_mode():
    choosing_mode = True
    while choosing_mode:
        print(msg_pl['msg_fixed'])
        print(msg_pl['msg_loop'])
        mode = input()
        if mode == 'fixed':
            setting_fixed = True
            while setting_fixed:
                print(msg_pl['fixed'])
                length = input()
                try:
                    length = int(length)
                    setting_fixed = False
                    choosing_mode = False
                except ValueError:
                    print(msg_pl['not_int'])
                return False, length
        elif mode == 'loop':
            choosing_mode = False
            return True, None
        else:
            error_message = f'{msg_pl['wrong_choice']} {msg_pl['again']}'
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


def calculate_average_difference(string_dict):
    strings = list(string_dict.keys())
    different_bits_sum = 0
    strings_number = len(strings)
    for first_string, second_string in zip(strings, strings[1:]):
        different_bits = sum(1 for b1, b2 in zip(first_string, second_string) if b1 != b2)
        different_bits_sum += different_bits
    return different_bits_sum/(strings_number - 1)


def print_statistics(string_dict, space_utilization, average_difference):
    print(msg_pl['generated_strings'])
    string_list = list(string_dict.keys())
    print(string_list)
    msg = f'{msg_pl['space_utilization']} {space_utilization*100}%'
    print(msg)
    msg = f'{msg_pl['avg_difference']} {average_difference}'
    print(msg)


def save_statistics(string_dict, space_utilization, average_difference):
    string_list = list(string_dict.keys())
    path = 'result.txt'
    with open(path, 'w') as file_handle:
        file_handle.write(f'Generated strings: {string_list}\n')
        file_handle.write(f'Space utilization: {space_utilization*100}%\n')
        file_handle.write(f'Average difference: {average_difference}')


def ask_if_save(string_dict, space_utilization, average_difference):
    asking = True
    while asking:
        print(msg_pl['save'])
        answer = input()
        if answer == 'yes':
            save_statistics(string_dict, space_utilization, average_difference)
            asking = False
        elif answer == 'no':
            asking = False
        else:
            msg = f'{msg_pl['wrong_choice']} {msg_pl['again']}'
            print(msg)


def main():
    register = load_file()
    set_starting_values(register)
    looping, length = choose_mode()
    if looping:
        string_dict = generate_string_looping(register)
    else:
        string_dict = generate_string_fixed(register, length)
    space_utilization = calculate_space_utilization(register, string_dict)
    average_difference = calculate_average_difference(string_dict)

    print_statistics(string_dict, space_utilization, average_difference)
    ask_if_save(string_dict, space_utilization, average_difference)


if __name__ == "__main__":
    main()
