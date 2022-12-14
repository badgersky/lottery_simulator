from random import shuffle


def get_winning_nums():
    """function generates 6 random numbers in range 1-49"""
    numbers = list(range(1, 50))
    shuffle(numbers)
    return numbers[:6]


def get_numbers():
    """function takes input numbers from user, checks conditions under which input is valid"""
    print(f'Remember that numbers cannot be repeated and must be in range 1-49')
    numbers = []
    while len(numbers) < 6:
        try:
            number = int(input(f'Enter a number: '))
            if number not in numbers and number in range(1, 49):
                numbers.append(number)
        except ValueError:
            print(f'Wrong input!')
    return numbers


def check_win():
    """function compares numbers chosen by human with numbers generated by computer"""
    secret_numbers = get_winning_nums()
    chosen_numbers = get_numbers()
    secret_numbers.sort()
    chosen_numbers.sort()
    print(f'Numbers chosen by you: ' + ' '.join([str(n) for n in chosen_numbers]))
    print(f'Numbers generated by a computer: ' + ' '.join([str(n) for n in secret_numbers]))
    same_nums = [n for n in chosen_numbers if n in secret_numbers]
    return f'You have guessed {len(same_nums)} numbers right.'


if __name__ == '__main__':
    print(check_win())
