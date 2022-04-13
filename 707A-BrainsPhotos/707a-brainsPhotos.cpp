#include <iostream>
 
using namespace std;
 
string fun(){
    int i1, i2;
    cin >> i1 >> i2;
    string sample;
    for(int i = 0; i < i1; ++i){
        for(int j = 0; j < i2; ++j){
            cin >> sample;
            if(sample == "C" || sample == "M" || sample == "Y")
                return "#Color"; 
        }
    }
    return "#Black&White";
}
 
int main(){
    cout << fun();
    return 0;
}
