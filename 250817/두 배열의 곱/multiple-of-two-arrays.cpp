#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr1_2d[3][3], arr2_2d[3][3];
    for (int i=0;i<3;i++){
        for (int j=0;j<3;j++){
            cin >> arr1_2d[i][j];
        }
    }
    for (int i=0;i<3;i++){
        for (int j=0;j<3;j++){
            cin >> arr2_2d[i][j];
        }
    }
    for (int i=0;i<3;i++){
        for (int j=0;j<3;j++){
            cout << arr1_2d[i][j] * arr2_2d[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}