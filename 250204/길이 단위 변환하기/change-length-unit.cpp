#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    double ft_trans_cm = 30.48, mi_trans_cm = 160934;
    double a = 9.2, b = 1.3;
    cout << fixed;
    cout.precision(1);
    cout << a << "ft = " << a*ft_trans_cm << "cm" << endl;
    cout << b << "mi = " << b*mi_trans_cm << "cm" << endl; 
    return 0;
}