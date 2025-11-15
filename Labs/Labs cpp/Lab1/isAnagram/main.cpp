#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    string s1;
    string s2;

    cout<<"Enter String 1"<<endl;
    cin>>s1;
    cout<<"Enter String 2"<<endl;
    cin>>s2;
    sort(s1.begin(), s1.end());
    sort(s2.begin(), s2.end());
    if(s1==s2){
        return true;

    }else{
       return false;
    }


}
