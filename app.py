import os
import pickle

import numpy as np
import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

import matplotlib.pyplot as plt
import seaborn as sns


# @st.cache
# def read_files(folder_name='components'):
#     """
#     Функция для чтения файлов
#    """
#     pass
#     return 

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)


def main():

    st.header('Анкета для определения команды')
    st.write('')

    content = {
        'name': st.text_input('Введите ваше имя: '),
        'answer_0': st.selectbox('0. Укажите ваш возраст',
                                 ('20-25', '25-30', '30-35', '35+', 'Другое')),
        'answer_1': st.selectbox('1. Укажите ваш часовой пояс', 
                                 ('UTC+2', 'UTC+3', 'UTC+4', 'UTC+5', 'UTC+6', 'UTC+7', 'Другое')),
        'aswer_2': st.selectbox('2. Уделяете ли вы время проектам каждый день?',
                                ('Да', 'Нет')),
        'answer_3': st.selectbox('3. В каком временном диапазоне вы чаще всего занимаетесь учебными проектами в будни (по Мск)?',
                                 ('9-15', '10-16', '11-17', '12-18', '13-19', '14-20', 
                                  '15-21', '16-22', '17-23', '18-00')),
        'answer_4': st.selectbox('4. В каком временном диапазоне вы чаще всего занимаетесь учебными проектами в выходные (по Мск)?',
                                 ('9-15', '10-16', '11-17', '12-18', '13-19', 
                                  '14-20', '15-21', '16-22', '17-23', '18-00')),
        'answer_5': st.selectbox('5. Сколько часов на проект вы обычно тратите в неделю?',
                                 ('до 15', '15-25', '25-30', 'больше 30')),
        # 'answer_6': st.selectbox('6. Как вы оцениваете уровень вашего кода?',
        #                          ('Базовый', 'Средний', 'Выше среднего'))
        # 'answer_7': st.selectbox('7. Как вы оцениваете сложность задач на курсе?',
        #                          ('Легкие', 'Средней сложности', 'Сложные')), 
        'answer_8': st.selectbox('8. Как вы относитесь к дедлайнам?',
                                 ('Строго придерживаюсь сроков, даже в ущерб качеству',
                                  'Предпочитаю немного гибкости ради высокого качества')),
        'answer_9': st.selectbox('9. Какой стиль общения в команде вам больше подходит?',
                                 ('Формальный, только по делу', 'Неформальный, с дружеским общением')),
        'answer_10': st.selectbox('10. Насколько часто вы готовы участвовать в командных обсуждениях?',
                                  ('Только при необходимости', 'Ежедневно', 'Один-два раза в неделю')),
        'answer_11': st.selectbox('11. Какой уровень структурированности работы вам предпочтителен?',
                                  ('Четкие инструкции и последовательный план', 
                                   'Гибкость и свобода в выборе подхода')),
        'answer_12': st.selectbox('12. Как вы относитесь к работе в условиях неопределенности?',
                                  ('Уверенно, люблю решать новые задачи', 'Предпочитаю четкие правила и инструкции',
                                   'Чувствую себя комфортно, если есть поддержка команды')),
        'answer_13': st.selectbox('13. Насколько важно для вас одобрение и признание команды?',
                                  ('Очень важно, это мотивирует меня работать лучше',
                                   'Не слишком важно, главное — выполнить задачу',
                                   'Скорее всего, мне не нужно одобрение')),
        'answer_14': st.selectbox('14. Вы готовы помогать другим членам команды с их задачами?',
                                  ('Всегда готов, если это улучшит общий результат',
                                   'Помогу, если у меня есть свободное время',
                                   'Предпочитаю сосредоточиться на своих задачах')),
        'answer_15': st.selectbox('15. Как вы оцениваете свою инициативность?',
                                  ('Часто выступаю с предложениями и беру инициативу в свои руки',
                                   'Вношу предложения, если вижу явную возможность улучшений',
                                   'Редко проявляю инициативу, но поддерживаю хорошие идеи'))
    }

    send = st.button('Отправить')
    
    if send:
        if os.path.exists('components/data.csv'):
            result = pd.read_csv('components/data.csv')
        else:
            result = pd.DataFrame()
        result = pd.concat([result, pd.DataFrame(content, index=[0])], ignore_index=True)
        result.to_csv('components/data.csv', index=False)
        switch_page('thank you')



if __name__ == "__main__":
    main()
