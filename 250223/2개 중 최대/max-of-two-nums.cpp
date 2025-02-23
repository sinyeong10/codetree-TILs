#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b;
    cin >> a >> b;
    cout << (a > b ? a : b) << endl; //<< 연산자는 >보다 우선순위가 높음에 주의!

    return 0;
}