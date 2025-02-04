#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    float ft, ft_trans_cm = 30.48;
    cin >> ft;
    cout << fixed;
    cout.precision(1);
    cout << ft*ft_trans_cm;
    return 0;
}