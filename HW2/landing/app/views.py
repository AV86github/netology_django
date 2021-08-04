from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
print("Load counters")
counter_show = Counter()
counter_click = Counter()
ORIG_PARAM = "original"
ALTER_PARAM = "test"


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    req_source = request.GET.get("from-landing")
    if req_source == ORIG_PARAM:
        print(ORIG_PARAM)
        counter_click[ORIG_PARAM] += 1
    else:
        print(ALTER_PARAM)
        counter_click[ALTER_PARAM] += 1
    return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    req_source = request.GET.get("ab-test-arg")
    if req_source == ORIG_PARAM:
        print("show: ", ORIG_PARAM)
        counter_show[ORIG_PARAM] += 1
        return render(request, 'landing.html')
    else:
        print("show: ", ALTER_PARAM)
        counter_show[ALTER_PARAM] += 1
        return render(request, 'landing_alternate.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    print("show: ", counter_show)
    print("click: ", counter_click)
    return render(request, 'stats.html', context={
        'test_conversion': round(counter_show[ALTER_PARAM] / counter_click[ALTER_PARAM], 2),
        'original_conversion': round(counter_show[ORIG_PARAM] / counter_click[ORIG_PARAM], 2),
    })
