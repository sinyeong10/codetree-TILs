#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;
    while (A <= B){
        cout << A << " ";
        if (A%2==0){
            A+=3;
        } else {
            A*=2;
        }
    }
    return 0;
}