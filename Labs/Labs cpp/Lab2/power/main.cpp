#include <iostream>

using namespace std;

int main()
{
    int num;
    int pow;
    cout<<"Please Enter num: \n";
    cin>>num;
    cout<<"Please Enter power: \n";
    cin>>pow;
    int tot = 1;

    for(int i=1 ;i<=pow;i++){
        tot*=num;//
    }
    cout<<"Number of Power = "<<tot<<endl;
} //5*5
