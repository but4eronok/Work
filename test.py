from docxtpl import DocxTemplate

doc = DocxTemplate("Laba_3.docx")
context = {'номер_лабы': '2', 'тема': 'Шаблоны в питоне', 'группа': 'ИУ10-114', 'студент_1': 'Пупа',
           'студент_2': 'Лупа', 'преподаватель': 'бухгалтерия'}
doc.render(context)
doc.save("Laba_3-final.docx")
