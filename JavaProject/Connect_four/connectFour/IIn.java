package connectFour;

public interface IIn {
    IRowColK getRowColK();
    int getCol(int max);
    int getNumber(int min);
    int getNumber(int min, int max);
    void close();
}