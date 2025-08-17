#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    for (int i=0;i<4;i++){
        int num, total = 0;
        for (int j=0;j<4;j++){
            cin >> num;
            total += num;
        }
        cout << total << "\n";
    }
    return 0;
}