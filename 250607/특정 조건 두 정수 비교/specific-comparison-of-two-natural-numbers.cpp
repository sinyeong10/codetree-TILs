#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;
    if (A < B){
        cout << 1;
    } else {
        cout << 0;
    }
    cout << " ";
    if (A == B){
        cout << 1;
    } else {
        cout << 0;
    }
    return 0;
}