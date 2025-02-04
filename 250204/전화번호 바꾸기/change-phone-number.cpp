#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int tmp, x, y;
    cin >> tmp;
    cin.get();
    cin >> x;
    cin.get();
    cin >> y;
    //c++에서는 숫자가 0으로 시작하면 8진수로 인식됨!
    // cout << 010 << "-" << y << "-" << x;
    cout << "010-" << y << "-" << x;
    return 0;
}