## The Chess

ChessUI has a public method draw, that method expect a hash as its sole parameter, the hash must contain
a key for every active piece on the board, the key corresponds to a board coordinate, i.e a1, f5, etc.
the value corresponding to that key must be the piece that lives on that square, the piece is represented
by a string composed by the color of the piece, (b or w) followed by the type of the piece.
The different piece types are:
- K - King
- Q - Queen
- N - kNight
- B - Bishop
- R - Rook
- P - Pawn

You are expected to ask the user for it's next movement, i.e a2-a4, and redraw the board after every successfully
state change on the board.

Remember, we'll evaluate both design and implementation, even when implementing many parts of the game is good, it's better to have a solid design.

Some rules to remember:

- https://en.wikipedia.org/wiki/Rules_of_chess General rules of chess
- http://en.wikipedia.org/wiki/Castling Castling
- http://en.wikipedia.org/wiki/En_passant En Passant
- If you're on check the only valid moves are those that let you on a no-check state
- If a move lets you on a check state that move is invalid
- If the current player is not on check but has no valid moves available the games ends as a draw
- If the current player is on check and has no way to remove it's status a checkmate is declared
- Every time a player puts on check its opponent the event must be declared
- Pawns becomes queens if they get to the opponent's first row
# Chess
