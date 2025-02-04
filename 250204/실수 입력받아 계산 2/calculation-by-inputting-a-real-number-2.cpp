#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    float a;
    cin >> a;
    // cout.precision(2); #이렇게 먼저해도 되지만 의미가 유효숫자 설정이라서 아래처럼 하는 게 좀 더 명시적임
    cout << fixed
    cout.precision(2);
    cout << a+1.5;
    return 0;
}