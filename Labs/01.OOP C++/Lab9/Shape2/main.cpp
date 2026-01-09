#include <iostream>

using namespace std;

class shape{
protected:
    float dim1;
    float dim2;

public:
    shape(){dim1=0;dim2=0;}
    shape(float _dim1){dim1= _dim1;}
    shape(float _dim1,float _dim2){
        dim1=_dim1;
        dim2=_dim2;
    }

    void setd1(float _dim1){
        dim1=_dim1;
    }
    void setd2(float _dim2){
        dim2=_dim2;
    }
    void setall(float _d1,float _d2){
        dim1=_d1;
        dim2=_d2;
        }
        void print(){
            cout<<"dim1: "<<dim1<<", dim2: "<<dim2<<endl;
        }
};

class Rectangle:public shape{

public:
    Rectangle(float _dim1,float _dim2):shape(_dim1,_dim2){
    }
    float computearea(){
        return dim1*dim2;
    }

};

class circle:public shape{
public:
    circle(int _dim1):shape(_dim1){}

    float ComputeArea(){
        return 3.14*dim1*dim1;
    }

    void printr(){
        cout<<"raduis: "<<dim1<<endl;

    }


};

class Triangle:public shape{

public:
    Triangle(float _dim1,float _dim2):shape(_dim1,_dim2){
    }
    float computearea(){
        return 0.5*dim1*dim2;
    }

};

// =============== TEST MAIN =====================
int main() {
    cout << "==== Shape Area Calculator ====\n\n";

    // Rectangle
    Rectangle r(10, 20);
    cout << "Rectangle:\n";
    r.print();
    cout << "Area = " << r.computearea() << "\n\n";

    // Cicle
    circle c(7);
    cout << "Circle:\n";
    c.printr();
    cout << "Area = " << c.ComputeArea() << "\n\n";

    // Triangle
    Triangle t(8, 12);
    cout << "Triangle:\n";
    t.print();
    cout << "Area = " << t.computearea() << "\n\n";

    // Updateing Using setall()
    cout << "Updating rectangle dimensions...\n";
    r.setall(5, 15);
    r.print();
    cout << "New Rectangle Area = " << r.computearea() << endl;

    cout << "\n==== Program Finished ====\n";

    return 0;
}
