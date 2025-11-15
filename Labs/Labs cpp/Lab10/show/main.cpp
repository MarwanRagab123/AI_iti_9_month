#include <iostream>
#define size 10
using namespace std;

int main()
{
    int arr[size];
    for(int i=0;i<size;i++){
        cin>>arr[i];
    }
    for(int i=0;i<size-1;i++){
        bool swap=false;

        for(int j=0;j<size-1;j++){
            if(arr[j]>arr[j+1]){
                int temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
                swapped=true;
            }

        }
        if(!swapped){
            break;
        }
    }
    for(int)


}
