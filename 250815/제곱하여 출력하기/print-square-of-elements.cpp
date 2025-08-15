#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    int A[N];
    for (int i=0; i<N; i++){
        cin >> A[i];
    }
    
    for (int i=0; i<N; i++){
        A[i] = A[i] * A[i];
    }

    for (int i=0; i<N; i++){
        cout << A[i] << " ";
    }
    return 0;
}