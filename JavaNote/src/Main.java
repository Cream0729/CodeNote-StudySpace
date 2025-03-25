import java.util.Random;
import java.util.TreeMap;

public class Main {
    public static void main(String[] args) {
        Random rand = new Random();
        boolean flag = true;

        TreeMap<String, Integer> map = new TreeMap<>();
        for (int i = 0; i <= 20; i++) {
            map.put((i + 100 + ""), rand.nextInt(10));
        }
        System.out.println("Value about key \"105\" is: " + map.get("105"));
        System.out.println();

        for (int i : getKey(map, 5)) {
            if (i == 0) {
                break;
            } else {
                System.out.println("The key about value 5 is: \"" + i + '\"');
                flag = false;
            }
        }

        if (flag) {
            System.out.println("Have not key about value 5.");
        }
    }

    public static int[] getKey(TreeMap<String, Integer> map, int value) {
        int[] keys = new int[5];
        int keyNext = 0;
        for (int i = 100; i <= 105; i++) {
            if (map.get(String.valueOf(i)) == value) {
                keys[keyNext++] = i;
            }
        }
        return keys;
    }
}