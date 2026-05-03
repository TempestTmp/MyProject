package connectFour;

import java.util.Random;

public class PlayerRandom implements IPlayer {
    private final Random random;
    private final ECell player;

    public PlayerRandom(final ECell player) {
        this.random = new Random();
        this.player = player;
    }

    @Override
    public IMove move(final IFirewall firewall) {
        while (true) {
            int col = random.nextInt(firewall.getColLength());
            int row = firewall.getRow(col);
            if (firewall.isRight(col)) {
                return new Move(player, col, row);
            }
        }
    }

    @Override
    public ECell getPLayer() {
        return player;
    }
}
