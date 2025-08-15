#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string A;
    cin >> A;
    A[1] = 'a';
    //인덱스는 0~A.length()-1까지 길이는 A.length(), 따라서 뒤에서 2번째는 -2가 맞음
    A[A.length()-2] = 'a';
    cout << A;
    return 0;
}