#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    char gen_a, gen_b;
    int age_a, age_b;
    cin >> age_a >> gen_a >> age_b >> gen_b;
    if ((age_a >= 19 && gen_a == 'M') || (age_b >= 19 && gen_b == 'M')){
        cout << 1;
    } else {
        cout << 0;
    }
    return 0;
}