from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

# menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

# нужен был в процессе обучения для вывода аргументов 
# class MyClass:
#     def __init__(self, num_1, num_2):
#         self.num_1 = num_1
#         self.num_2 = num_2

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]

# Имитируем базу данных
data_db = [
    {'id': 1, 'title': 'Cyrax', 'content': 'Cyrax\'s biography', 'is_published': True},
    {'id': 2, 'title': 'Sub Zero', 'content': 'Sub Zero\'s biography', 'is_published': False},
    {'id': 3, 'title': 'Kano', 'content': 'Kano\'s biography', 'is_published': True},
]


def index(request):
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        # 'float': 28.56,
        # 'lst': [1, 2, 'Hello', True],
        # 'set': {1, 2, 3, 2, 5},
        # 'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        # 'obj': MyClass(10, 20),
        # 'url': slugify('The main page')

    }  # для передачи заголовка в html по ключу
    return render(request, 'women/index.html', context=data)  # Заменяет работу верхних двух строк. Функция render
    # обрабатывает шаблон и отдаёт его клиенту


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def categories(request, cat_id):
#     return HttpResponse(f'<h1>Статьи по категориям</h1><p>id: {cat_id}</p> ')


# def categories_by_slug(request, cat_slug):
#     if request.POST:
#         print(request.POST)
#     return HttpResponse(f'<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p> ')


# def archive(request, year):
#     if year > 2023:
       # uri = reverse('cats', args=('sport',))   функция reverse - для вычисления переменной-маршрута
    #return HttpResponsePermanentRedirect(uri)   для перенаправлений с кодом 301
        # return HttpResponseRedirect(uri) для перенаправлений с кодом 302
        # return redirect(uri) при таком перенаправлении необходимо указывать доп параметр, в данном
        # случае - 'music' (автоматом подставляется в slug) и он будет также в маршруте

        # return redirect('home') Данный вариант самый верный! Спасает, от редактирования кода,
        # при изменениях! код 302 - временное перемещение
        # return redirect(index)  # код 302 - временное перемещение

        # return redirect('/', permanent=True) функция redirect делает по умолчанию перенаправление
        # с кодом 302(страница перемещена временно на другой URL адрес), если есть permanent=True, то код
        # будет 301 - страница постоянно перемещена на другой URL адрес

        # raise Http404() для того чтобы перекидывать на представление ниже, если год > 2023
    # return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')



