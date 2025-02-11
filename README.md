# ITMO-System-Design-2

## Roguelike

### Общие сведения о системе:

Разрабатывается MVP простой игры в жанре [Roguelike](https://ru.wikipedia.org/wiki/Roguelike). 
#### Общая концепция игры: 
Игрок появляется в процедурно (случайно) сгенерированном подземелье, состоящим из комнат, противников, 
находящихся в них, и артефактов, которые могут увеличивать здоровье или урон. 
Далее происходит пошаговое взаимодействие - на каждом ходу игрок выбирает одно из доступных действий: движение или атака. 
Целью игры является найти и победить финального босса. 

### Запуск

```
poetry install
python3 roguelike/main.py
```

Если Вы столкнулись с ошибкой:
```
ModuleNotFoundError: No module named 'tkinter'
```

То необходимо в системный **python3** установить пакет `python3-tk`:  
* Linux
```
   sudo apt-get install python3-tk
```

* Mac
```
   brew install python3-tk
```


### Architectural drivers:

#### Технические ограничения:
Подразумевается устройство ввода (клавиатура) и устройства вывода (монитор). 

#### Функциональные требования:
1) Персонаж игрока, способный перемещаться по карте, управляемый с клавиатуры;
2) Карты генерируются случайно;
3) Характеристики - здоровье и сила атаки;
4) Инвентарь, состоящий из вещей, добавляющих здоровье и урон;
5) Пошаговое взаимодействие

### Роли и случаи использования:
**Роли:**
1. Игрок:

   - Контролирует персонажа через клавиатуру.
   - Взаимодействует с игровым окружением и объектами.
   - Управляет инвентарем и экипировкой персонажа.

2. Разработчик/Дизайнер уровней:

   - Разрабатывает уникальные уровни и сценарии.
   - Настраивает параметры для генерации карт.
   - Добавляет новые объекты, врагов и предметы.

**Сценарии:**
1. Сценарий 1: Перемещение персонажа

   - Игрок использует клавиши для перемещения по карте.

2. Сценарий 2: Взаимодействие с айтемами

   - Игрок собирает мечи и щиты.

3. Сценарий 3: Управление инвентарем

   - Игрок надевает и снимает экипировку.

4. Сценарий 4: Сражение с врагами

   - Игрок атакует противников, применяя навыки и предметы для победы.

5. Сценарий 5: Смерть

   - Персонаж погибает и игра заканчивается.

### Описание типичного пользователя

Типичный пользователь нашей системы — это увлечённый игрок, который находит удовольствие в минималистичных играх жанра Roguelike. Он обладает страстью к стратегическому мышлению, исследованию обширных и таинственных миров, а также управлению ограниченными ресурсами. Такой игрок ценит глубину и сложность игрового процесса, даже если визуальная часть игры выполнена в простом, но стильном формате ASCII-графики. Он понимает, что истинная красота игры заключается не в её внешнем облике, а в механике и возможностях, которые она предлагает.

Возраст типичного пользователя варьируется от 14 лет и старше, что свидетельствует о том, что наша игра привлекает как молодое поколение, так и более опытных геймеров. Эти игроки имеют средний уровень опыта и выше, что позволяет им уверенно ориентироваться в типовых игровых механиках. Они знакомы с жанром RPG и готовы погружаться в изучение новых игровых систем и механик, даже если обучение не всегда представлено в явной форме. 

Такой пользователь не боится вызовов и стремится к самосовершенствованию, исследуя каждый уголок игрового мира, принимая сложные решения и развивая свои стратегические навыки. Он ищет не просто развлечение, а глубокий и увлекательный опыт, который позволит ему раскрыть свои способности и насладиться каждой минутой игрового процесса.


#### Некоторые случаи использования roguelike:
 * Исследование мира. В каждом новом прохождении это исследование нужно начинать с самого начала, так как уровни генерируются случайным образом. 
 * Истребление монстров. Концепция игры «один против всех». 

### Композиция (диаграмма компонентов)
Помогает понять, как различные части системы связаны друг с другом.  
![тут должна быть диаграмма компонентов...](./diagrams/components_diagram.jpg)

### Логическая структура (диаграмма классов)
Предоставляет комплексный, достаточно подробный взгляд на систему, позволяя увидеть, как различные элементы взаимодействуют друг с другом.
![тут должна быть диаграмма компонентов...](./diagrams/classes_diagram.png)

### Взаимодействия и состояния (диаграммы последовательностей и конечных автоматов)

#### Диаграмма конечных автоматов
Используется для описания поведения системы, показывая переходы из одного состояния в другое в зависимости от входных данных.
![тут должна быть диаграмма  конечных автоматов...](./diagrams/finite_state_diagram.png)

#### Диаграмма последовательностей
Показывает, как объекты взаимодействуют друг с другом через обмен сообщениями в определенной последовательности.
![тут должна быть диаграмма  последовательностей...](./diagrams/sequences_diagram.png)

### Мотивация выбора библиотеки turtle для разработки игры roguelike
#### Преимущества библиотеки Turtle для разработки игр
**Библиотека Turtle** в Python — это простая и интуитивно понятная графическая библиотека, 
поставляемая в базовом пакете **Python3**.

Данный пакет отлично подходит для разработки несложных проектов с 2D анимацией, 
коим является создаваемая игра в стиле **roguelike**.   
API библиотеки простое и интуитивно понятное, 
отлично подходит новичкам в области создания графических приложений и gamedev.  
Кроме того, библиотека **turtle** не является **roguelike** специфичной, что так же является изначальным требованием.  
Резюмируя, пакет **turtle** - отличный, легковесный вариант, 
с помощью которого можно реализовать MVP простой игры в жанре [Roguelike](https://ru.wikipedia.org/wiki/Roguelike), не углубляясь в специфику доменной области.
#### Аналоги библиотеки Turtle
Кратко отметим имеющиеся **Python** аналоги:
- **Pygame**: Это одна из самых популярных библиотек для разработки игр на Python. 
  Она предоставляет более широкий набор инструментов для работы с графикой, 
  звуком и событиями, что делает её хорошим вариантом для создания более сложных игр.

- **Arcade**: Эта библиотека также предназначена для 2D-игр и предлагает более современный подход к разработке, с поддержкой OpenGL и более удобным API.

- **Pyglet**: Этот пакет используется создания игр и мультимедийных приложений, поддерживает 2D и 3D графику, а также работу со звуком.

### [Документация по разработке](./SETUP.md)