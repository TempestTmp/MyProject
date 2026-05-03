package connectFour;

public class Firewall implements IFirewall {
    private static final int[][] steps = {{1, 0}, {0, 1}, {1, 1}, {-1, 1}};

    private final ECell[][] board;
    private final int row, col, k;
    private final int full;
    private final int[] fullness;

    public Firewall(ECell[][] board, int row, int col, int k, int full, int[] fullness) {
        this.board = board;
        this.row = row;
        this.col = col;
        this.k = k;
        this.full = full;
        this.fullness = fullness;
    }

    @Override
    public ECell getCell(int row, int col) {
        return board[row][col];
    }

    @Override
    public int getRowLength() {
        return row;
    }

    @Override
    public int getColLength() {
        return col;
    }

    @Override
    public int getRow(int col) {
        int row = 0;
        while (row + 1 < this.row && getCell(row + 1, col) == ECell.E) {
            row++;
        }
        return row;
    }

    private boolean isRight(int row, int col) {
        return 0 <= row && 0 <= col && row < this.row && col < this.col;
    }

    @Override
    public EResult getResult(IMove move) {
        int col = move.getCol();
        int row = move.getRow();

        for (int[] step : steps) {
            int count = 1, ind = 1;
            ECell player = move.getPLayer();
            boolean flag1 = true, flag2 = true;
            while (flag1 || flag2) {
                ECell cell = getCell(row + ind * step[0], col + ind * step[1]);

                if (flag1 && isRight(row + ind * step[0], col + ind * step[1]) &&
                        getCell(row + ind * step[0], col + ind * step[1]).equals(move.getPLayer())) {
                    count++;
                } else {
                    flag1 = false;
                }

                cell = getCell(row + -1 * ind * step[0], col + -1 * ind * step[1]);
                if (flag2 && isRight(row + -1 * ind * step[0], col + -1 * ind * step[1]) &&
                        getCell(row + -1 * ind * step[0], col + -1 * ind * step[1]).equals(move.getPLayer())) {
                    count++;
                } else {
                    flag2 = false;
                }
                ind++;

            }
            if (count >= k) {
                return EResult.Win;
            }
        }

        if (fullness[0] + 1 >= full) {
            return EResult.Draw;
        }

        return EResult.Next;
    }

    @Override
    public boolean isRight(int col) {
        return 0 <= col && col < this.col && getCell(0, col) == ECell.E;
    }
}
