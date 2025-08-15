#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a, b;
    int arr[10];
    cin >> arr[0] >> arr[1];
    for (int i=2;i<10;i++){
        arr[i] = (arr[i-2]+arr[i-1])%10;
    }

    for (int i=0;i<10;i++){
        cout << arr[i] << " ";
    }

    return 0;
}