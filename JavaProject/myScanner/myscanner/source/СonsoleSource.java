package myscanner.source;

import java.io.*;

public class СonsoleSource implements ICharsSource {
    private final BufferedReader in;
    private final int lenBuffer;

    private final char[] buffer;

    private int countRead;
    private int pos = 0;

    public СonsoleSource(final InputStream stream, final String encoding, final int lenBuffer)
            throws UnsupportedEncodingException, IOException {
        this.lenBuffer = lenBuffer;
        this.buffer = new char[lenBuffer];

        this.in = new BufferedReader(new InputStreamReader(stream, encoding), lenBuffer);
        updateBuffer();
    }

    public СonsoleSource(final InputStream stream, final String encoding)
            throws UnsupportedEncodingException, IOException {
        this(stream, encoding,1024);
    }

    public СonsoleSource(final InputStream stream)
            throws UnsupportedEncodingException, IOException {
        this(stream, "utf8");
    }

    private void updateBuffer() throws IOException {
        countRead = in.read(buffer, 0, lenBuffer);
        if (countRead < 0) {
            close();
        }
        pos = 0;
    }

    public void close() throws IOException {
        in.close();
    }


    @Override
    public boolean hasNext() throws IOException {
        if (countRead < 0) {
            return false;
        } else if (pos >= countRead) {
            updateBuffer();
        }

        return countRead >= 0;
    }

    @Override
    public char next() throws IOException {
        if (pos >= countRead) {
            updateBuffer();
        }

        return buffer[pos++];
    }

    @Override
    public IllegalArgumentException error(final String message) {
        return new IllegalArgumentException(pos + ": " + message);
    }
}
