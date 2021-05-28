from datetime import datetime
from plyer import notification


def count_num(sentence):                    # counting the number of numerical words in a sentence
    num = 0
    for word in sentence.split():
        if word[0].isdigit():
            num += 1
    return num


time_in_words = ['noon', 'midnight', 'in the morning', 'in the evening', 'in the afternoon']
time_in_am_pm = ['12:00', '00:00', 'am', 'pm', 'pm']


def convert_time(a_string):                 # converting words in sentences into time
    for i in range(5):
        a_string = a_string.replace(time_in_words[i], time_in_am_pm[i])
    return a_string


# counting the number of numerical words in a sentence, the one which follows 'at' is time.
# when there is no numerical or  no time given, default time is used.
default_time = '12:00'


def notification_time(a_string):
    time1 = ''
    time_in_hours = ''
    str_lst = a_string.split()
    for word in str_lst:
        if word[0].isdigit():
            if count_num(a_string) == 1 and str_lst[str_lst.index(word)-1] == 'at':
                if str_lst.index(word) == len(str_lst)-1:              # for time : 12:00 or 00:00
                    time1 = word
                else:                       # for time : 6:30 pm, 10:00 am ..
                    time1 = " ".join([word, str_lst[str_lst.index(word)+1]])
            elif count_num(a_string) == 1 and str_lst[str_lst.index(word) - 1] != 'at':   # time is not given
                time1 = default_time
        elif count_num(a_string) == 0:      # time is not given
            time1 = default_time
    if len(time1.split()) > 1:              # converting 12 hour (am/pm) into 24 hour clock
        if time1.split()[1] == 'pm' and int(time1.split()[0].split(':')[0]) < 12:
            time1 = time1.replace(time1.split()[0].split(':')[0], str(int(time1.split()[0].split(':')[0])+12), 1)
            time_in_hours = time1.split()[0]
        elif time1.split()[1] == 'am':
            time_in_hours = time1.split()[0]
    else:                                   # for time like 12:00 or 00:00
        time_in_hours = time1
    return time_in_hours


def notification_message(a_string):
    str_lst = a_string.split()
    if ' '.join(str_lst[:3]) == 'Remind me to':                  # for reminders beginning with 'Remind me to'
        if 'at' in str_lst:                                      # message will be between 'to' and 'at' i.e. till time
            return ' '.join(str_lst[3:str_lst.index('at')])
        else:                                                    # message will be from 'to' till end
            return ' '.join(str_lst[3:])
    else:                                                        # for reminders not beginning with 'Remind me to'
        if 'at' in str_lst:
            return ' '.join(str_lst[:str_lst.index('at')])       # message will be 'at' i.e. till time
        else:
            return a_string                                      # message will be the reminder itself


with open("C:/Users/Acer/Desktop/reminder_data.txt", "r") as data:
    while True:
        for rem in data.readlines():
            if notification_time(convert_time(rem)) == datetime.now().strftime('%H:%M'):
                notification.notify(message=notification_message(convert_time(rem)))
