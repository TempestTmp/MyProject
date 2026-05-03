package game;

import java.util.HashMap;

// rank file

public class CBetween implements IBetween {
    private final HashMap<EChessPiece, IMove> map;
    private final EChessPiece[] pieces = {EChessPiece.BKING, EChessPiece.WKING, EChessPiece.WROOK};

    private final int[][] kingsStep = {{-1, 0}, {-1, 1}, {0, 1}, {1, 1}};

    public CBetween(HashMap<EChessPiece, IMove> map) {
        this.map = map;
    }

    private boolean isMoveInABoard(IMove move) {
        return (0 <= move.getFile() && move.getFile() <= 7) && (0 <= move.getRank() && move.getRank() <= 7);
    }

    private boolean sameDiagonalWithTheRook(IMove move) {
        int rank = move.getRank();
        int file = move.getFile();

        return Math.abs(rank - map.get(EChessPiece.WROOK).getRank()) == 0 || Math.abs(file - map.get(EChessPiece.WROOK).getFile()) == 0;
    }

    private boolean inAuraOfKing(IMove move, EChessPiece piece) {
        int rank = move.getRank();
        int file = move.getFile();

        return Math.abs(rank - map.get(piece).getRank()) < 2 && Math.abs(file - map.get(piece).getFile()) < 2;
    }

    @Override
    public boolean isKingsMoveCorrect(IMove move) {
        boolean flag = true;

        if (!isMoveInABoard(move)) {
            flag = false;
        } else if (sameDiagonalWithTheRook(move)) {
            flag = false;
        } else if (move.getChessPiece() == EChessPiece.WKING && inAuraOfKing(move, EChessPiece.BKING)) {
            flag = false;
        } else if (move.getChessPiece() == EChessPiece.BKING && inAuraOfKing(move, EChessPiece.WKING)) {
            flag = false;
        }

        return flag;

    }

    @Override
    public boolean isRooksMoveCorrect(IMove move) {
        boolean flag = true;

        int rank = move.getRank();
        int file = move.getFile();

        if (!isMoveInABoard(move)) {
            flag = false;
        } else if (Math.abs(rank - map.get(EChessPiece.BKING).getRank()) == 0 && Math.abs(file - map.get(EChessPiece.BKING).getFile()) == 0) {
            flag = false;
        } else if (Math.abs(rank - map.get(EChessPiece.WKING).getRank()) == 0 && Math.abs(file - map.get(EChessPiece.WKING).getFile()) == 0) {
            flag = false;
        }

        return flag;
    }

    @Override
    public boolean checkmateСheck() {
        if (sameDiagonalWithTheRook(map.get(EChessPiece.BKING))) {
            int rank = map.get(EChessPiece.BKING).getRank();
            int file = map.get(EChessPiece.WKING).getFile();

            for (int[] step : kingsStep) {
                if (isKingsMoveCorrect(new CMove(EChessPiece.BKING, rank + step[0], file + step[1]))) {
                    return false;
                } else if (isKingsMoveCorrect(new CMove(EChessPiece.BKING, rank - step[0], file - step[1]))) {
                    return false;
                }
            }
            return true;
        }

        return false;
    }


    @Override
    public IMove getPosition(EChessPiece chessPiece) {
        return map.get(chessPiece);
    }
}
