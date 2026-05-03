package connectFour;


// получить число -1 исправить в начале


public class ConnectFour implements IConnectFour {
    @Override
    public int play() {
        return 0;
    }

    @Override
    public int play(final IOut out, final IIn in,
                        final IBoard board, final IPlayer[] players,
                            final IRowColK rowColK, final boolean log) {

        out.start();
        final int row = rowColK.getRow(), col = rowColK.getCol(), k = rowColK.getK();

        final IGame game = new Game(board, players, out, log);

        int result = game.play();

        if (result == 0) {
            out.vin(0);
            out.lose(1);
        } else if (result == 1) {
            out.vin(1);
            out.lose(0);
        } else {
            out.draw();
        }
        out.end();

        return result;

        // in.close()
    }

    public static void main(String[] args) {
        final IOut out = new Out();
        final IIn in = new In(out);

        out.start();
        final IRowColK rowColK = in.getRowColK();

        final int row = rowColK.getRow(), col = rowColK.getCol(), k = rowColK.getK();

        final IBoard board = new Board(row, col, k);
        final IPlayer[] players = {new PlayerRandom(ECell.X), new PlayerRandom(ECell.O)};
        final IGame game = new Game(board, players, out, true);

        int result = game.play();

        if (result == 0) {
            out.vin(0);
            out.lose(1);
        } else if (result == 1) {
            out.vin(1);
            out.lose(0);
        } else {
            out.draw();
        }
        out.end();
        in.close();
    }
}
