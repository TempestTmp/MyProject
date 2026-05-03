package connectFour;

public interface IPlayer {
    IMove move(IFirewall firewall);
    ECell getPLayer();
}
