#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    double h, w, b;
    cin >> h >> w;
    b = 10000*w/(h*h);
    cout << int(b) << endl; //처음부터 자료형을 int로 해도 되었을 듯?
    if (b >= 25) {
        cout << "Obesity" << endl;
    }
    return 0;
}