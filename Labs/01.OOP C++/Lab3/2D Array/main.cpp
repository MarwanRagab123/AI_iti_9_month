#include <iostream>
#define rows 3
#define cols 4
using namespace std;

int main()
{
    int arr[rows][cols];
    for(int i=0;i<rows;i++){
            cout<<"Enter Grade "<< i+1<< " Student: "<<endl;
        for(int j=0;j<cols;j++){
            cin>>arr[i][j];
        }
    }

    for(int i=0;i<rows;i++){
            cout<<"Grade the "<<i+1<<" Student: "<<endl;
        for(int j=0;j<cols;j++){
            cout<<arr[i][j]<<"\t";
        }
        cout<<endl;
    }
    int sum[rows]={0}; //{0,0,0,0}

        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                sum[i]+=arr[i][j];
            }
            cout<<"Sum rows "<<i+1<<" = "<<sum[i]<<endl;

    }

    int t[cols]={0}; //{0,0,0,0}

        for(int i=0;i<cols;i++){
            for(int j=0;j<rows;j++){
                t[i]+=arr[j][i];
            }

            cout<<"Sum average of column "<<i+1<<" = "<<t[i]/rows<<endl;

    }
}
