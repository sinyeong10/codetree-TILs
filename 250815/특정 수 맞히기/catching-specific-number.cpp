#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    while (N != 25){
        if (N < 25){
            cout << "Higher\n";
        } else if (N > 25){
            cout << "Lower\n";
        }
        cin >> N;
    }
    cout << "Good";
    return 0;
}