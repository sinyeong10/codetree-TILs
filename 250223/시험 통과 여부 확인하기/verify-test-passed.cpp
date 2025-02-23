#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin >> n;
    if (n >= 80){
        cout << "pass" << endl;
    } else {
        cout << 80 - n << " more score" << endl; //cout시 python과 다르게 공백 등이 들어가지 않음에 주의!
    }
    return 0;
}