#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int temperature;
    cin >> temperature;
    if (temperature < 0){
        cout << "ice";
    } else if (temperature >= 100){
        cout << "vapor";
    } else {
        cout << "water";
    }
    return 0;
}