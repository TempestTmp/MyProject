package game;

public interface IPlayer {
    IMove move(IBetween between);
    EPlayer getPLayer();
}
