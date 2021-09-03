from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    infl_file = "inflation_russia.csv"

    with open(infl_file, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        ordered_fields = reader.fieldnames
        data = list(reader)


    # чтение csv-файла и заполнение контекста
    # зарегестрировать фильтр для цветов
    context = {
        "data": data,
        "ordered_fields": ordered_fields
    }

    return render(request, template_name, context)
