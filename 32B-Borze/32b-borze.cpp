#include <iostream>
 
using namespace std;
 
int main(){
    string s;
    string res;
    cin >> s;
    for(int i = 0; i < s.length(); i++){
        if(s[i] == '.')
            res += "0";
        else if(s[i] == '-' && s[i+1] == '.'){
            res += "1";
            i++;
        }
        else if(s[i] == '-' && s[i+1] == '-'){
            res += "2";
            i++;
        }
    }
    cout << res;
}
