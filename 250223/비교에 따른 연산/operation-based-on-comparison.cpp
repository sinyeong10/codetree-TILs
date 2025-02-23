#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b;
    cin >> a >> b;
    if (a > b) cout << a*b << endl;
    else cout << b / a << endl; //정수의 나누기로 몫 계산
    return 0;
}