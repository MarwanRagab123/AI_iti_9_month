#include <iostream>

using namespace std;

int main()
{
    char ch;
    cout<<" Enter char :"<<endl;
    cin>>ch;
    int a =ch;

    if (a>='a' && a<='z'){
        a=a-32;
    }

    cout<<"char Capital is :" <<char(a);
}
