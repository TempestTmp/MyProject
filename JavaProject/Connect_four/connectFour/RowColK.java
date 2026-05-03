package connectFour;

public class RowColK implements IRowColK {
    private final int row;
    private final int col;
    private final int k;

    public RowColK(int row, int col, int k) {
        this.row = row;
        this.col = col;
        this.k = k;
    }

    @Override
    public int getCol() {
        return col;
    }

    @Override
    public int getRow() {
        return row;
    }

    @Override
    public int getK() {
        return k;
    }
}
