print('ВВЕДИТЕ КОЛИЧЕСТВО СЕКУНД')
duration = int(input())
if duration < 60: # выводим секунды
    print(duration,' сек')
elif 3600 > duration >= 60:
    m = duration // 60 #выводим минуты
    print(m,'мин',(duration - m * 60),'сек')
elif 86400 > duration >= 3600: #выводим часы
    h = duration//3600
    print(h,'час',duration % 3600 // 60,'мин',(duration - (duration // 60) * 60),'сек')
else:
    print(duration // 86400,'дн',duration % 86400 // 3600,'час',duration % 60,'мин',(duration - (duration // 60) * 60),'сек')

