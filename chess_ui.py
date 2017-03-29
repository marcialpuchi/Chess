from colorama import Fore, Back, Style

class ChessUI:

    def piece_builder(self, player, piece, color):
        bg = Back.WHITE if color == 'white' else Back.GREEN
        fg = Fore.BLACK if player == 'b' else Fore.MAGENTA
        return bg + fg + piece

    def draw(self, pieces):
        cols_map = {
            1 : 'a',
            2 : 'b',
            3 : 'c',
            4 : 'd',
            5 : 'e',
            6 : 'f',
            7 : 'g',
            8 : 'h'
        }

        for row in range(8,0,-1):
            line = '{0}'.format(row)
            color = 'black' if row % 2 == 1 else 'white'

            for x in range(1,9):
                col = cols_map[x]
                piece = pieces.get('{0}{1}'.format(col, row))
                player = 'b'

                if piece:
                    player = piece[0]
                    piece = ' ' + piece[1] + ' '
                else:
                    piece = '   '

                line += self.piece_builder(player, piece, color)

                if color == 'white':
                    color = 'black'
                else:
                    color = 'white'

            print line + Style.RESET_ALL

        print "  a  b  c  d  e  f  g  h  "
