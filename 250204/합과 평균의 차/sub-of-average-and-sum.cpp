#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c, total, mean;
    cin >> a >> b >> c;
    total = a+b+c;
    mean = total / 3;
    cout << total << endl << mean << endl << total-mean;
    return 0;
}