package connectFour;

public interface IGameLogs {
    ILog getLog(int moveNumber);
    int size();

    ECell getPlayer(int moveNumber);
    EResult getResult(int moveNumber);
    String getNote(int moveNumber);
    IMove getMove(int moveNumber);
}