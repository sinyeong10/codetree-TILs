#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    string str;
    getline(cin, str);
    char word;
    cin >> word;
    int count=0;
    for (int i=0;i<str.length();i++){
        if (str[i]==word){
            count++;
        }
    }
    cout << count;
    return 0;
}