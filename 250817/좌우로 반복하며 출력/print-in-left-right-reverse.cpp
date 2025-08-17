#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    for (int i=0;i<N;i++){
        for (int j=1;j<=N;j++){
            if (i%2==0){
                cout << j;
            } else {
                cout << N+1-j;
            }
        }
        cout << "\n";
    }
    return 0;
}