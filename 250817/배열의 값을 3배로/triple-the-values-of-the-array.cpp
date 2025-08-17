#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr_2d[3][3] = {0};
    for (int i=0;i<3;i++){
        for (int j=0;j<3;j++){
            cin >> arr_2d[i][j];
        }
    }
    for (int i=0;i<3;i++){
        for (int j=0;j<3;j++){
            arr_2d[i][j]*=3;
        }
    }
    for (int i=0;i<3;i++){
        for (int j=0;j<3;j++){
            cout << arr_2d[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}