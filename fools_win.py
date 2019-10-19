import asyncio
import chess
import chess.engine

async def main():
    transport, engine = await chess.engine.popen_uci("C:\\Users\\Adrian\\Downloads\\stockfish-10-win\\stockfish-10-win\\Windows\\stockfish_10_x64")
    # transport, engine_crap = await chess.engine.popen_uci("C:\\Users\\Adrian\\Downloads\\stockfish-10-win\\stockfish-10-win\\Windows\\stockfish_10_x64")
    
    tlim = .005
    board = chess.Board()
    while not board.is_game_over():
        result = await engine.play(board, chess.engine.Limit(time=tlim))
        board.push(result.move)
        print(board.uci(result.move), file=open("stockfish_test1.pgn", "a+"))
        if board.is_game_over():
            break
        result = await engine.play(board, chess.engine.Limit(time=tlim))
        board.push(result.move)
        print(board.uci(result.move), file=open("stockfish_test1.pgn", "a+"))
    # while board.is_game_over():
    #     print(board.move_stack, file=open("stockficsh_test.pgn", "w+"), end="\n\n")

    await engine.quit()

asyncio.set_event_loop_policy(chess.engine.EventLoopPolicy())
asyncio.run(main())
