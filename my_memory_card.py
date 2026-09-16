# Подключаем библиотеку PyQT5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Questions():
    def __init__(self, questions, right_answer, wrong1, wrong2, wrong3):
        self.questions = questions
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Questions('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Questions('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Questions('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))

# Создаём приложение PyQt
app = QApplication([])
# Создаём главное окно
window = QWidget()
# Заголовок окошка
window.setWindowTitle("Memory Card")
window.resize(400, 400)

# Интерфейс приложения Memory Card
# Кнопка для отправки ответа
btn_OK = QPushButton('Ответить')
# Надпись с вопросом
lb_Questions = QLabel("Самый сложный вопрос в мире!")
# Блок (группа) для вариантов ответов
RadioGroupBox = QGroupBox("Варианты ответов:")
rbtn_1 = QRadioButton("Вариант 1")
rbtn_2 = QRadioButton("Вариант 2")
rbtn_3 = QRadioButton("Вариант 3")
rbtn_4 = QRadioButton("Вариант 4")

# -------- Новые изменения ----------
radioGroup = QButtonGroup()
radioGroup.addButton(rbtn_1)
radioGroup.addButton(rbtn_2)
radioGroup.addButton(rbtn_3)
radioGroup.addButton(rbtn_4)
# -------- Новые изменения ----------

# Горизонтальный контейнер для двух столбцов ответов
layout_ans1 = QHBoxLayout()
# Вертикальные контейнеры для каждого столбца
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
# Добавляем две радиокнопки в первый столбец
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
# Добавляем две радиокнопки во второй столбец
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
# Вставляем оба столбца в горизонтальный контейнер
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
# Устанавливаем готовый макет в группу с ответами
RadioGroupBox.setLayout(layout_ans1)

# -------- Новые изменения ----------
AnsGroupBox = QGroupBox("Результаты теста")
lb_Result = QLabel("Прав ты или нет?")
lb_Correct = QLabel("Ответ будет тут.")
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
# -------- Новые изменения ----------

# Строка для вопроса
layout_line1 = QHBoxLayout()
# Строка для вариантов ответов
layout_line2 = QHBoxLayout()
# Строка для кнопки ответа
layout_line3 = QHBoxLayout()
# Размещаем вопрос по центру
layout_line1.addWidget(lb_Questions, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
# Добавляем блок с вариантами ответов в строку
layout_line2.addWidget(RadioGroupBox)
# -------- Новые изменения ----------
layout_line2.addWidget(AnsGroupBox)
# hide() скрыть элемент
AnsGroupBox.hide()
# -------- Новые изменения ----------
# Добавляем отступ слева
layout_line3.addStretch(1)
# Добавляем кнопку "Ответить" и делаем её шире
layout_line3.addWidget(btn_OK, stretch=2)
# Добавляем отступ справа
layout_line3.addStretch(1)
# Основной вертикальный макет окна
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
# пробелы между содержимым
layout_card.setSpacing(5)

# ----------------------------------------------------------
# Виджеты и макеты созданы, далее - функции:
# ----------------------------------------------------------
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.score = 0 
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос.")
def show_Questions():
    ''' показать панель вопросов '''
    # Тут Ошибки
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    radioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radioGroup.setExclusive(True)

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Questions):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Questions.setText(q.questions)
    lb_Correct.setText(q.right_answer)
    show_Questions()

def show_correct(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    show_result()

def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика:')
        print('Всего вопросов', window.total)
        print('Правильных ответов:', window.score)
        print('Рейтинг:',(window.score / window.total) * 100, '%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Не верно!')
            print('Рейтинг:',(window.score / window.total) * 100, '%')
def next_questions():
    ''' задает следующий вопрос из списка '''
    window.total += 1
    print('Статистика:')
    print('Всего вопросов', window.total)
    print('Правильных ответов:', window.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_questions()
       
window.setLayout(layout_card)

window.cur_question = -1
btn_OK.clicked.connect(click_OK)
window.total = 0
window.score = 0
next_questions()
window.show()
app.exec()
