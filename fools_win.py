# import asyncio
import chess
import chess.engine
import FirstOrderOptimalLongtermStrategy as eng2

# def main():
print("\n\n\n\n\n\n\n")
engine = chess.engine.SimpleEngine.popen_uci("C:\\Users\\Adrian\\Downloads\\stockfish-10-win\\stockfish-10-win\\Windows\\stockfish_10_x64")
engine2 = eng2.engine()
# transport2, engine_crap = await chess.engine.popen_uci("C:\\Users\\Adrian\\Downloads\\stockfish-10-win\\stockfish-10-win\\Windows\\stockfish_10_x32")
# transport, engine_crap = await chess.engine.popen_uci("C:\\Users\\Adrian\\Downloads\\stockfish-10-win\\stockfish-10-win\\Windows\\stockfish_10_x64")
print("", file=open("stockfish_test5.pgn", "w+"), end="")


tlim = .01
board = chess.Board()
while not board.is_game_over():
    result2 = engine2.play(board, chess.engine.Limit(time=tlim))
    if board.uci(result2) == "0000":
        break
    board.push(result2)
    print("\nFools", file=open("stockfish_test5.pgn", "a+"))
    print(board.uci(result2), file=open("stockfish_test5.pgn", "a+")) #add output to  own uci file
    print(board, file=open("stockfish_test5.pgn", "a+"))

    if board.is_game_over():
        break
    result = engine.play(board, chess.engine.Limit(time=tlim))
    board.push(result.move)
    print("\nStockfish AI", file=open("stockfish_test5.pgn", "a+"))
    print(board.uci(result.move), file=open("stockfish_test5.pgn", "a+"))
    print(board, file=open("stockfish_test5.pgn", "a+"))

    # result = await engine_crap.play(board, chess.engine.Limit(time=tlim))
    # board.push(result.move)
    # print(board.uci(result.move), file=open("stockfish_test1.pgn", "a+"))
# while board.is_game_over():
#     print(board.move_stack, file=open("stockficsh_test.pgn", "w+"), end="\n\n")

engine.quit()
# engine2.quit()
# asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
# asyncio.run(main())
