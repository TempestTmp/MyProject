package game;

public interface IBoard {
    IBetween getBetween();
    EResult makeMove(IMove move);
    boolean isMoveRight(IMove move);
}
