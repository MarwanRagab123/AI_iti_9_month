#include <iostream>

using namespace std;

class Stack{
    int* arr;
    int size;
    int tos;

public:
    Stack(int size){
        this->size=size;
        tos=-1;
        arr=new int[size];
    }
    ~Stack(){
        cout<<"\n object destruction\n";
        delete[] arr;
    }

    int push(int num){
        if(tos<size-1){
            tos++;
            arr[tos]=num;

            return 1;
        }else{
            cout<<"Stack is Full \n";
            return 0;

        }
    }
    int pop(int& num){
        if(tos>-1){
            num=arr[tos];
            tos--;

            return 1;
        }else{
            cout<<"\nStack is Empty \n";
            return 0;

        }
    }
};
void myfun(Stack& s){
    int x=0;
    while(s.pop(x)==1){
        cout<<x<<endl;
    }

}

int main()
{
    Stack s(4);
    int x;
    s.push(10);
    s.push(20);
    s.push(30);
    s.push(50);
    s.push(50);
    s.push(100);

    myfun(s);
    //s.push(20);
    //s.push(30);
}
