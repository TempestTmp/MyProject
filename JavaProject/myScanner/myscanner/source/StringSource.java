package myscanner.source;

public class StringSource implements ICharsSource {
    private final String input;
    private int pos = 0;

    public StringSource(final String input) {
        this.input = input;
    }

    @Override
    public boolean hasNext() {
        return pos < input.length();
    }

    @Override
    public char next() {
        return input.charAt(pos++);
    }

    @Override
    public IllegalArgumentException error(final String message) {
        return new IllegalArgumentException(pos + ": " + message);
    }
}
