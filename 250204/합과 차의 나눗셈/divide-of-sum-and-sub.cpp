#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b;
    cin >> a >> b;
    cout << fixed;
    cout.precision(2);
    cout << (a+b) / (a-b);
    return 0;
}