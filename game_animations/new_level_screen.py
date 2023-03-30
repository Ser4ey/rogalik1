import curses
import time
import random
from console import Console


class DrawLevel:
    ASCIISymbols = {
        'level': r''' _                    _ 
| |                  | |
| |     _____   _____| |
| |    / _ \ \ / / _ \ |
| |___|  __/\ V /  __/ |
|______\___| \_/ \___|_|''',
        '1': r''' __ 
/_ |
 | |
 | |
 | |
 |_|''',
        '2': r'''  ___  
 |__ \ 
    ) |
   / / 
  / /_ 
 |____|''',
        '3': r'''  ____  
 |___ \ 
   __) |
  |__ < 
  ___) |
 |____/ ''',
        '4': r'''  _  _   
 | || |  
 | || |_ 
 |__   _|
    | |  
    |_|  ''',
        '5': r'''  _____ 
 | ____|
 | |__  
 |___ \ 
  ___) |
 |____/ ''',
        '6': r'''    __  
   / /  
  / /_  
 | '_ \ 
 | (_) |
  \___/ ''',
        '7': r'''  ______ 
 |____  |
     / / 
    / /  
   / /   
  /_/    ''',
        '8': r'''   ___  
  / _ \ 
 | (_) |
  > _ < 
 | (_) |
  \___/ ''',
        '9': r'''   ___  
  / _ \ 
 | (_) |
  \__, |
    / / 
   /_/  ''',
        '0': r'''   ___  
  / _ \ 
 | | | |
 | | | |
 | |_| |
  \___/ '''
    }

    def __init__(self, console: Console):
        self.console = console

    @staticmethod
    def join_symbols(*symbols: str):
        new_symbols = ''
        symbols = [i.split('\n') for i in symbols]

        for j in range(len(symbols[0])):
            for i in range(len(symbols)):
                new_symbols += symbols[i][j]
            new_symbols += '\n'
        return new_symbols[:-1]

    def draw_level_screen(self, level_number):
        symbols = [DrawLevel.ASCIISymbols['level']]
        for i in str(level_number):
            symbols.append(DrawLevel.ASCIISymbols[i])
        draw_symbol = DrawLevel.join_symbols(*symbols)

        x_size, y_size = self.console.get_long_string_size(draw_symbol)
        x_position = (self.console.max_width - x_size) // 2
        y_position = (self.console.max_height - y_size) // 2

        for i in range(5, 21):
            self.console.clear()
            self.console.write_border(0, 0, 150, 49)

            draw_symbol_random = ''
            for s in draw_symbol:
                if s == '\n':
                    draw_symbol_random += s
                    continue
                if random.randint(1, 19) > i:
                    draw_symbol_random += ' '
                else:
                    draw_symbol_random += s

            x_position_here = x_position
            y_position_here = y_position
            if random.randint(1, 19) > i and 20 > i:
                x_position_here = x_position + random.randint(-(21-i), 21-i)
                y_position_here = y_position + random.randint(-(21-i), 21-i)

            self.console.write_object_by_long_string(x_position_here, y_position_here, draw_symbol_random)
            self.console.refresh()
            self.console.napms(random.randint(30, 80))

        self.console.clear_buffer()
        self.console.get_char()














