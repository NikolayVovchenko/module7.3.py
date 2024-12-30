# Пример входных данных
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print('В команде Мастера кода участников: %s !'% team1_num)
print('Итого сегодня в командах участников: %s и %s!'% (team1_num, team2_num))
print(f'Команды решили по {score_1} и {score_2} задачи.')

result1 = 'Команда Волшебники решила данных задач:{} !'.format(score_2)
result2 = 'Волшебники решили данные задачи за {} с!'.format(team1_time)
print(result1)
print(result2)


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'


tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f'Сегодня было решено {tasks_total} задачи,\n',
      f'в среднем по {time_avg:.1f} секунды на задачу!')
print(f'Результат битвы:{challenge_result}')


if __name__ =='__main__':
    # Пример входных данных
    team1_num = 5
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451
    tasks_total = 82
    time_avg = 45.2
    challenge_result = 'Победа команды Волшебники данных!'