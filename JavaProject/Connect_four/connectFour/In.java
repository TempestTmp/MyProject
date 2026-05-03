package connectFour;

import java.util.Scanner;

public class In implements IIn {
    private final IOut out;
    private final Scanner scan;

    public In(IOut out) {
        this.out = out;
        scan = new Scanner(System.in);
    }

    private void separator(final int len) {
        out.print("|" + out.repeat('-', len) + "|");
    }

    @Override
    public IRowColK getRowColK() {
        String message;

        message = "Enter the number of lines in the game:";
        separator(message.length());
        out.print(message);
        int row = getNumber(1) + 1;


        message = "Enter the number of columns in the game:";
        separator(message.length());
        out.print(message);
        int col = getNumber(1) + 1;

        message = "Enter the number of balls in the line to win:";
        separator(message.length());
        out.print(message);
        int k = getNumber(1) + 1;

        message = "Enter the number of balls ";

        return new RowColK(row, col, k);
    }

    @Override
    public int getCol(int max) {
        out.print("Enter the column number for your move:");
        return getNumber(1, max);
    }

    @Override
    public int getNumber(int min, int max) {
        int number = -1;
        do {
            try {
                out.print("Enter a number between " + (min - 1) + " and " + (max + 1));
                number = scan.nextInt();
            } catch (RuntimeException e) {
                scan.next();
            }
        } while (number < min || number > max);

        return number - 1;
    }

    @Override
    public void close() {
        scan.close();
    }

    @Override
    public int getNumber(int min) {
        int number = -1;
        do {
            try {
                out.print("Enter a number greater than or equal to " + min);
                number = scan.nextInt();
            } catch (RuntimeException e) {
                scan.next();
            }
        } while (number < min);


        return number - 1;
    }
}
