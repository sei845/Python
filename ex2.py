def personal_inf(**kwargs):
    return ' '.join(kwargs.values())

params = {
    'name': input('Введите имя - '),
    'surname': input('Введите фамилию - '),
    'birthday': input('Введите дату рождения - '),
    'city': input('Введите город проживания - '),
    'email': input('Введите электронную почту - '),
    'phone': input('Введите номер телефона - '),

}

print(personal_inf(**params))
