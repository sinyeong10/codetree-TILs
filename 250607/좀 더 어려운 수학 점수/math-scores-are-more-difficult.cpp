#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int mathScoreA, enScoreA, mathScoreB, enScoreB;
    cin >> mathScoreA >> enScoreA >> mathScoreB >> enScoreB;
    if (mathScoreA > mathScoreB){
        cout << "A";
    } else if (mathScoreB > mathScoreA){
        cout << "B";
    } else {
        if (enScoreA > enScoreB){
            cout << "A";
        } else if (enScoreB > enScoreA){
            cout << "B";
        }
    }
    return 0;
}