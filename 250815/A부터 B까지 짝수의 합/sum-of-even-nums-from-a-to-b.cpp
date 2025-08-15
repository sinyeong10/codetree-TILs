#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B, total=0;
    cin >> A >> B;
    for (int i=A;i<=B;i++){
        if (i%2==0){
            total += i;
        }
    }
    cout << total;
    return 0;
}