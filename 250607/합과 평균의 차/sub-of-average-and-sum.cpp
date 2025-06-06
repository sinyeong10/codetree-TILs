#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c, total, average;
    cin >> a >> b >> c;
    total = a+b+c;
    average = total / 3;
    cout << total << endl << average << endl << total-average;
    return 0;
}