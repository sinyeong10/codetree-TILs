#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, tmp;
    cin >> a >> b;
    tmp = a;
    a = b;
    b = tmp;
    cout << a << " " << b;
    return 0;
}