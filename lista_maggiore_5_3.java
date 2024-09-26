package main;

import java.util.ArrayList;

public class Example {
    @SuppressWarnings("unused")
    public static void main(String[] args) {
        final ArrayList<Integer> list = new ArrayList<>();
        for(int i = 0; i < 2000; i++) {
            list.add((int)(Math.random() * 10));
        }
        System.out.println(list);
        System.out.println(someFunc(list));
    }

    public static int someFunc(ArrayList<Integer> v) {
        int lt = 0;
        for(int r = 0; r < v.size(); r++) {
            int c3 = 0;
            int c5 = 0;
            if(v.get(r) == 3)
                c3++;
            else if(v.get(r) == 5)
                c5++;

            for(int j = r+1; j < v.size(); j++) {
                if(v.get(j) == 3)
                    c3++;
                else if(v.get(j) == 5)
                    c5++;
            }
            if(c3 == c5)
                if(v.size() - r> lt)
                    lt = v.size() - r;
            else for(int x = v.size() - 1; x > r; x--) {
                    if(v.get(x) == 3)
                        c3--;
                    else if(v.get(x) == 5)
                        c5--;
                    if(c3 == c5) {
                        final int temp = x - r;
                        if(temp > lt)
                            lt = temp;
                        break;
                    }
            }
        }
        return lt;
    }
}
