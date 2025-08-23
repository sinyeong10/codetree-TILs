#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string str;
    getline(cin, str);
    for (int i=2;i<10;i++){
        cout << str[i];
    }
    return 0;
}