#include <iostream>

using namespace std;

int fibR(int n){
    if(n==1){
        return 1;
    }
    if(n==0){
        return 0;
    }

    return fibR(n-1)+fibR(n-2);

}

int main()
{
    int x;
    cout<<"Enter Number you need compute fib:";
    cin>>x;

    for(int i=0 ;i<x;i++){
        cout<<fibR(i)<<" ";
    }
    cout<<endl;
}
