package game;

public interface IMove {
    int getRank();
    int getFile();
    EChessPiece getChessPiece();
    int getAlgNot();
}