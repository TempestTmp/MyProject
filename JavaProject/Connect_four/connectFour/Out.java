package connectFour;

import java.util.Arrays;
import java.util.Map;

public class Out implements IOut {
    private static final Map<ECell, Character> SYMBOLS = Map.of(
            ECell.X, 'X',
            ECell.O, 'O',
            ECell.E, '·'
    );

    @Override
    public void start() {
        print("Start of the game");
    }

    @Override
    public void vin(final int playersNumber) {
        print("Player " + playersNumber + " wins");
    }

    @Override
    public void lose(final int playersNumber) {
        print("Player " + playersNumber + " lost");
    }

    @Override
    public void draw() {
        print("The game ended in a draw");
    }

    @Override
    public void end() {
        print("End of the game");
    }

    @Override
    public void print(final String message) {
        System.out.println(message);
    }

    @Override
    public char getSymbol(ECell cell) {
        return SYMBOLS.get(cell);
    }

    @Override
    public String repeat(final char chr, final int repeat) {
        char[] chars = new char[repeat];
        Arrays.fill(chars, chr);
        String string = new String(chars);
        return string;
    }

    @Override
    public void printBoard(final IFirewall firewall) {
        print("Position on the board:");

        final int row = firewall.getRowLength(), col = firewall.getColLength();

        for (int i = 1; i < col + 1; i++) {
            System.out.print(i + " ");
        }

        print("");

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                int mlog = String.valueOf(c).length();
                System.out.print(getSymbol(firewall.getCell(r, c)) + repeat(' ', mlog));
            }
            print("");
        }
        print("");
    }
}
