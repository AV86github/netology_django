from django.urls import path, register_converter
from app.views import file_list, file_content
from .converters import ISO_Date

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам

register_converter(ISO_Date, 'ISO')


urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path("", file_list, name='file_list'),
    path("<ISO:date>/", file_list, name='file_list'),
    path("file/<name>/", file_content, name='file_content'),
]
