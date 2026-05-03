import java.io.BufferedReader;
import java.io.InputStreamReader;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            int read = reader.read();
            while (read >= 0) {
                System.out.println(read);
                read = reader.read();
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}