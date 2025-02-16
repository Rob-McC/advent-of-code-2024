import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day4 {
    public static void main(String[] args) {
        int numOfLines = 0;
        int xmasCount = 0;
        String[][] xmasList = new String[140][140];
        try (BufferedReader br = new BufferedReader(new FileReader("day4_input.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                xmasList[numOfLines] = line.split("");
                numOfLines++;
            }

            //Part 1
            for (int i = 0; i < xmasList.length; i++) {
                for (int j = 0; j < xmasList[i].length; j++) {
                    if (xmasList[i][j].equals("X") || xmasList[i][j].equals("S")) {
                        //Check horizontally if j isn't 4 away from the end
                        xmasCount += checkHorizontal(xmasList, xmasList[i][j], i, j);

                        //Check vertically down if i isn't 4 away from end
                        xmasCount += checkVerticalDown(xmasList, xmasList[i][j], i, j);

                        //Check forward diagonally if j is < 4 from the end
                        xmasCount += checkDiagonalForward(xmasList, xmasList[i][j], i, j);

                        //Check back diagonally if j is >= 3 and i isn't 4 away from the end
                        xmasCount += checkDiagonalBackwards(xmasList, xmasList[i][j], i, j);
                    }
                }
            }
            System.out.println(xmasCount);

            //Part 2
            int xShapeMasCount = 0;
            for (int i = 0; i < xmasList.length; i++) {
                for (int j = 0; j < xmasList[i].length; j++) {
                    if (xmasList[i][j].equals("M") || xmasList[i][j].equals("S")) {
                        //Check X so long as col is 3 away from the end
                        xShapeMasCount += checkXShape(xmasList, xmasList[i][j], i, j);
                    }
                }
            }
            System.out.println(xShapeMasCount);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static int checkHorizontal(String[][] xmasList, String letter, int row, int col) {
        if (col <= 136 ) {
            if (letter.equals("X")) {
                return (xmasList[row][col+1].equals("M") && xmasList[row][col+2].equals("A") && xmasList[row][col+3].equals("S")) ? 1 : 0;
            } else if (letter.equals("S")) {
                return (xmasList[row][col+1].equals("A") && xmasList[row][col+2].equals("M") && xmasList[row][col+3].equals("X")) ? 1 : 0;
            }
        }
        return 0;
    }

    public static int checkVerticalDown(String[][] xmasList, String letter, int row, int col) {
        if (row <= 136 ) {
            if (letter.equals("X")) {
                return (xmasList[row+1][col].equals("M") && xmasList[row+2][col].equals("A") && xmasList[row+3][col].equals("S")) ? 1 : 0;
            } else if (letter.equals("S")) {
                return (xmasList[row+1][col].equals("A") && xmasList[row+2][col].equals("M") && xmasList[row+3][col].equals("X")) ? 1 : 0;
            }
        }
        return 0;
    }

    public static int checkDiagonalForward(String[][] xmasList, String letter, int row, int col) {
        if (row <=136 && col <= 136 ) {
            if (letter.equals("X")) {
                return (xmasList[row+1][col+1].equals("M") && xmasList[row+2][col+2].equals("A") && xmasList[row+3][col+3].equals("S")) ? 1 : 0;
            } else if (letter.equals("S")) {
                return (xmasList[row+1][col+1].equals("A") && xmasList[row+2][col+2].equals("M") && xmasList[row+3][col+3].equals("X")) ? 1 : 0;
            }
        }
        return 0;
    }

    public static int checkDiagonalBackwards(String[][] xmasList, String letter, int row, int col) {
        if (row <=136 && col >= 3 ) {
            if (letter.equals("X")) {
                return (xmasList[row+1][col-1].equals("M") && xmasList[row+2][col-2].equals("A") && xmasList[row+3][col-3].equals("S")) ? 1 : 0;
            } else if (letter.equals("S")) {
                return (xmasList[row+1][col-1].equals("A") && xmasList[row+2][col-2].equals("M") && xmasList[row+3][col-3].equals("X")) ? 1 : 0;
            }
        }
        return 0;
    }

    public static int checkXShape(String[][] xmasList, String letter, int row, int col) {
        if (row <=137 && col <= 137 ) {
            boolean backwardsCross = (xmasList[row+2][col].equals("M") && xmasList[row][col+2].equals("S")) ||
                (xmasList[row+2][col].equals("S") && xmasList[row][col+2].equals("M"));
            if (letter.equals("M")) {
                boolean forwardCross = xmasList[row+1][col+1].equals("A") && xmasList[row+2][col+2].equals("S");
                return (forwardCross && backwardsCross) ? 1 : 0;
            } else if (letter.equals("S")) {
                boolean forwardCross = xmasList[row+1][col+1].equals("A") && xmasList[row+2][col+2].equals("M");
                return (forwardCross && backwardsCross) ? 1 : 0;
            }
        }
        return 0;
    }
}
