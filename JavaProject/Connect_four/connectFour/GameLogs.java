package connectFour;

import java.util.ArrayList;
import java.util.HashMap;

public class GameLogs implements IGameLogs {
    private final ArrayList<ILog> list;

    public GameLogs(ArrayList<ILog> list) {
        this.list = list;
    }

    @Override
    public ILog getLog(int moveNumber) {
        return list.get(moveNumber);
    }

    @Override
    public int size() {
        return list.size();
    }


    @Override
    public ECell getPlayer(int moveNumber) {
        return list.get(moveNumber).getPlayer();
    }

    @Override
    public EResult getResult(int moveNumber) {
        return list.get(moveNumber).getResult();
    }

    @Override
    public String getNote(int moveNumber) {
        return list.get(moveNumber).getNote();
    }

    @Override
    public IMove getMove(int moveNumber) {
        return list.get(moveNumber).getMove();
    }
}
