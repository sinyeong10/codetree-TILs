#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B, total;
    cin >> A >> B;
    cout << fixed;
    cout.precision(1);
    total = A+B;
    cout << total << " " << (double)total / 2;
    return 0;
}