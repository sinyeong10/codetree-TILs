#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string a, b;
    cin >> a >> b;
    int a_len=a.length(), b_len=b.length();
    if (a_len < b_len){
        cout << b << " " << b_len;
    } else if (a_len > b_len){
        cout << a << " " << a_len;
    } else {
        cout << "same";
    }
    return 0;
}