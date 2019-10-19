import asyncio
import chess
import chess.engine

async def main():
    transport, engine = await chess.engine.popen_uci("C:\\Users\\Adrian\\Downloads\\stockfish-10-win\\stockfish-10-win\\Windows\\stockfish_10_x64")

    board = chess.Board()
    while not board.is_game_over():
        result = await engine.play(board, chess.engine.Limit(time=0.0100))
        board.push(result.move)
        print(board.uci(result.move), file=open("stockfish_test.pgn", "a+"))
    # while board.is_game_over():
    #     print(board.move_stack, file=open("stockfish_test.pgn", "w+"), end="\n\n")

    await engine.quit()

asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())