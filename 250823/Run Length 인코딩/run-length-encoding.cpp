#include <iostream>
#include <string>

using namespace std;

string A;

int main() {
    cin >> A;
    string B="";
    char word = A[0];
    int cnt = 1;
    for (int i=1;i<A.length();i++){
        if (A[i] != word){
            B+=word;
            B+=to_string(cnt);
            cnt = 1;
            word = A[i];
        } else {
            cnt += 1;
        }
    }
    B+=word;
    B+=to_string(cnt);
    cout << B.length() << "\n" << B;
    return 0;
}
