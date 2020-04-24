from bottle import run, route, get, post, template, request, static_file
from datetime import datetime, timedelta
left_dryers = [' ', ' ', ' ', ' ', ' ']
washer = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
right_dryer = [' ', ' ', ' ', ' ', ' ']
@route('/')
def main_menu():
    return template('index.html')


@get('/available')
def availability():
    return template('availability.html', left_dryers=left_dryers, washer=washer, right_dryer=right_dryer)


@post('/available')
def available():
    timer = request.forms.selectedTime
    machine = request.forms.id
    machine = int(machine)
    timer = int(timer)
    if machine <= 5:
        for i in range(5):
            if machine == i + 1:
                total_t = (datetime.now() + timedelta(minutes=timer)).strftime('%I:%M%p')
                left_dryers.pop(i)
                left_dryers.insert(i, total_t)
                times_up = datetime.now().strftime('%I:%M%p')
                for check in range(5):
                    if left_dryers[check] != ' ':
                        if times_up >= left_dryers[check]:
                            for ind, ite in enumerate(left_dryers):
                                if ite == left_dryers[check]:
                                    left_dryers[ind] = ' '

    elif 6 <= machine <= 15:
        for i in range(16):
            if machine == i:
                total_t = (datetime.now() + timedelta(minutes=timer)).strftime('%I:%M%p')
                washer.pop(i - 6)
                washer.insert(i - 6, total_t)
                times_up = datetime.now().strftime('%I:%M%p')
                for check in range(10):
                    if washer[check] != ' ':
                        if times_up >= washer[check]:
                            for ind, ite in enumerate(washer):
                                if ite == washer[check]:
                                    washer[ind] = ' '

    else:
        for i in range(21):
            if machine == i:
                total_t = (datetime.now() + timedelta(minutes=timer)).strftime('%I:%M%p')
                right_dryer.pop(i - 16)
                right_dryer.insert(i - 16, total_t)
                times_up = datetime.now().strftime('%I:%M%p')
                for check in range(5):
                    if right_dryer[check] != ' ':
                        if times_up >= right_dryer[check]:
                            for ind, ite in enumerate(right_dryer):
                                if ite == right_dryer[check]:
                                    right_dryer[ind] = ' '

    return template('availability.html', left_dryers=left_dryers, washer=washer, right_dryer=right_dryer)


@route('/feedback')
def feedback():
    return template('feedback.html')


@get('/static/<filename>')
def ser_static(filename):
    return static_file(filename, root='./static')


@route('/images/<filename>')
def get_images(filename):
    return static_file(filename, root='C:/Users/codyw/PycharmProjects/Projects/COMPUTING I/final/static/images')


run(local='localhost', port=8090, debug=True, reloader=True)
