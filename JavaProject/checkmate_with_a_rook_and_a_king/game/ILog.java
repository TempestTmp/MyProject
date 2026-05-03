package game;

public interface ILog {
    EPlayer getPlayer();
    EResult getResult();
    IMove getMove();
    String getNote();
}
