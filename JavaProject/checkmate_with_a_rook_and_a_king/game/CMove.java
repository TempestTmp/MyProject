package game;

public class CMove implements IMove {
    private final EChessPiece piece;
    private final int rank;
    private final int file;

    public CMove(EChessPiece piece, int rank, int file) {
        this.piece = piece;
        this.rank = rank;
        this.file = file;
    }

    @Override
    public int getRank() {
        return rank;
    }

    @Override
    public int getFile() {
        return file;
    }

    @Override
    public EChessPiece getChessPiece() {
        return piece;
    }

    @Override
    public int getAlgNot() {
        return 0;
    }
}
