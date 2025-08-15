#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int cnt = 0;
    string arr[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    char word;
    cin >> word;
    for (int i=0;i<5;i++){
        if (arr[i][2]==word || arr[i][3]==word){
            cout << arr[i]<<"\n";
            cnt+=1;
        }
    }
    cout << cnt;
    return 0;
}