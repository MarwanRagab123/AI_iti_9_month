#include <iostream>
#define size 5

using namespace std;

int main()
{
    int arr[size];
    for(int i=0;i<size;i++){
        cout<<"Enter Number" <<(i+1) <<":";
        cin>>arr[i];
    }
    cout<<"Print Data In Array \n";
    for(int i=0;i<size;i++){
        cout<<arr[i]<<endl;
    }

     cout<<"********************* \n";

    int sum=0;
    cout<<"Sum Array\n";
    for(int i=0;i<size;i++){
        sum+=arr[i];
    }
    cout<<"Sum Number in Array: "<<sum<<endl;

    cout<<"********************* \n";

    int maxim=arr[0]; //10 11 12
    for(int i=1;i<size;i++){
        if(maxim<arr[i]){
            maxim=arr[i];
        }
    }
    cout<<"Max Number in Array: "<<maxim<<endl;

    cout<<"********************* \n";

    int minim=arr[0]; //10 11 12
    for(int i=1;i<size;i++){
        if(minim>arr[i]){
            maxim=arr[i];
        }
    }
    cout<<"Min Number in Array: "<<minim<<endl;


    cout<<"Enter Number to you search: ";
    int sr;
    cin>>sr;
    for(int i=1;i<size;i++){
        if(sr==arr[i]){
            cout<<"The Position of The Number = "<<sr<<endl;

            break;
        }

    }



}
