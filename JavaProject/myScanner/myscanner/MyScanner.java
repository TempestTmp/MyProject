package myscanner;

import java.io.IOException;
import java.io.InputStream;

public class MyScanner extends BaseScanner {
    private String lineSeparator = System.lineSeparator();
    private ThisSeparator separator = (mychar) -> Character.isWhitespace(mychar);

    public MyScanner(String input) throws IOException {
        super(input);
    }

    public MyScanner(String fileName, String encoding) throws IOException {
        super(fileName, encoding);
    }

    public MyScanner(InputStream stream) throws IOException {
        super(stream);
    }

    private StringBuilder word;
    private boolean flagStart = true;

    private boolean flagHas = false;
    private boolean flagHasInt = false;

    private boolean flagNowHasLineSeparator = false;
    private boolean flagGetTake = false;

    public boolean updateSeparator(final ThisSeparator separator) {
        /*
        for (int i = 0; i < lineSeparator.length(); i++) {
            if (separator.isCharSeparator(lineSeparator.charAt(i))) {
                return false;
            }
        }
         */
        this.separator = separator;
        return true;
    }

    public void updateLineSeparator(final String lineSeparator) {
        this.lineSeparator = lineSeparator;
    }

    private void skipWhitespace() throws IOException {
        while (separator.isCharSeparator(test())) {
            flagGetTake = false;
            take();
        }
    }

    private boolean isSeparator() throws IOException {
        int ind = 0;
        while (test(lineSeparator.charAt(ind))) {
            ind++;
            if (ind >= lineSeparator.length()) {
                flagNowHasLineSeparator = true;
                flagGetTake = true;
                return true;
            }
            take();
        }
        word.append(lineSeparator.substring(0, ind));
        return false;
    }

    public boolean emptyLine() throws IOException {
        if (flagGetTake) {
            flagGetTake = false;
            take();
        }

        int count = 0;
        while (separator.isCharSeparator(test()) || lineSeparator.contains(String.valueOf(test()))) {
            if (test(lineSeparator.charAt(count))) {
                count++;
                if (count >= lineSeparator.length()) {
                    boolean flag = false;
                    if (flagStart || flagNowHasLineSeparator) {
                        flag = true;
                    }
                    flagStart = false;
                    flagNowHasLineSeparator = true;
                    flagGetTake = true;
                    return flag;
                }
            } else {
                count = 0;
            }
            take();
        }
        return false;
    }

    public String next() throws IOException {
        if (flagHasInt) {
            flagHasInt = false;
            return word.toString();
        }

        if (flagStart) {
            flagStart = false;
        }

        if (flagGetTake) {
            flagGetTake = false;
            take();
        }


        word = new StringBuilder();
        skipWhitespace();

        while (!isSeparator() && !separator.isCharSeparator(test()) && !eof()) {
            flagNowHasLineSeparator = false;
            word.append(take());
        }
        
        return word.toString();
    }

    public boolean hasNext() throws IOException {
        skipWhitespace();
        return !eof();
    }

    public int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    public boolean hasNextInt() throws IOException {
        if (flagHasInt) {
            return true;
        }

        try {
            Integer.parseInt(next());
            flagHasInt = true;
            return true;
        } catch (RuntimeException e) {
            flagHasInt = false;
            return false;
        }
    }

    public boolean isFlagHas() {
        return flagHas;
    }

    public void setFlagHas(boolean flagHas) {
        this.flagHas = flagHas;
    }
}