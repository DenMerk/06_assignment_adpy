import pytest
import first_assignment as fa

geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]


@pytest.mark.parametrize(
    'country', [
        'Франция', 'Индия', 'Португалия'
    ]
)
def test_geo_logs(country):
    for geo_log in fa.geo_logs_function(geo_logs):
        for key, value in geo_log.items():
            assert country != value[1]


@pytest.mark.parametrize(
    'id_for_checking', [
        213, 15, 80, '54'
    ]
)
def test_unique_ids_reader(id_for_checking):
    """проверка на наличие повторяющихся элементов и элементов, которых не было в начальной выборке"""
    res_lst = fa.unique_ids_reader(ids)
    if id_for_checking in res_lst:
        res_lst.remove(id_for_checking)
    assert id_for_checking not in res_lst


@pytest.mark.parametrize(
    'percentage', [100, 120]
)
def test_search_query_distribution(percentage):
    """Праверка, что в сумме все запросы дают 100 %"""
    res = fa.search_query_distribution(queries)
    sum = 0
    for key, value in res.items():
        sum += value
    assert percentage == sum
