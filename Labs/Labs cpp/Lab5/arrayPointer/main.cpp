#include <iostream>

using namespace std;

int main()
{
    int arr[5];
    int* ptr=arr; //arr

    for(int i =0;i<5;i++){

        cout<<"Enter The value In Array value "<<(i+1)<<" : ";
        cin>>ptr[i];
    }


    for(int i =0 ;i<5;i++){

        cout<<"Address of Element "<<(i+1)<<" : "<<&arr[i]<<endl;

    }

    cout<<"Access To Element by pointer \n";



        for(int i =0 ;i<5;i++){

        cout<<"Address of Element "<<(i+1)<<" : "<<*(ptr+i)<<endl;

    }
     cout<<"Access To Element by pointer \n";

        for(int i =0 ;i<5;i++){

        cout<<"Address of Element "<<(i+1)<<" : "<<ptr[i]<<endl;

    }


}
