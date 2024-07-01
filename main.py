import os, re

#Количество файлов с сообщениями
count_files = len(os.listdir(os.getcwd())) - 1
filename = 'Messages.html'
#Регулярное выражение для получения количество пришедших лайков
pattern = re.compile(r'Кому-то понравилась твоя анкета:<br><br>(.*?)</div>', re.DOTALL)
recieved_likes_data = set()
#Взаимные лайки от других людей, которые получили  Ваш лайк первыми
common_likes = 0
#Количество Ваших дизлайков
dislikes = 0
#Количество Ваших лайков
likes = 0
#Количество лайков, которые Вы поставили людям, лайкнувших Вас первыми
mutual_received_likes = 0

for i in range(count_files):
    #Если обрабатывается первый файл
    file_number = ""
    # Если обрабатываются последующие файлы
    if i != 0:
        file_number = str(i + 1)

    with open(filename[:8] + file_number + filename[8:], 'r', encoding='utf-8') as file:
        data = file.read()

    for match in re.finditer(pattern, data):
        recieved_likes_data.add(match.group(1).strip())

    dislikes += data.count('👎')
    likes += data.count('❤')
    common_likes += data.count('Есть взаимная симпатия!')
    mutual_received_likes += data.count('Отлично! Надеюсь хорошо проведете время')

print(f'Общее количество просмотренных анкет = {dislikes + likes}')
print(f'Количество поставленных дизлайков = {dislikes - (len(recieved_likes_data) - mutual_received_likes)}')
print(f'Количество поставленных лайков = {likes - mutual_received_likes}')
print(f'Количество взаимных лайков от девушек = {common_likes}')
print(f'Количество полученных лайков = {len(recieved_likes_data)}')
print(f'Количество положительных ответов на полученные лайки = {mutual_received_likes}')