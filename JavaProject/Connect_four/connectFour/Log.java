package connectFour;

public class Log implements ILog {
    private final ECell player;
    private final EResult result;
    private final IMove move;
    private final String note;

    public Log(ECell player, EResult result, IMove move, String note) {
        this.player = player;
        this.result = result;
        this.move = move;
        this.note = note;
    }

    @Override
    public ECell getPlayer() {
        return player;
    }

    @Override
    public EResult getResult() {
        return result;
    }

    @Override
    public IMove getMove() {
        return move;
    }

    @Override
    public String getNote() {
        return note;
    }
}
