from django.shortcuts import render
from .models import TerminalList
import datetime


# Create your views here.
def home(request):
    return render(request, 'home.html')
    
def show_terminal(request):
    pre_terminal = request.POST['pre_terminal']
    terminal_list = TerminalList.objects.all()
    list(terminal_list)
    pre_terminal_list = []
    for i in terminal_list:
        i = str(i)
        if pre_terminal in i:
            pre_terminal_list.append(i)
    if len(pre_terminal_list) == 0:
        return render(request, 'terminal_error.html')

    return render(request, 'show_terminal.html', {'pre_terminal':pre_terminal, 'pre_terminal_list':pre_terminal_list})

def add_info(request):
    terminal = request.POST['terminal']

    return render(request, 'add_info.html', {'terminal':terminal})


def result(request):
    terminal = request.POST['terminal']##역
    day = request.POST['day'] ## 날짜
    weather = request.POST['weather']
    weather_dic = {'맑음':0, '구름 조금':1, '구름 많음':2, '흐림':3, '비':4, '눈':5}
    weather_num = weather_dic[weather] ## 날씨
    year = int(day.split('-')[0])
    month = int(day.split('-')[1])
    days = int(day.split('-')[2])
    time = request.POST['time'] ## 시간
    day_of_the_week = datetime.datetime(year, month, days).weekday()
    day_of_the_week_dic = {1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일', 7:'월요일'}
    week_day = day_of_the_week_dic[day_of_the_week] ## 요일
    return render(request, 'result.html', {'terminal':terminal, 'day':day, 'time':time})