#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string str;
    getline(cin, str);
    int N, cnt = 0;
    cin >> N;
    for (int i=str.length()-1;i>=0;i--){
        if (N <= cnt){ //==이면 멈추지만, 혹시나 넘어갈 예외 상황 반영
            break;
        }
        cout << str[i];
        cnt++;
    }
    return 0;
}