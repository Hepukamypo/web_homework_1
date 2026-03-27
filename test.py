import subprocess
import pytest
import os

INTERPRETER = 'python'

def run_script(filename, input_data=None):
    proc = subprocess.run(
        [INTERPRETER, filename],
        input='\n'.join(input_data if input_data else []),
        capture_output=True,
        text=True,
        check=False
    )
    return proc.stdout.strip()


# ---------- 1. Hello World ----------

def test_hello_world():
    assert run_script('hello.py') == 'Hello, World!'


# ---------- 2. Python If-Else ----------

@pytest.mark.parametrize("n, expected", [
    ('1', 'Weird'),
    ('2', 'Not Weird'),
    ('3', 'Weird'),
    ('4', 'Not Weird'),
    ('5', 'Weird'),
    ('6', 'Weird'),
    ('20', 'Weird'),
    ('22', 'Not Weird'),
    ('100', 'Not Weird'),
])
def test_python_if_else(n, expected):
    assert run_script('python_if_else.py', [n]) == expected


# ---------- 3. Arithmetic Operators ----------

@pytest.mark.parametrize("input_data, expected", [
    (['1', '2'], ['3', '-1', '2']),
    (['10', '5'], ['15', '5', '50']),
    (['100', '1'], ['101', '99', '100']),
    (['0', '5'], ['5', '-5', '0']),
    (['-3', '2'], ['-1', '-5', '-6']),
])
def test_arithmetic_operators(input_data, expected):
    assert run_script('arithmetic_operators.py', input_data).splitlines() == expected


# ---------- 4. Division ----------

@pytest.mark.parametrize("input_data", [
    (['3', '5']),
    (['10', '2']),
    (['5', '1']),
    (['0', '3']),
    (['-6', '3']),
])
def test_division(input_data):
    out = run_script('division.py', input_data).splitlines()
    assert len(out) == 2


# ---------- 5. Loops ----------

@pytest.mark.parametrize("n, expected", [
    ('1', ['0']),
    ('3', ['0', '1', '4']),
    ('5', ['0', '1', '4', '9', '16']),
    ('2', ['0', '1']),
])
def test_loops(n, expected):
    assert run_script('loops.py', [n]).splitlines() == expected


# ---------- 6. Print Function ----------

@pytest.mark.parametrize("n, expected", [
    ('1', '1'),
    ('5', '12345'),
    ('10', '12345678910'),
    ('2', '12'),
])
def test_print_function(n, expected):
    assert run_script('print_function.py', [n]) == expected


# ---------- 7. Second Score ----------

@pytest.mark.parametrize("input_data, expected", [
    (['5', '2 3 6 6 5'], '5'),
    (['4', '10 9 8 7'], '9'),
    (['3', '1 1 2'], '1'),
    (['6', '1 2 3 4 5 6'], '5'),
    (['5', '5 5 4 4 3'], '4'),
])
def test_second_score(input_data, expected):
    assert run_script('second_score.py', input_data) == expected


# ---------- 8. Nested List ----------

def test_nested_list_multiple():
    data = [
        '5',
        'Harry', '37.21',
        'Berry', '37.21',
        'Tina', '37.2',
        'Akriti', '41',
        'Harsh', '39'
    ]
    out = run_script('nested_list.py', data).splitlines()
    assert out == ['Berry', 'Harry']


def test_nested_list_simple():
    data = ['3', 'A', '10', 'B', '20', 'C', '30']
    assert run_script('nested_list.py', data) == 'B'


def test_nested_list_float():
    data = ['3', 'X', '1.1', 'Y', '2.2', 'Z', '3.3']
    assert run_script('nested_list.py', data) == 'Y'


# ---------- 9. Lists ----------

def test_lists_example():
    data = [
        '12',
        'insert 0 5',
        'insert 1 10',
        'insert 0 6',
        'print',
        'remove 6',
        'append 9',
        'append 1',
        'sort',
        'print',
        'pop',
        'reverse',
        'print'
    ]
    out = run_script('lists.py', data).splitlines()
    assert out == [
        '[6, 5, 10]',
        '[1, 5, 9, 10]',
        '[9, 5, 1]'
    ]


def test_lists_append_print():
    data = ['3', 'append 1', 'append 2', 'print']
    assert run_script('lists.py', data) == '[1, 2]'


def test_lists_sort():
    data = ['4', 'append 3', 'append 1', 'sort', 'print']
    assert run_script('lists.py', data) == '[1, 3]'


# ---------- 10. Swap Case ----------

