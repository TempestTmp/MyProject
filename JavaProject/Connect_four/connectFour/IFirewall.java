package connectFour;

public interface IFirewall {
    ECell getCell(int row, int col);
    int getRowLength();
    int getColLength();
    int getRow(int col);
    EResult getResult(IMove move);
    boolean isRight(int col);
}