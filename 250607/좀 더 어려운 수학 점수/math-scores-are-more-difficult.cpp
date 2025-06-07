#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int mathScoreA, enScoreA, mathScoreB, enScoreB;
    cin >> mathScoreA >> enScoreA >> mathScoreB >> enScoreB;
    if (mathScoreA > mathScoreB || (mathScoreA == mathScoreB && enScoreA > enScoreB)){
        cout << "A";
    } else {
        cout << "B";
    }
    return 0;
}