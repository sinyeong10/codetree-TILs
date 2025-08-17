#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N, M;
    cin >> N >> M;
    int arr1_2d[N][M], arr2_2d[N][M], arr3_2d[N][M]={}; //={0}, ={0,}로 모두 0으로 초기화 불가능??
    for (int i=0;i<N;i++){
        for (int j=0;j<M;j++){
            cin >> arr1_2d[i][j];
        }
    }
    for (int i=0;i<N;i++){
        for (int j=0;j<M;j++){
            cin >> arr2_2d[i][j];
        }
    }
    for (int i=0;i<N;i++){
        for (int j=0;j<M;j++){
            if (arr1_2d[i][j] != arr2_2d[i][j]){
                arr3_2d[i][j] = 1;
            }//  else {
            //     arr3_2d[i][j] = 0;
            // }
        }
    }
    for (int i=0;i<N;i++){
        for (int j=0;j<M;j++){
            cout << arr3_2d[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}