@pytest.mark.parametrize("s, expected", [
    ('Www.MosPolytech.ru', 'wWW.mOSpOLYTECH.RU'),
    ('Pythonist 2', 'pYTHONIST 2'),
    ('ABC', 'abc'),
    ('abc', 'ABC'),
])
def test_swap_case(s, expected):
    assert run_script('swap_case.py', [s]) == expected


# ---------- 11. Split and Join ----------

@pytest.mark.parametrize("s, expected", [
    ('this is a string', 'this-is-a-string'),
    ('hello world', 'hello-world'),
    ('a b c', 'a-b-c'),
])
def test_split_and_join(s, expected):
    assert run_script('split_and_join.py', [s]) == expected


# ---------- 12. Max Word ----------

def test_max_word_basic(tmp_path):
    text = "hello amazing unbelievable world"
    file = tmp_path / "example.txt"
    file.write_text(text)
    os.replace(file, "example.txt")
    assert run_script('max_word.py') == 'unbelievable'


def test_max_word_multiple(tmp_path):
    text = "biggest longest biggest"
    file = tmp_path / "example.txt"
    file.write_text(text)
    os.replace(file, "example.txt")
    out = run_script('max_word.py').splitlines()
    assert 'biggest' in out


# ---------- 13. Price Sum ----------

def test_price_sum_basic(tmp_path):
    csv = "name,child,adult,pensioner\ncheese,5,10,15\nmilk,15,5,20\n"
    file = tmp_path / "products.csv"
    file.write_text(csv)
    os.replace(file, "products.csv")
    out = run_script('price_sum.py')
    assert len(out.split()) == 3


def test_price_sum_only_adult(tmp_path):
    csv = "name,child,adult,pensioner\ncheese,5,10,15\nmilk,15,5,20\n"
    file = tmp_path / "products.csv"
    file.write_text(csv)
    os.replace(file, "products.csv")
    out = run_script('price_sum.py').split()
    assert float(out[0]) == 20.00


# ---------- 14. Anagram ----------

@pytest.mark.parametrize("a, b, expected", [
    ('listen', 'silent', 'YES'),
    ('hello', 'world', 'NO'),
    ('abc', 'cba', 'YES'),
    ('aabb', 'bbaa', 'YES'),
    ('abc', 'abcd', 'NO'),
])
def test_anagram(a, b, expected):
    assert run_script('anagram.py', [a, b]) == expected


# ---------- 15. Metro ----------

def test_metro_basic():
    data = ['3', '1 5', '2 6', '4 8', '4']
    assert run_script('metro.py', data) == '3'


def test_metro_single():
    data = ['1', '1 10', '5']
    assert run_script('metro.py', data) == '1'


def test_metro_none():
    data = ['1', '1 2', '5']
    assert run_script('metro.py', data) == '0'


# ---------- 16. Minion Game ----------

def test_minion_game_banana():
    assert run_script('minion_game.py', ['BANANA']) == 'Стюарт 12'


def test_minion_game_all_vowels():
    out = run_script('minion_game.py', ['AEIOU'])
    assert 'Кевин' in out or 'Kevin' in out


# ---------- 17. Leap Year ----------

@pytest.mark.parametrize("year, expected", [
    ('2000', 'True'),
    ('1900', 'False'),
    ('2024', 'True'),
    ('2023', 'False'),
    ('2400', 'True'),
])
def test_is_leap(year, expected):
    assert run_script('is_leap.py', [year]) == expected


# ---------- 18. Happiness ----------

def test_happiness_basic():
    data = ['3 2', '1 5 3', '3 1', '5 7']
    assert run_script('happiness.py', data) == '1'


def test_happiness_zero():
    data = ['3 1', '1 2 3', '4', '5']
    assert run_script('happiness.py', data) == '0'


# ---------- 19. Pirate Ship ----------

def test_pirate_ship_basic():
    data = ['10 2', 'gold 5 100', 'silver 10 50']
    out = run_script('pirate_ship.py', data)
    assert 'gold' in out


def test_pirate_ship_fraction():
    data = ['5 1', 'gold 10 100']
    out = run_script('pirate_ship.py', data)
    assert 'gold' in out


# ---------- 20. Matrix Multiplication ----------

def test_matrix_mult_2x2():
    data = ['2', '1 2', '3 4', '5 6', '7 8']
    out = run_script('matrix_mult.py', data).splitlines()
    assert out == ['19 22', '43 50']


def test_matrix_mult_identity():
    data = ['2', '1 0', '0 1', '5 6', '7 8']
    out = run_script('matrix_mult.py', data).splitlines()
    assert out == ['5 6', '7 8']


def test_matrix_mult_zero():
    data = ['2', '0 0', '0 0', '5 6', '7 8']
    out = run_script('matrix_mult.py', data).splitlines()
    assert out == ['0 0', '0 0']