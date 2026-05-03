package connectFour;

public interface IConnectFour {
    int play();
    int play(final IOut out, final IIn in,
             final IBoard board, final IPlayer[] players,
                final IRowColK rowColK, final boolean log);
}
