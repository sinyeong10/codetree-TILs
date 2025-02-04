#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b, c;
    cin >> a >> b >> c;
    // int d;
    // d = (double)(a+b+c)/3; 근데 굳이 실수 연산 후 정수로 처리하지 않아도 됨!
    cout << a+b+c << endl << (a+b+c)/3;
    return 0;
}