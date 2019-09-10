# Пишу код в браузере. Не мешайте
import random

class OtrhBattle:

    @staticmethod
    def fight(player, enemy):
        _player = player
        _enemy = enemy

        text = 'Сражение {} and {}\n'.format(_player['nick'], _enemy['name'])

        moves = 1
        first = False
        if _player['fatk'] / 2 < random.randint(1, 70):
            first = True

        while _player['hp'] > 0 and _enemy['hp'] > 0:
            if (moves == 1 and first) or moves > 1:
                atk = random.randint(round(_player['atk'] * 0.8), round(_player['atk'] * 1.2))
                if _player['crit'] / 2 < random.randint(1, 70):
                    atk *= 1.5
                atk = round(atk)
                _enemy['hp'] -= atk
                text += '\n{} нанес удар 💥{}'.format(_player['nick'], atk)

            if _enemy['hp'] > 0:
                atk = random.randint(round(_enemy['atk'] * 0.8), round(_enemy['atk'] * 1.2))
                if _enemy['crit'] / 2 < random.randint(1, 70):
                    atk *= 1.5
                atk = round(atk)
                _player['hp'] -= atk
                text += '\n{} нанес удар 💥{}'.format(_enemy['nick'], atk)

            moves += 1

            
        winner = 'player'
        if _player['hp'] > 0:
            text += '\n\n{} одержал победу над {}'.format(_player['nick'], _enemy['nick'])
        else:
            winner = 'enemy'
            text += '\n\n{} одержал победу над {}'.format(_enemy['nick'], _player['nick'])

        return [text, winner]


player = {'nick': 'otrh', 'hp': 100, 'atk': 5, 'fatk': 5, 'crit': 5}
enemy = {'nick': 'mob', 'hp': 100, 'atk': 5, 'fatk': 5, 'crit': 5}
test = OtrhBattle.fight(player, enemy)
print(test)
#Вызывать по примеру выше. Вернет чисто текст
