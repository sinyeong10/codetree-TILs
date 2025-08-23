#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;
    cin.ignore();

    string strs[N];
    for (int i=0;i<N;i++){
        getline(cin, strs[i]);
    }

    char word;
    cin >> word;

    int cnt = 0, total_cnt = 0;
    for (int i=0;i<N;i++){
        if (strs[i][0] == word){            
            cnt += 1;
            total_cnt += strs[i].length();
        }
    }

    double lengthMean = total_cnt/(double)cnt;
    cout << fixed;
    cout.precision(2);
    cout << cnt <<" "<< lengthMean;

    return 0;
}