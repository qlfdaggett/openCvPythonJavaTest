import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test {

    public static void main(String[] args) throws IOException {
        Runtime rt = Runtime.getRuntime();
        Process proc = rt.exec("python3 src/imageMatcher.py images/tablet_shot.png images/bluetooth.png");

        BufferedReader stdInput = new BufferedReader(new
                InputStreamReader(proc.getInputStream()));

        BufferedReader stdError = new BufferedReader(new
                InputStreamReader(proc.getErrorStream()));

        String res = stdInput.readLine();
        int[] coords = new int[] {
                Integer.valueOf(res.split(" ")[0]),
                Integer.valueOf(res.split(" ")[1])
        };

        System.out.println("Coordinates of bluetooth : (" + coords[0] + ", " + coords[1] + ")");
    }
}
