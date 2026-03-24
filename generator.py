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
        'language': 'Polski (Polska)',
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
        'invalid_value': 'Błędna wartość, dostępne wartości:',
        'input_choices': '(True/true/1 lub False/false/0)',
        'msg_fixed': 'Aby wybrać ilość ciągów do wygenerowania, wpisz: "fixed"',
        'msg_loop': 'Aby wybrać generowanie aż ciąg się zapętli, wpisz: "loop"',
        'fixed': 'Podaj liczbę ciągów które chcesz wygenerować: ',
        'not_int': 'Liczba ciągów musi być liczbą całkowitą.',
        'generated_strings': 'Wygenerowane unikatowe ciągi:',
        'space_utilization': 'Stopień wykorzystania przestrzeni:',
        'avg_diff': 'Średnia liczba bitów różniących się między ciągami:',
        'save': 'Zapisać wyniki? "yes" jeśli tak, "no" jeśli nie'
    }

msg_en = {
        'language': 'English (UK)',
        'welcome': 'Welcome user! This program generates bit strings.',
        'load_file': 'Input a path to a file with your register settings: ',
        'again': 'Try again:',
        'no_file': 'File not found.',
        'not_json': 'File has to have a ".json". extension',
        'no_access': 'No permission to open the file.',
        'input_values1': 'Input flip-flop ids of which you',
        'input_values2': 'want to set starting values,',
        'input_values3': 'separated by comma and space (defaults to false)',
        'key_error': 'Flip-flop not found with id:',
        'msg_replace': 'To replace this id input: "replace"',
        'replace': 'Input the corrected id: ',
        'msg_skip': 'To skip this id input: "skip"',
        'wrong_choice': 'Command not recognised.',
        'input_value': 'Input flip-flop value',
        'invalid_value': 'Incorrect value, avaliable values:',
        'input_choices': '(True/true/1 or False/false/0)',
        'msg_fixed': 'To choose how many strings to generate, input: "fixed"',
        'msg_loop': 'To generate strings until they repeat, input: "loop"',
        'fixed': 'Input a number of strings to generate: ',
        'not_int': 'Strings number has to be an integer.',
        'generated_strings': 'Generated unique strings:',
        'space_utilization': 'Space utilisation percentage:',
        'avg_diff': 'Average bit difference between strings:',
        'save': 'Save results? "yes" to save, "no" to not'
    }


def choose_language():
    choosing_language = True
    print('Choose language option')
    while choosing_language:
        msg = f'en for {msg_en['language']} or pl for {msg_pl['language']}\n'
        answer = input(msg)
        if answer == 'en':
            choosing_language = False
            return msg_en
        elif answer == 'pl':
            choosing_language = False
            return msg_pl
        else:
            print('\nLanguage code not recognised')
            print('Avaliable options:')


def load_file(my_msg):
    print(my_msg['welcome'])
    print(my_msg['load_file'])
    loading = True
    while loading:
        path = input()
        try:
            flipflops, gates = open_file(path)
            loading = False
        except FileNotFoundError:
            error_message = f'{my_msg['no_file']} {my_msg['again']}'
            print(error_message)
        except NotJsonError:
            error_message = f'{my_msg['not_json']} {my_msg['again']}'
            print(error_message)
        except PermissionError:
            error_message = f'{my_msg['no_access']} {my_msg['again']}'
            print(error_message)
    return Register(flipflops, gates)


def set_starting_values(register, my_msg):
    msg = f'{my_msg['input_values1']} {my_msg['input_values2']}'
    msg = f'{msg} {my_msg['input_values3']}'
    print(msg)
    input_values = input()
    input_list = input_values.split(', ')
    for key in input_list:
        setting = True
        if key not in register.flipflops:
            correcting = True
            error_message = f'{my_msg['key_error']} {key}'
            print(error_message)
            while correcting:
                print(my_msg['msg_replace'])
                print(my_msg['msg_skip'])
                choice = input()
                if choice == 'replace':
                    while correcting:
                        new_key = input(my_msg['replace'])
                        if new_key in register.flipflops:
                            key = new_key
                            correcting = False
                        else:
                            msg = f'{my_msg['key_error']} {new_key}'
                            msg = f'{msg} {my_msg['again']}'
                            print(msg)
                elif choice == 'skip':
                    correcting = False
                    setting = False
                else:
                    msg = f'{my_msg['wrong_choice']} {my_msg['again']}'
                    print(msg)
        while setting:
            msg = f'{my_msg['input_value']} {key} {my_msg['input_choices']}: '
            value = input(msg)
            if value == 'True' or value == 'true' or value == '1':
                register.set_value(key, True)
                setting = False
            elif value == 'False' or value == 'false' or value == '0':
                register.set_value(key, False)
                setting = False
            else:
                msg = f'{my_msg["invalid_value"]} {my_msg["input_choices"]}'
                print(msg)


def choose_mode(my_msg):
    choosing_mode = True
    while choosing_mode:
        print(my_msg['msg_fixed'])
        print(my_msg['msg_loop'])
        mode = input()
        if mode == 'fixed':
            setting_fixed = True
            while setting_fixed:
                print(my_msg['fixed'])
                length = input()
                try:
                    length = int(length)
                    setting_fixed = False
                    choosing_mode = False
                except ValueError:
                    print(my_msg['not_int'])
                return False, length
        elif mode == 'loop':
            choosing_mode = False
            return True, None
        else:
            error_message = f'{my_msg['wrong_choice']} {my_msg['again']}'
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
    for first, second in zip(strings, strings[1:]):
        different_bits = sum(1 for b1, b2 in zip(first, second) if b1 != b2)
        different_bits_sum += different_bits
    return different_bits_sum/(strings_number - 1)


def print_statistics(string_dict, space_utilization, average_difference, my_msg):
    print(my_msg['generated_strings'])
    string_list = list(string_dict.keys())
    print(string_list)
    msg = f'{my_msg['space_utilization']} {space_utilization*100}%'
    print(msg)
    msg = f'{my_msg['avg_diff']} {average_difference}'
    print(msg)


def save_statistics(string_dict, space_utilization, average_difference):
    string_list = list(string_dict.keys())
    path = 'result.txt'
    with open(path, 'w') as file_handle:
        file_handle.write(f'Generated strings: {string_list}\n')
        file_handle.write(f'Space utilization: {space_utilization*100}%\n')
        file_handle.write(f'Average difference: {average_difference}')


def ask_if_save(string_dict, space_utilization, average_difference, my_msg):
    asking = True
    while asking:
        print(my_msg['save'])
        answer = input()
        if answer == 'yes':
            save_statistics(string_dict, space_utilization, average_difference)
            asking = False
        elif answer == 'no':
            asking = False
        else:
            msg = f'{my_msg['wrong_choice']} {my_msg['again']}'
            print(msg)


def main():
    language = choose_language()

    register = load_file(language)

    set_starting_values(register, language)
    looping, length = choose_mode(language)
    if looping:
        string_dict = generate_string_looping(register)
    else:
        string_dict = generate_string_fixed(register, length)
    space_utilization = calculate_space_utilization(register, string_dict)
    average_difference = calculate_average_difference(string_dict)

    print_statistics(string_dict, space_utilization, average_difference, language)
    ask_if_save(string_dict, space_utilization, average_difference, language)


if __name__ == "__main__":
    main()
