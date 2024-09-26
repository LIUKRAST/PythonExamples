#include <iostream>
#include <list>
#include <cmath>
#include <valarray>
#include <vector>
using namespace std;

int bTo10(int number, const int base) {
    const int tt = number;
    int result = 0;
    vector<int> list;
    while(number > 0) {
        const int temp = number % 10;
        list.push_back(temp);
        if(temp >= base)
            throw invalid_argument("La cifra " + to_string(temp) + " in " + to_string(tt) + " è maggiore o uguale alla base " + to_string(base));
        number /= 10;
    }
    for(int i = 0; i < list.size(); i++) {
        const int k = list.at(i);
        result += k * static_cast<int>(pow(base, i));
    }
    return result;
}

int tenToB(int number, int base) {
    vector<int> list;
    do {
        list.push_back(number % base);
        number /= base;
    } while (number != 0);
    int result = 0;
    for(int i = 0; i < list.size(); i++) {
        result += list.at(i) * static_cast<int>(pow(10, i));
    }
    return result;
}

int base2base(int number, int inBase, int outBase) {
    return tenToB(bTo10(number, inBase), outBase);
}


int main() {
    int num, base1, base2;
    cout << "Numero da convertire" << endl;
    cin >> num;
    cout << "Base da cui convertire" << endl;
    cin >> base1;
    cout << "Base a cui convertire" << endl;
    cin >> base2;

    cout << "Il numero " + to_string(num) + " (base " + to_string(base1) + ") diventa " + to_string(base2base(num, base1, base2)) + " in base " + to_string(base2) << endl;
    return 0;
}

