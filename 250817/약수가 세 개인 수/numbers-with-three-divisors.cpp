#include <iostream>

using namespace std;

int st, ed;

int main() {
    cin >> st >> ed;
    int ans = 0;
    // Please write your code here.
    for (int i=st;i<=ed;i++){
        int total = 0;
        for (int j=1;j<=i;j++){
            if (i%j==0){
                total += 1;
            }
        }
        if (total == 3){
            ans += 1;
        }
    }
    cout << ans;

    return 0;
}
