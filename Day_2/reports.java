import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

class Reports {
    public static void main(String[] args) {
        int safeReports = 0;
        int dampenedReports = 0;
        try (BufferedReader br = new BufferedReader(new FileReader("day2_input.txt"))) {
            String line;
            ArrayList<String[]> badReports = new ArrayList<>();
            while ((line = br.readLine()) != null) {
                String[] levelsString = line.split(" ");
                Object[] levels = Arrays.stream(levelsString).map(Integer::valueOf).toArray();
                if(isArraySafe(levels)) {
                    safeReports++;
                } else {
                    for (int i = 0; i < levels.length; i++) {
                        if (isArraySafe(concatWithCopy2(Arrays.copyOfRange(levels, 0, i), 
                        Arrays.copyOfRange(levels, i+1, levels.length)))) {
                            dampenedReports++;
                            break;
                        }
                        if (i == levels.length -1 ) {
                            badReports.add(levelsString);
                        }
                    }
                }
            }
            // badReports.forEach((report) -> {
            //     System.out.println(Arrays.toString(report));
            // });
            System.out.println("Safe reports: "+safeReports);
            System.out.println("Dampened reports: "+dampenedReports);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static boolean isArraySafe(Object[] array) {
        boolean increase = false;
        boolean decrease = false;
        for (int i = 1; i < array.length; i++) {
            int diff = Math.abs((int) array[i] - (int) array[i-1]);
            if (diff > 3 || diff < 1) {
                return false;
            }

            if ((int) array[i] > (int) array[i-1]) {
                increase = true;
            } else {
                decrease = true;
            }

            if (increase && decrease) {
                return false;
            }
        }
        return true;
    }

    public static boolean isSubArraySafe(Object[] startOfArray, Object[] endOfArray) {
        int increment = 1;
        int decrement = 1;
        int diff = 0;
        Object [] subArray = concatWithCopy2(startOfArray, endOfArray);
        for (int i = 1; i < subArray.length; i++) {
            int current = (int) subArray[i];
            int previous = (int) subArray[i-1];
            if (current >= previous) {
                diff = current-previous;
                if (decrement > 1 || diff > 3 || diff < 1) {
                    return false;
                }
                increment++;
            } else {
                diff = previous-current;
                if (increment > 1 || diff > 3 || diff < 1) {
                    return false;
                }
                decrement++;
            }
        }
        return true;
    }

    static <T> T concatWithCopy2(T array1, T array2) {
        if (!array1.getClass().isArray() || !array2.getClass().isArray()) {
            throw new IllegalArgumentException("Only arrays are accepted.");
        }

        Class<?> compType1 = array1.getClass().getComponentType();
        Class<?> compType2 = array2.getClass().getComponentType();

        if(!compType1.equals(compType2)) {
            throw new IllegalArgumentException("Two arrays have different types.");
        }

        int len1 = Array.getLength(array1);
        int len2 = Array.getLength(array2);

        @SuppressWarnings("unchecked")
        T result = (T) Array.newInstance(compType1, len1+len2);

        System.arraycopy(array1, 0, result, 0, len1);
        System.arraycopy(array2, 0, result, len1, len2);
        return result;
    }
}