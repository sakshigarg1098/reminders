time_in_words = ['noon', 'midnight', 'in the morning', 'in the evening', 'in the afternoon']
time_in_am_pm = ['12:00', '00:00', 'am', 'pm', 'pm']
default_time = '12:00'


def count_num(sentence):
    num = 0
    for word in sentence.split():
        if word[0].isdigit():
            num += 1
    return num


def convert_time(a_string):
    for i in [0, 1, 2, 3, 4]:
        a_string = a_string.replace(time_in_words[i], time_in_am_pm[i])
    return a_string


def notification_time(a_string):
    not_time = ''
    time = ''
    for word in a_string.split():
        if word[0].isdigit():
            if count_num(a_string) == 1 and a_string.split()[a_string.split().index(word)-1] == 'at':
                if a_string.split().index(word) == len(a_string.split())-1:
                    not_time = word
                else:
                    not_time = " ".join([word, a_string.split()[a_string.split().index(word)+1]])
            elif count_num(a_string) == 1 and a_string.split()[a_string.split().index(word) - 1] != 'at':
                not_time = default_time
        elif count_num(a_string) == 0:
            not_time = default_time
    if len(not_time.split()) > 1:
        if not_time.split()[1] == 'pm' and int(not_time.split()[0].split(':')[0]) < 12:
            not_time = not_time.replace(not_time.split()[0].split(':')[0], str(int(not_time.split()[0].split(':')[0])+12), 1)
            time = not_time.split()[0]
        elif not_time.split()[1] == 'am':
            time = not_time.split()[0]
    else:
        time = not_time
    return time


def notification_message(a_string):
    if ' '.join(a_string.split()[:3]) == 'Remind me to':
        if 'at' in a_string.split():
            return ' '.join(a_string.split()[3:a_string.split().index('at')])
        else:
            return ' '.join(a_string.split()[3:])
    else:
        if 'at' in a_string.split():
            return ' '.join(a_string.split()[:a_string.split().index('at')])
        else:
            return a_string


with open("C:/Users/Acer/Desktop/reminder_data.txt", "r") as data:
    for rem in data.readlines():
        print('Message - ', notification_message(convert_time(rem)).strip(), ', Time - ', notification_time(convert_time(rem)))

print("testing branch")