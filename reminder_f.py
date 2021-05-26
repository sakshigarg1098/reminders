# counting the number of numerical words in a sentence


def count_num(sentence):
    num = 0
    for word in sentence.split():
        if word[0].isdigit():
            num += 1
    return num


# converting words in sentences into time

time_in_words = ['noon', 'midnight', 'in the morning', 'in the evening', 'in the afternoon']
time_in_am_pm = ['12:00', '00:00', 'am', 'pm', 'pm']


def convert_time(a_string):
    for i in [0, 1, 2, 3, 4]:
        a_string = a_string.replace(time_in_words[i], time_in_am_pm[i])
    return a_string


# counting the number of numerical words in a sentence, the one which follows 'at' is time.
# when there is no numerical or  no time given, default time is used.

default_time = '12:00'


def notification_time(a_string):
    time1 = ''
    time_in_hours = ''
    for word in a_string.split():
        if word[0].isdigit():
            if count_num(a_string) == 1 and a_string.split()[a_string.split().index(word)-1] == 'at':
                if a_string.split().index(word) == len(a_string.split())-1:              # for time : 12:00 or 00:00
                    time1 = word
                else:                       # for time : 6:30 pm, 10:00 am ..
                    time1 = " ".join([word, a_string.split()[a_string.split().index(word)+1]])
            elif count_num(a_string) == 1 and a_string.split()[a_string.split().index(word) - 1] != 'at':   # time is not given
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
    if ' '.join(a_string.split()[:3]) == 'Remind me to':                       # for reminders beginning with 'Remind me to'
        if 'at' in a_string.split():                                           # message will be between 'to' and 'at' i.e. till time
            return ' '.join(a_string.split()[3:a_string.split().index('at')])
        else:                                                                  # message will be from 'to' till end
            return ' '.join(a_string.split()[3:])
    else:                                                                      # for reminders not beginning with 'Remind me to'
        if 'at' in a_string.split():
            return ' '.join(a_string.split()[:a_string.split().index('at')])   # message will be 'at' i.e. till time
        else:
            return a_string                                                    # message will be the reminder itself


with open("C:/Users/Acer/Desktop/reminder_data.txt", "r") as data:
    for rem in data.readlines():
        print('Message - ', notification_message(convert_time(rem)).strip(), ', Time - ', notification_time(convert_time(rem)))
