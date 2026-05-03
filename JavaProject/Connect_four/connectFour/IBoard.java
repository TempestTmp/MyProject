package connectFour;

public interface IBoard {
    IFirewall getFirewall();
    ECell getCell(int row, int col);
    EResult getResult(IMove move);
    EResult makeMove(IMove move);
    boolean isRight(IMove move);
}