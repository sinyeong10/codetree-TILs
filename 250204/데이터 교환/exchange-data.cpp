#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a = 5, b = 6, c = 7, tmp;
    //c<b<a<c
    tmp = a;
    a = c;
    c = b;
    b = tmp;
    cout << a << endl << b << endl << c;
    return 0;
}