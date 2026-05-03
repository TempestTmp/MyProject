package connectFour;

public interface IOut {
    void start();
    void vin(int playersNumber);
    void lose(int playersNumber);
    void draw();
    void end();

    void print(String message);
    char getSymbol(ECell cell);
    String repeat(char chr, int repeat);

    void printBoard(IFirewall firewall);
}