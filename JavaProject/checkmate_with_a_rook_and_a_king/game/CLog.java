package game;

public class CLog implements ILog {
    private final EPlayer player;
    private final EResult result;
    private final IMove move;
    private final String note;

    public CLog(EPlayer player, EResult result, IMove move, String note) {
        this.player = player;
        this.result = result;
        this.move = move;
        this.note = note;
    }

    @Override
    public EPlayer getPlayer() {
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
