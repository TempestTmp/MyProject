package game;

public class CGame implements IGame {
    private final IBoard board;
    private final IPlayer[] players;
    private final IOut out;

    //private final ArrayList<ILog> list = new ArrayList<>();
    private final boolean log;
    //private final IGameLogs gameLogs;

    public CGame(IBoard board, IPlayer[] players, IOut out, boolean log) {
        this.board = board;
        this.players = players;
        this.out = out;
        this.log = log;
    }

    public CGame(IBoard board, IPlayer[] players, IOut out) {
        this(board, players, out, true);
    }

    @Override
    public int play() {
        int moveNumber = 0;
        while (true) {
            for (int i = 0; i < players.length; i++) {
                EResult result = action(moveNumber, players[i]);

                if (result == EResult.Win) {
                    return i;
                } else if (result == EResult.Draw) {
                    return -1;
                }
            }
        }
    }

    public EResult action(final int moveNumber, final IPlayer player) {
        IMove move;
        do {
            move = player.move(board.getBetween());
        } while (!board.isMoveRight(move));

        final EResult result = board.makeMove(move);

        if (result == EResult.Win) {
            log(moveNumber, new CLog(player.getPLayer(), result, move, "Player " + player.getPLayer() + "'s move " + move.getAlgNot() + " leads to victory (" + moveNumber + ")"));
        } else if (result == EResult.Draw) {
            log(moveNumber, new CLog(player.getPLayer(), result, move, "Player " + player.getPLayer() + "'s move " + move.getAlgNot() + " results in a draw (" + moveNumber + ")"));
        } else if (result == EResult.Lose) {
            log(moveNumber, new CLog(player.getPLayer(), result, move, "Player " + player.getPLayer() + "'s move " + move.getAlgNot() + " leads to a defeat (" + moveNumber + ")"));
        } else if (result == EResult.Next) {
            log(moveNumber, new CLog(player.getPLayer(), result, move, "Player " + player.getPLayer() + " has made a move " + move.getAlgNot() + "(" + moveNumber + ")"));
        }

        return result;
    }

    public void log(int moveNumber, ILog log) {
        if (this.log) {
            //list.add(log);
            out.print(log.getNote());
            out.printBoard(board.getBetween());
        }
    }

}