#include <iostream>

using namespace std;

class Queue{
    int* arr;
    int size;
    int head;

public:
    Queue(int size){
        this->size=size;
        head=-1;
        arr=new int[size];
    }
    ~Queue(){
        cout<<"\n object destruction\n";
        delete[] arr;
    }

    int enqueu(int num){
        if(head<size-1){
            head++;
            arr[head]=num;

            return 1;
        }else{
            cout<<"Queue is Full \n";
            return 0;

        }
    }
    int dequeue(int& num){
        if(head>-1){
            num=arr[0];
            for(int i=0;i<head;i++){

            arr[i]=arr[i+1];
            } //3  0 1 2
            head--;
            return 1;
        }else{
            cout<<"\Queue is Empty \n";
            return 0;

        }
    }
};

int main()
{
    Queue q(3);
    int x;
    q.enqueu(1);
    q.enqueu(2);
    q.enqueu(3);
    q.enqueu(4);

    if(q.dequeue(x)==1){
        cout<<x<<endl;
    }
    if(q.dequeue(x)==1){
        cout<<x<<endl;
    }
    if(q.dequeue(x)==1){
        cout<<x<<endl;
    }
    if(q.dequeue(x)==1){
        cout<<x<<endl;
    }
    if(q.dequeue(x)==1){
        cout<<x<<endl;
    }
    //cout<<q.dequeue(x)<<' '<<x<<"\n";
    //cout<<q.dequeue(x)<<' '<<x<<"\n";
    //cout<<q.dequeue(x)<<' '<<x<<"\n";
    //cout<<q.dequeue(x)<<' '<<x<<"\n";


}
