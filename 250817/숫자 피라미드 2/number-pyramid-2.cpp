#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N, cnt = 1;
    cin >> N;
    for (int i=1;i<=N;i++){
        for (int j=0;j<i;j++){
            cout << cnt << " ";
            cnt += 1;
        }
        cout << "\n";
    }
    return 0;
}