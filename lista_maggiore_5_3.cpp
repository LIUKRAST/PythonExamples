#include <iostream>
#include <ostream>
#include <random>
#include <vector>
using namespace std;


int lunghezzaFroci(const vector<int>& v) {
    int lt = 0;
    for(int r = 0; r < v.size(); r++) {
        int c3 = 0;
        int c5 = 0;
        if(v.at(r) == 3)
            c3++;
        else if(v.at(r) == 5)
            c5++;
        for(int j = r+1; j < v.size(); j++) {
            if(v.at(j) == 3)
                c3++;
            else if(v.at(j) == 5)
                c5++;
        }
        if(c3 == c5) {
            if(v.size() - r > lt)
                lt = v.size() - r;
        } else {
            for(int x = v.size() - 1; x >= r; x--) {
                if(v.at(x) == 3)
                    c3--;
                else if(v.at(x) == 5)
                    c5--;
                if(c3 == c5) {
                    int temp = x - r;
                    if(temp > lt)
                        lt = temp;
                    break;
                }
            }
        }
    }
    return lt;
}

int mthRandom() {
    random_device rd;
    mt19937 mt(rd());
    uniform_int_distribution dist(0, 10);
    return dist(mt);
}

int main() {
    vector<int> v;
    cout << "[ ";
    for(int i = 0; i < 10; i++) {
        int random = mthRandom();
        v.push_back(random);
        cout << to_string(random) + ", ";
    }
    cout << "]" << endl;
    cout << lunghezzaFroci(v) << endl;
    return 0;
}