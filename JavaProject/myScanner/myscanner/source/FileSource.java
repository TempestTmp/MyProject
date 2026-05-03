package myscanner.source;

import java.io.*;

public class FileSource implements ICharsSource {
    private final BufferedReader in;
    private final int lenBuffer;

    private final char[] buffer;

    private int countRead;
    private int pos = 0;

    FileSource(final String fileName, final String encoding, final int lenBuffer)
            throws FileNotFoundException, UnsupportedEncodingException, IOException {
        this.lenBuffer = lenBuffer;
        this.buffer = new char[lenBuffer];

        this.in = new BufferedReader(new InputStreamReader(new FileInputStream(fileName), encoding), lenBuffer);
        updateBuffer();
    }

    public FileSource(final String fileName, final String encoding)
            throws FileNotFoundException, UnsupportedEncodingException, IOException {
        this(fileName, encoding, 1024);
    }

    FileSource(final String fileName)
            throws FileNotFoundException, UnsupportedEncodingException, IOException {
        this(fileName, "utf8", 1024);
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