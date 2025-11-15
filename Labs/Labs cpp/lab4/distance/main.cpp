#include <iostream>
#define size 10
using namespace std;

int main()
{
 int arr[size];
 for(int i=0;i<size;i++){
    cin>>arr[i];
 }
 int counter=0;
 int num ;
 for(int i=0;i<size;i++){
    for(int j=i+1;j<size;j++){ //1 2 3 4 5 6 7 1 7
        if(arr[i]==arr[j]){
            int n=j-i; //6
            if(n>counter){
                counter=n;
                num=arr[i];

                }
        }

    }
 }
 cout<<"num ="<<num<<" : "<<"counter= "<<counter<<endl;
}
