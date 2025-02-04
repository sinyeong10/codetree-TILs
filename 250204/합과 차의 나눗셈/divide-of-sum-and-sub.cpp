#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b;
    cin >> a >> b;
    cout << fixed;
    cout.precision(2);
    //다 int라서 실수연산을 위해 형변환이 필요!
    cout << (double)(a+b) / (a-b);
    return 0;
}