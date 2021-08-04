from datetime import datetime
from django.shortcuts import render
from django.conf import settings
import os


def file_list(request, date=None):
    template_name = 'index.html'
    file_list = os.listdir(settings.FILES_PATH)
    files = []
    for cur_file in file_list:
        cr_time = datetime.fromtimestamp(os.stat(os.path.join(settings.FILES_PATH, file_list[0])).st_ctime)
        if date is None or date == cr_time.date():
            files.append({
                "name": cur_file,
                "ctime": cr_time,
                "mtime":  datetime.fromtimestamp(os.stat(os.path.join(settings.FILES_PATH, file_list[0])).st_mtime),
            })
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    context = {
        'files': files,
        'date': date  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    file_content = None
    file_path = os.path.join(settings.FILES_PATH, name)
    if os.path.isfile(file_path):
        with open(file_path) as f:
            file_content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )

