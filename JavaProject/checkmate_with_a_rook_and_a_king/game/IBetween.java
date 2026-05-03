package game;

public interface IBetween {
    boolean isKingsMoveCorrect(IMove move);
    boolean isRooksMoveCorrect(IMove move);
    boolean checkmateСheck();
    IMove getPosition(EChessPiece chessPiece);
}
