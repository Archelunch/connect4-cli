# Connect 4

## Установка

```bash
pip install -r requirements.txt
```

## Запуск
Дефолтная игра:
```bash
python app/game.py
```

## Аргументы
```
--rows            -r    INTEGER  Number of rows in the board [default: 6]
--columns         -c    INTEGER  Number of columns in the board [default: 7]
--win-count       -w    INTEGER  Number of pieces needed in a row to win [default: 4]
--players         -p    INTEGER  Number of players (2-5) [default: 2]
--animation       -a             Enable animation for dropping pieces
--clean-display   -d             Show only the current board state (clears terminal between turns)
```

## Примеры

4 на 8, 3 игрока
```bash
python app/game.py --rows 8 --columns 4 --players 3
```

4 на 4, 2 игрока, анимация
```bash
python app/game.py --rows 4 --columns 4 --players 2 --animation
```

4 на 4, 2 игрока, анимация, очистка терминала
```bash
python app/game.py --rows 4 --columns 4 --players 2 --animation --clean-display
```

## Тесты

```bash
pytest
```

## Готово

- [x] Минимальные требования для логики игры
- [x] Анимация гравитации расстановки фишек
- [x] Кастомные значения для доски
- [x] Возможность добавлять больше игроков
- [x] Тесты
- [x] Очистка истории

## Возможные улучшения
Можно было бы заранее считать сколько осталось каждому игроку до победы и возможные ходы для этого. Мне понравилось, как это было сделано на сайте.
Но решил уйти в сторону UI/UX, потому что не сильно влияло на провизвольность.

Дописал бы больше тестов.
