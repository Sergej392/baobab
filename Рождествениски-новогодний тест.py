import pyautogui
print("Дед мороз заметил что у него нехватает подарков,а до нового года остаётся день и новые подарки Дед Мороз не успеет сделать")
input()
print("Поэтому Дед мороз звонит своему брату,Санте Клаусу,чтобы попросить с его фабрики Эльфов немного подарков")
input()
print("Санта соглошается помочь своему брату")
input()
print("Дед Мороз пришел на фабрику(в ней никого небыло).Только на двери стоит замок с тестом.Дед Мороз звонит через телефоную будку Санте,чтобы тот помог ему с тестом")
input()
print("Санта не припомнит никокого теста.Оказывается это Крампус поставил замок,чтобы испортить новый год")
input()
print("Помогите Деду Морозу решить тест")
input()
print("Викторина 1:","Новогодние традиции мира")
text=pyautogui.prompt(text="а)Италия б)Испания в)Мексика г)Япония",title="Вопрос №1: В какой стране жители пишут желания на бумаге, сжигают её и добавляют пепел в бокал шампанского?",default="Ответ")
print(text)
Ответ_к_вопросу_1 = ("Испания")
if text == Ответ_к_вопросу_1:
    print("Верно!")
    print("Следующий вопрос")
else:
    print("Неверно!Начните тест занаво")
text=pyautogui.prompt(text="а) Бразилия б) Финляндия в) Австралия г) Индия",title="Вопрос №2: Где принято встречать Новый год в белом?",default="Ответ")
print(text)
Ответ_к_вопросу_2 = ("Бразилия")
if text == Ответ_к_вопросу_2:
    print("Верно!")
    print("Следующий вопрос")
else:
    print("Неверно!Начните тест занаво")
text=pyautogui.prompt(text="а) Суши б) Лапшу соба в) Традиционный рис с овощами г) Торт моти",title="Вопрос №3: Какую еду традиционно подают на Новый год в Японии?",default="Ответ")
print(text)
Ответ_к_вопросу_3 = ("Лапшу соба")
if text == Ответ_к_вопросу_3:
    print("Верно!")
    print("Следующий вопрос")
else:
    print("Неверно!Начните тест занаво")
print("Викторина 2:","Кино и мультфильмы праздников")
text=pyautogui.prompt(text="а) Ёлки б) Рождественская история в) Гринч-похититель рождества г) Один дома",title="Вопрос №4: Какой фильм о мальчике, оставшемся дома одного на Рождество, стал культовым?",default="Ответ")
print(text)
Ответ_к_вопросу_4 = ("Один дома")
if text == Ответ_к_вопросу_4:
    print("Верно!")
    print("Следующий вопрос")
else:
    print("Неверно!Начните тест занаво")
text=pyautogui.prompt(text="а) ""Соник в кино"" б) ""Брюс всемогущий"" в) ""Гринч-похититель рождества"" г) ""Тупой и ещё тупее",title="Вопрос №5: В каком фильме посвещёному рождеству сыграл актёр Джим Керри?",default="Ответ")
print(text)
Ответ_к_вопросу_5 = ("Гринч-похититель рождества")
if text == Ответ_к_вопросу_5:
    print("Верно!")
    print("Следующий вопрос")
else:
    print("Неверно!Начните тест занаво")
text=pyautogui.prompt(text="а) «Рождественская песнь» б) «Подарок волхвов» в) «Щелкунчик» г) ""Холодное торжество",title="Вопрос №6: Как называется рождественская история про Скруджа?",default="Ответ")
print(text)
Ответ_к_вопросу_6 = ("Рождественская песнь")
if text == Ответ_к_вопросу_6:
    print("Верно!")
    print("Следующий вопрос")
else:
    print("Неверно!Начните тест занаво")
print("Викторина 3:","Новогодние персонажи")
text=pyautogui.prompt(text="а) Траву б) Морковь в) Ягоды г) Снег,title=""Вопрос №7: Что обычно едят северные олени Санты?",default="Ответ")
print(text)
Ответ_к_вопросу_7 = ("Морковь")
if text == Ответ_к_вопросу_7:
    print("Верно!")
    print("Следующий вопрос")
else:
    print("Неверно!Начните тест занаво")
text=pyautogui.prompt(text="а) Финляндия б) Норвегия в) Швеция г) Исландия,title=""Вопрос №8: В какой стране Санта-Клаус носит имя Йоулупукки?",default="Ответ")
print(text)
Ответ_к_вопросу_8 = ("Финляндия")
if text == Ответ_к_вопросу_8:
    print("Верно!")
    print("Следующий вопрос")
else:
    print("Неверно!Начните тест занаво")
text=pyautogui.prompt(text="а) Финляндия б) Норвегия в) Швеция г) Исландия,title=""Вопрос №9: В какой стране Санта-Клаус носит имя Йоулупукки?",default="Ответ")
print(text)
Ответ_к_вопросу_9 = ("Финляндия")
if text == Ответ_к_вопросу_9:
    print("Верно!")
    print("Следующий вопрос")
else:
    print("Неверно!Начните тест занаво")
text=pyautogui.prompt(text="а) Сатана высасывающий кровь непослушных детей б) Монстр кродя подарки непослушных детей в) Чёрт пугающий непослушных детей  г) Чародей превращая непослушных детей в уголь,title=""Вопрос №10: Кто такой Крампус?",default="Ответ")
print(text)
Ответ_к_вопросу_10 = ("Чёрт пугающий непослушных детей")
if text == Ответ_к_вопросу_10:
    print("Верно!")
    print("Следующий вопрос")
else:
    print("Неверно!Начните тест занаво")
    print("Я в тебе разочарован!Незнать великого Крампуса")
print("Дед Мороз реша тест открыл фабрику,собра все нужные игрушки Дед Мороз полетел разностить подарки.Новый год был спасён!")