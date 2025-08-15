#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    for (;N<=100;N++){
        if (N >= 90){
            cout << "A" << " ";
        } else if (N >= 80){
            cout << "B" << " ";
        } else if (N >= 70){
            cout << "C" << " ";
        } else if (N >= 60){
            cout << "D" << " ";
        } else{
            cout << "F" << " ";
        }
    }
    return 0;
}