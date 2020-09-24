from django.shortcuts import render
from .models import TerminalList
import datetime
# import sklearn.external.joblib as extjoblib
import joblib
import os
import pandas as pd


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
    os.chdir(r'C:\Users\whdid\OneDrive\바탕 화면\bus_confusion_reminder')
    model = joblib.load('시청.pkl')
    terminal = request.POST['terminal']##역
    day = request.POST['day'] ## 날짜
    weather = request.POST['weather']
    weather_dic = {'맑음':0, '구름 조금':1, '구름 많음':2, '흐림':3, '비':4, '눈':5}
    weather_num = weather_dic[weather] ## 날씨
    if weather_num == 0:
        wth = 1,0,0,0,0,0
    elif weather_num == 1:
        wth = 0,1,0,0,0,0
    elif weather_num == 2:
        wth = 0,0,1,0,0,0
    elif weather_num == 3:
        wth = 0,0,0,1,0,0
    elif weather_num == 4:
        wth = 0,0,0,0,1,0
    elif weather_num == 5:
        wth = 0,1,0,0,0,1
    year = int(day.split('-')[0])#년
    month = int(day.split('-')[1])#월
    days = int(day.split('-')[2])#일
    time = request.POST['time'] ## 시간
    day_of_the_week = datetime.datetime(year, month, days).weekday()#요일숫자
    # day_of_the_week_dic = {1:'화요일', 2:'수요일', 3:'목요일', 4:'금요일', 5:'토요일', 6:'일요일', 7:'월요일'}
    # week_day = day_of_the_week_dic[day_of_the_week] ## 요일
    if day_of_the_week == 7:
        week = 1,0,0,0,0,0,0
    elif day_of_the_week == 6:
        week = 0,0,0,0,0,0,1
    elif day_of_the_week == 5:
        week = 0,0,0,0,0,1,0
    elif day_of_the_week == 4:
        week = 0,0,0,0,1,0,0
    elif day_of_the_week == 3:
        week = 0,0,0,1,0,0,0
    elif day_of_the_week == 2:
        week = 0,0,1,0,0,0,0
    elif day_of_the_week == 1:
        week = 0,1,0,0,0,0,0
    predict = model.predict(pd.DataFrame([year,month,days,time,week,wth]).T)
    return render(request, 'result.html', {'terminal':terminal, 'day':day, 'time':time, 'predict':predict})