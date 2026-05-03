package myscanner;

import myscanner.source.FileSource;
import myscanner.source.ICharsSource;
import myscanner.source.StringSource;
import myscanner.source.СonsoleSource;

import java.io.IOException;
import java.io.InputStream;

public class BaseScanner {
    private static final char END = '\0';
    private final ICharsSource source;
    private char ch;

    public BaseScanner(final String input) throws IOException {
        source = new StringSource(input);
        take();
    }

    public BaseScanner(final String fileName, final String encoding) throws IOException {
        source = new FileSource(fileName, encoding);
        take();
    }

    public BaseScanner(final InputStream stream, final String encoding) throws IOException {
        source = new СonsoleSource(stream);
        take();
    }
    public BaseScanner(final InputStream stream) throws IOException {
        this(stream, "utf8");
    }

    protected char take() throws IOException {
        final char res = ch;
        ch = source.hasNext() ? source.next() : END;
        return res;
    }

    protected boolean take(final char expected) throws IOException {
        if (ch == expected) {
            take();
            return true;
        } else {
            return false;
        }
    }

    protected char test() {
        return ch;
    }

    protected boolean test(final char expected) {
        return ch == expected;
    }

    protected boolean eof() {
        return ch == END;
    }

    protected IllegalArgumentException error(final String message) {
        return source.error(message);
    }
}
