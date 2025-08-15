#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int cnt_3=0, cnt_5=0, arr[10];
    for (int i=0;i<10;i++){
        cin >> arr[i];
    }
    for (int i=0;i<10;i++){
        if (arr[i]%3==0){
            cnt_3+=1;
        }
        if (arr[i]%5==0){
            cnt_5+=1;
        }
    }
    cout << cnt_3 << ' ' << cnt_5;
    return 0;
}