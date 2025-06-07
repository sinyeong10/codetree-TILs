#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int midScore, finalScore;
    cin >> midScore >> finalScore;
    if (midScore >= 90 && finalScore >= 95){
        cout << 100000;
    } else if (midScore >= 90 && finalScore >= 90){
        cout << 50000;
    } else {
        cout << 0;
    }
    return 0;
}