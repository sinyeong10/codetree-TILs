#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    if (N >= 3000){
        cout << "book";
    } else if (N >= 1000){
        cout << "mask";
    } else {
        cout << "no";
    }
    return 0;
}