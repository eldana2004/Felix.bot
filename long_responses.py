import re


def process_message(message, response_array, response):
    list_message=re.findall(r"[\w']+|[.,!?;]", message.lower())
    score = 0
    for word in list_message:
        if word in response_array:
            score =score+1

    print(score, response)
    return[score, response]

def get_response(message):
    response_list = [
        process_message(message, ['hello','hi','hey','morning','evening'], 'Hello!'),
        process_message(message, ['bye'], "Bye, bye!"),
        process_message(message, ['i', 'am ', 'good', 'okey', 'ok','norm'], 'Good to hear!^-^'),
        process_message(message, ['can', 'you', 'help', 'with'], 'I will try my best!'),
        process_message(message, ['how', 'you', 'are'], 'I am good! And you?'),
        process_message(message, ['what', 'is', 'your', 'name', 'who'], 'My name is Felix!'),
        process_message(message, ['who', 'create', 'you', 'made', 'maden'], 'I was created by Eldana, Altynai, Saltanat and Urmatai!^-^'),
        process_message(message, ['what','is','your','job','responsibility'], 'I am your friend, and I am jobless, hehe'),
        process_message(message, ['where', 'are','you'], 'I live in ala-too\'s canteen'),
        process_message(message, ['do', 'you', 'like', 'ala-too', 'ala too'], 'Sure! I like this University!'),
        process_message(message, ['my', 'name', 'is'], 'Nice to meet you!'),
        process_message(message, ['thank','thanks'], "You are welcome!"),
        process_message(message, ['english'], 'Monday \n English \n 9.00-10.40 \n B202\n\n Friday \n 9.00-10.40 \n B201' ),
        process_message(message, ['pl','programming'],'Monday\n10.40-13.00 \nB104\n\nFriday\n14.00-16.20 \nB208'),
        process_message(message, ['graphic','design'],'Monday \n14.00-17.00 \nB210'),
        process_message(message, ['physical', 'training'], 'Tuesday \n9.00-10.30'),
        process_message(message, ['calculus'], 'Tuesday\n10.40-13.00 \nB205\n\nThursday\n9.00-11.20\nB204'),
        process_message(message, ['graphic', 'design'], 'Monday \n14.00-17.00 \nB210'),
        process_message(message, ['russian'], 'Tuesday \n14.00-15.30 \nB202/B203'),
        process_message(message, ['algebra'], 'Tuesday \n15.40-17.00 \nB201\n\nThursday\n14.00-15.30\nB201'),
        process_message(message, ['introduction'], 'Wednesday\n10.40-12.10\nB205\n\nThursday\n11.30-13.00\nBig Lab'),
        process_message(message, ['bookkeeping','accounts','counting','cabinet'], 'A block, 111 cabinet\nWork hours: 9.00-17.00\nLunch time: 13.00-14.00 '),
        process_message(message, ['medical', 'medicine','cabinet'],'A block, 102 cabinet\nWork hours: 9.00-17.00\nLunch time: 13.00-14.00 '),
        process_message(message, ['konye', 'hall'], 'A block, 105 cabinet\nWork hours: 9.00-17.00'),
        process_message(message, ['big', 'lab'], 'B block, 2 floor\nWork hours: 9.00-17.00'),
        process_message(message, ['library', 'book', 'books'], 'A block, 106 cabinet\nWork hours: 9.00-17.00\nLunch time: 12.00-13.00 '),
        process_message(message, ['mid', 'midterms','when','mid exam','2022'], 'November 1 - November 6'),
        process_message(message, ['final', 'finals', 'when', 'final exam', '2022'], 'December 5 - December 18'),
        process_message(message, ['forgot', 'password', 'when'], 'A block, 102 cabinet\nWoork hours: 9.00-17.00\nLunch time: 12.00-13.00 ')





    ]


    response_scores=[]
    for response in response_list:
        response_scores.append(response[0])
    winning_response= max(response_scores)
    matching_response=response_list[response_scores.index(winning_response)]

    if winning_response == 0:
        bot_response= 'I don\'t understand what you wrote'
    else:
        bot_response = matching_response[1]
    print('Bot response: ', bot_response)
    return bot_response


