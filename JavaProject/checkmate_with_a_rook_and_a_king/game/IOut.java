package game;

public interface IOut {
    void start();
    void vin(int playersNumber);
    void lose(int playersNumber);
    void draw();
    void end();

    void print(String message);
    String repeat(char chr, int repeat);

    void printBoard(IBetween between);
}