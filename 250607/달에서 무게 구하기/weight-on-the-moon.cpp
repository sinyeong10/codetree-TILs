#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int mass = 13;
    float gravityRatio = 0.165;
    cout << fixed;
    cout.precision(6);
    cout << mass << " * " << gravityRatio << " = " << mass*gravityRatio;
    return 0;
}