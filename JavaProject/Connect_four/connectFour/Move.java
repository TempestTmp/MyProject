package connectFour;

public class Move implements IMove {
    private final ECell player;
    private final int row, col;

    public Move(final ECell player, final int col, final int row) {
        this.player = player;
        this.col = col;
        this.row = row;
    }

    @Override
    public ECell getPLayer() {
        return player;
    }

    @Override
    public int getCol() {
        return col;
    }

    @Override
    public int getRow() {
        return row;
    }
}
