#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int arr_2d[N][N];
    for (int j=0;j<N;j++){
        for (int i=0;i<N;i++){
            if (j%2==0){
                arr_2d[i][j]=i+1;
            } else {
                arr_2d[i][j]=N-i;
            }
        }
    }
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            cout << arr_2d[i][j];
        }
        cout << endl;
    }
    return 0;
}