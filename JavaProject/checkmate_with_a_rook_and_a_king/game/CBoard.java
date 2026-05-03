package game;

import java.util.HashMap;
import java.util.Random;

public class CBoard implements IBoard {
    private final HashMap<EChessPiece, IMove> map;
    private final IBetween between;

    public CBoard(IMove bking, IMove wking, IMove wrook) {
        this.map = new HashMap<>();
        map.put(bking.getChessPiece(), bking);
        map.put(wking.getChessPiece(), wking);
        map.put(wrook.getChessPiece(), wrook);

        between = new CBetween(map);
    }

    @Override
    public IBetween getBetween() {
        return between;
    }

    @Override
    public boolean isMoveRight(IMove move) {
        boolean result = false;
        if (move.getChessPiece() == EChessPiece.BKING || move.getChessPiece() == EChessPiece.WKING) {
            result = between.isKingsMoveCorrect(move);
        } else if (move.getChessPiece() == EChessPiece.WROOK) {
            result = between.isRooksMoveCorrect(move);
        }
        return result;
    }

    @Override
    public EResult makeMove(IMove move) {
        map.put(move.getChessPiece(), move);

        EResult result;
        if (between.checkmateСheck()) {
            result = EResult.Win;
        } else {
            result = EResult.Next;
        }
        return result;
    }
}
