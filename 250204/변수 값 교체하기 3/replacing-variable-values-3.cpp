#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a = 3, b = 5, tmp;
    tmp = a;
    a = b;
    b = tmp;
    cout << a << endl << b;
    return 0;
}