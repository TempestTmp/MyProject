package connectFour;

import java.util.ArrayList;
import java.util.List;

public interface IGame {
    IGameLogs getGameLogs();
    int play();

}