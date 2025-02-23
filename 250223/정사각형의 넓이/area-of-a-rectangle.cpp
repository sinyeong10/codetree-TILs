#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n, answer;
    cin >> n;
    answer = n * n;
    cout << answer << endl; //answer 변수 없어도 되었을 듯!
    if (n < 5)
        cout << "tiny" << endl;
    return 0;
}