#include <iostream>

using namespace std;
class parent{

    int x,y;
public:
    parent(int _x,int _y){
        x=_x;
        y=_y;
    }

    virtual int add(){
        return x+y;
    }
};
class child:public parent{

    int z;


public:
    child(int _x,int _y, int _z):parent(_x,_y){z=_z;}

    int add(){
        return parent::add()+z;
    }
};
int main()
{
    parent* p1;
   child c1(1,2,9);

   p1=&c1;
   cout<<p1->add();
}
