#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A_math, A_eng, B_math, B_eng;
    cin >> A_math >> A_eng;
    cin >> B_math >> B_eng;
    if (A_math > B_math && A_eng > B_eng){
        cout << 1;
    } else {
        cout << 0;
    }
    return 0;
}