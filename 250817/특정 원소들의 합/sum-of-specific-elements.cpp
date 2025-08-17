#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int total=0, arr_2d[4][4];
    for (int i=0;i<4;i++){
        for (int j=0;j<4;j++){
            cin >> arr_2d[i][j];
        }
    }
    for (int i=0;i<4;i++){
        for (int j=0;j<=i;j++){
            total += arr_2d[i][j];
        }
    }
    cout << total;
    return 0;
}