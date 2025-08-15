#include <iostream>
using namespace std;

int main() {
    char A[10];
    for (int i=0;i<sizeof(A)/sizeof(char);i++){
        cin >> A[i];
    }

    for (int i=sizeof(A)/sizeof(char)-1;i>=0;i--){
        cout << A[i];
    }
    // Please write your code here.
    return 0;
}