import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("day3_input.txt"))) {
            String line;
            int sum = 0;
            boolean process = true;
            Pattern pattern = Pattern.compile("(mul[(]{1}[0-9]{1,3},[0-9]{1,3}[)]{1})|do[(][)]|don't[(][)]");
            while ((line = br.readLine()) != null) {
                Matcher matcher = pattern.matcher(line);
                while (matcher.find()) {
                    String match = matcher.group();
                    if(match.equals("do()")) {
                        process = true;
                    } else if (match.equals("don't()")) {
                        process = false;
                    } else {
                        if (process) {
                            sum += Integer.parseInt(match.substring(4,match.indexOf(",")))
                                    * Integer.parseInt(match.substring(match.indexOf(",") + 1, match.length()-1));
                        }
                    }
                }
            }

            System.out.println(sum);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
}
