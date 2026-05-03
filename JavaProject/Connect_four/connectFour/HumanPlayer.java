package connectFour;

public class HumanPlayer implements IPlayer {
    private final ECell player;
    private final IOut out;
    private final IIn in;

    public HumanPlayer(final ECell player, IOut out, IIn in) {
        this.player = player;
        this.out = out;
        this.in = in;
    }

    @Override
    public IMove move(final IFirewall firewall) {
        out.print("Player X is your turn");
        out.printBoard(firewall);

        int col;
        do {
            col = in.getCol(firewall.getRowLength());
            if (!firewall.isRight(col)) {
                out.print("You can't make this move");
            }
        } while (!firewall.isRight(col));
        int row = firewall.getRow(col);
        return new Move(player, col, row);
    }

    @Override
    public ECell getPLayer() {
        return player;
    }
}
