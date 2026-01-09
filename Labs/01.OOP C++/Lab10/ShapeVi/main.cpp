#include <iostream>
using namespace std;

class shape {
protected:
    float dim1;
    float dim2;

public:
    shape(){dim1=0;dim2=0;}
    shape(float _dim1){dim1=_dim1;dim2=_dim1;}
    shape(float _dim1,float _dim2){dim1=_dim1;dim2=_dim2;}

    void setd1(float _dim1){ dim1=_dim1; }
    void setd2(float _dim2){ dim2=_dim2; }

    void setall(float _d1,float _d2){
        dim1=_d1;
        dim2=_d2;
    }

    void print(){
        cout << "dim1: " << dim1 << ", dim2: " << dim2 << endl;
    }

    virtual float calcarea() = 0;  // pure virtual
    virtual ~shape() {}
};

// Rectangle
class Rectangle : public shape {
public:
    Rectangle(float _dim1=1,float _dim2=1):shape(_dim1,_dim2){}
    float calcarea() {
        return dim1*dim2;
    }
};

// Square
class square : public Rectangle {
public:
    square(int _dim1):Rectangle(_dim1,_dim1){}

    void setdim1(float _dim1){
        dim1=_dim1; dim2=_dim1;
    }
    void setdim2(float _dim2){
        dim1=_dim2; dim2=_dim2;
    }

    float calcarea()  {
        return dim1*dim2;
    }
};

// Circle
class circle : public shape {
public:
    circle(int _dim1):shape(_dim1,_dim1){}

    void setdim1(float _dim1){
        dim1=_dim1; dim2=_dim1;
    }
    void setdim2(float _dim2){
        dim1=_dim2; dim2=_dim2;
    }

    float calcarea()  {
        return 3.14f*dim1*dim1;
    }

    void printr(){
        cout<<"radius: "<<dim1<<endl;
    }
};

class Triangle : public shape {
public:
    Triangle(float _dim1,float _dim2):shape(_dim1,_dim2){}
    float calcarea() override {
        return 0.5f*dim1*dim2;
    }
};

float myfun(shape* s[]){

    float sum=0;
    for(int i=0 ; i<4;i++){
        sum+=s[i]->calcarea();
    }
    return sum;
}

// ================== MAIN ==================
int main() {
    shape* h=new square(5);
    h->calcarea();
    h->print();

    shape* t[4];

    t[0]=new Rectangle(5,4);
    t[1]=new square(2);
    t[2]=new circle(4);
    t[3]=new Triangle(4,6);

    float sum=myfun(t);

    cout << "\nTotal area of all shapes: " << sum << endl;

   delete[] t;

    return 0;
}
