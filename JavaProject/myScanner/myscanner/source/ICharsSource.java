package myscanner.source;

import java.io.IOException;

public interface ICharsSource {
    boolean hasNext() throws IOException;
    char next() throws IOException;
    IllegalArgumentException error(final String message);
}