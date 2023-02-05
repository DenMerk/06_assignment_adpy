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


def geo_logs_function(geo_logs_lst):
    only_rus_lst = []
    for item in geo_logs_lst:
        if list(item.values())[0][1] == 'Россия':
            only_rus_lst.append(item)
    return only_rus_lst


def unique_ids_reader(ids_dict):
    unique_ids_set = set()
    for key, value in ids_dict.items():
        for geo_id in value:
            unique_ids_set.add(geo_id)
    return list(unique_ids_set)


def search_query_distribution(search_query):
    one_word_query = 0
    two_words_query = 0
    three_words_query = 0
    many_words_query = 0
    distribution_dict = {}
    for query in search_query:
        if len(query.split()) == 1:
            one_word_query += 1
        elif len(query.split()) == 2:
            two_words_query += 1
        elif len(query.split()) == 3:
            three_words_query += 1
        else:
            many_words_query += 1
    distribution_dict['one word'] = one_word_query / len(search_query) * 100
    distribution_dict['two words'] = two_words_query / len(search_query) * 100
    distribution_dict['three words'] = three_words_query / len(search_query) * 100
    distribution_dict['many words'] = 100 - (distribution_dict['one word'] + distribution_dict['two words']
                                             + distribution_dict['three words'])
    return distribution_dict


