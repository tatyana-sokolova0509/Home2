import pytest
from string_utils import StringUtils

string_utils = StringUtils()


# тесты для функции capitalize
@pytest.mark.positive
@pytest.mark.parametrize('input_text, result',
                         [('колобок', 'Колобок'),
                          ('rain', 'Rain'),
                          ('привет', 'Привет')])
def test_positive_capitalize(input_text, result):
    assert string_utils.capitalize(input_text) == result


@pytest.mark.negative
@pytest.mark.parametrize('input_text, result',
                         [('789', '789'),
                          ('?rain', '?rain'),
                          ('   ', '   ')])
def test_negative_capitalize(input_text, result):
    assert string_utils.capitalize(input_text) == result


# тесты для функции trim
@pytest.mark.positive
@pytest.mark.parametrize('input_text, result',
                         [(' телефон', 'телефон'),
                          ('  rain', 'rain'),
                          ('   привет, медведь', 'привет, медведь'),
                          ('  964', '964'),
                          ('мышь', 'мышь'),
                          ('  перекресток  ', 'перекресток  ')
                          ])
def test_positive_trim(input_text, result):
    assert string_utils.trim(input_text) == result


@pytest.mark.negative
@pytest.mark.parametrize('input_text, result',
                         [('', ''),
                          (' ', ''),
                          ('  ', '')
                          ])
def test_negative_trim(input_text, result):
    assert string_utils.trim(input_text) == result


# тесты для функции contains
@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, result',
                         [('колобок', 'к', True),
                          ('rain', 'i', True),
                          ('зонт78', '7', True),
                          ('чемодан, вокзал', ',', True),
                          ('халат', 'А', False),
                          ('Улица. Фонарь. Аптека', ' ', True),
                          ('привет', 'ж', False)])
def test_positive_contains(string, symbol, result):
    assert string_utils.contains(string, symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, result',
                         [('дом мой достроен', '', True),
                          ('', 'ф', False),
                          ('', '', True)])
def test_negative_contains(string, symbol, result):
    assert string_utils.contains(string, symbol) == result

# тесты для функции delete_symbol
@pytest.mark.positive
@pytest.mark.parametrize('string, symbol, result',
                         [('колобок', 'к', 'олобо'),
                          ('rain', 'i', 'ran'),
                          ('зонт78', '7', 'зонт8'),
                          ('чемодан, вокзал, перрон', ' ', 'чемодан,вокзал,перрон'),
                          ('халАт', 'А', 'халт')])
def test_positive_delete_symbol(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result


@pytest.mark.negative
@pytest.mark.parametrize('string, symbol, result',
                         [('дом мой достроен', 'х', 'дом мой достроен' ),
                          ('филин, фазан', '', 'филин, фазан'),
                          ('', 'к', '')])
def test_negative_delete_symbol(string, symbol, result):
    assert string_utils.delete_symbol(string, symbol) == result