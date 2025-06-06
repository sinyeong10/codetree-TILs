#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    if (N >= 80){
        cout << "pass";
    } else {
        cout << 80-N << " more score";
    }

    return 0;
}