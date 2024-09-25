import java.util.ArrayList;
import java.util.Scanner;

@SuppressWarnings("unused")
public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Numero da convertire");
    int num = sc.nextInt();
    System.out.println("Base da cui convertire");
    int base1 = sc.nextInt();
    System.out.println("Base a cui convertire");
    int base2 = sc.nextInt();

    System.out.println(STR."Il numero \{num} (base \{base1}) diventa \{base2base(num, base1, base2)} in base \{base2}");
}

private static int bto10(int number, int base) {
    final int tt = number;
    int result = 0;
    ArrayList<Integer> list = new ArrayList<>();
    while (number > 0) {
        final int temp = number % 10;
        list.add(temp);
        if (temp >= base)
            throw new IllegalArgumentException(STR."La cifra \{temp} in \{tt} è maggiore o uguale alla base \{base}");
        number /= 10;
    }
    for (int i = 0; i < list.size(); i++) {
        int k = list.get(i);
        result += (int) (k * Math.pow(base, i));
    }
    return result;
}

private static int tenToB(int number, int base) {
    final ArrayList<Integer> list = new ArrayList<>();
    do {
        list.add(number % base);
        number /= base;
    } while (number != 0);
    int result = 0;
    for (int i = 0; i < list.size(); i++) {
        result += (int) (list.get(i) * Math.pow(10, i));
    }
    return result;
}

private static int base2base(int number, int inBase, int outBase) {
    return tenToB(bto10(number, inBase), outBase);
}
