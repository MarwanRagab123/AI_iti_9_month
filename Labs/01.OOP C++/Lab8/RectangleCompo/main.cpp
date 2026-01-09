#include <iostream>

using namespace std;

class Point{
    int x;
    int y;
public:
    Point(){x=0;y=0;cout<<"\nParamless Constructor\n";}
    Point(int _x){x=_x;y=0;cout<<"\n one param Constructor\n";}
    Point(int _x,int _y){x=_x;y=_y;cout<<"\n two param constructor\n";}

    void setx(int _x){
        x=_x;
    }
    void sety(int _y){
        y=_y;
    }
    void setpoint(int _x,int _y){
        x=_x;
        y=_y;
    }
    void print(){
        cout<<"("<<x<<","<<y<<")"<<endl;
    }
    ~Point(){
        cout<<"Point Destructor\n";
    }

};

// Rectangle Composition
class Rectangle{
    Point ul;
    Point lr;

public:
    Rectangle(int x1,int y1 ,int x2, int y2):ul(x1,y1),lr(x2,y2){
        //ul.setpoint(x1,y1);
        //lr.setpoint(x2,y2);

        cout<<"[Rectangle Composition] Constructor\n";
    }
    ~Rectangle(){
        cout<<"[Rectangle composition] Destructor\n";
    }
    void setpointul(int _x,int _y){
       ul.setpoint(_x,_y);
    }
    void setpointlr(int _x,int _y){
       lr.setpoint(_x,_y);
    }

    void print(){
        ul.print();
        lr.print();
    }

};
//Triangle Compositions

class Triangle{
    Point r1;
    Point r2;
    Point r3;
public:
    Triangle(int x1,int y1,int x2,int y2,int x3,int y3):r1(x1,y1),r2(x2,y2),r3(x3,y3){
        cout<<"\n [Triangle composition] created  Constructor\n";
    }

    void setr1(int _x,int _y){
        r1.setpoint(_x,_y);
    }

    void setr2(int _x,int _y){
        r2.setpoint(_x,_y);
    }
    void setr3(int _x,int _y){
        r3.setpoint(_x,_y);
    }

    ~Triangle(){
        cout<<"\n[Triangle composition] Distructor\n";
    }

    //getters

    Point getr1(){
        return r1;
    }

    Point getr2(){
        return r2;
    }
    Point getr3(){
        return r3;
    }

    void print(){
        r1.print();
        r2.print();
        r2.print();
    }


};

// Circle Composition

class circle{
    Point r;//center
    double raduis;

public:
    circle(int x1,int y1,double r):r(x1,y1),raduis(r){
        cout<<"\n [Circle Composition] Constructor Created\n";
    }
    ~circle(){
        cout<<"\n[Circle Composition] Distructor Circle\n";
    }
    void setr(int _x,int _y){
        r.setpoint(_x,_y);
    }
    void setradius(double r) {
        raduis = r;
    }
    double getarea() {
        return 3.14 * raduis * raduis;
    }
    void print() {
        cout << "Center: ";
        r.print();
        cout << "Radius: " << raduis << endl;
        cout << "Area: " << getarea() << endl;
    }
};

//Rect Aggregation
class Rect{
    Point* ul;
    Point* lr;
public:
    Rect(){
        cout<<"[Rectangle Aggregation] ctro created\n";
    }
    ~Rect(){
        cout<<"[Rectangle Aggregation] ctro disrtructor\n";
    }
    void setpointul(Point* ul){
        this->ul=ul;
    }
    void setpointlr(Point* lr){
        this->lr=lr;
    }

    void setpontall(Point* ul,Point* lr){
        this->ul=ul;
        this->lr=lr;
    }

    void print(){
        ul->print();
        lr->print();
    }

};

//Triangle Aggregation

class Tre{
    Point* r1;
    Point* r2;
    Point* r3;
public:
    Tre(){
        cout<<"[Triangle Aggregation] ctro created\n";
    }
    ~Tre(){
        cout<<"[Triangle Aggregation] ctro disrtructor\n";
    }
    void setpointr1(Point* r1){
        this->r1=r1;
    }
    void setpointr2(Point* r2){
        this->r2=r2;
    }

    void setpointr3(Point* r3){
        this->r3=r3;
    }

    void setpointrall(Point* r1, Point* r2, Point* r3){
        this->r1=r1;
        this->r2=r2;
        this->r3=r3;
    }

    void print(){
        r1->print();
        r2->print();
        r3->print();
    }
};

//Circle Aggregation

class cr{
    Point* r;
    double rad;

public:
    cr(){
        cout<<"\n [circle Aggregation] Constructor Created\n";
    }
    ~cr(){
        cout<<"\n[Circle Aggregation] Distructor Object\n";
    }

    void setr(Point* r){
        this->r=r;
    }
    void setrad(double _rad){
        rad=_rad;
    }

    void setall(Point *r,double d){
        this->r=r;
        rad=d;
    }

    void print(){
        cout << "Center: ";
        r->print();
        cout << "Radius: " << rad << endl;
    }

    };


int main() {


    cout << "\n=== [1] Testing Point Class ===\n";
    Point p1(2, 3);
    Point p2(5, 7);
    cout << "p1 = "; p1.print(); cout << "\n";
    cout << "p2 = "; p2.print(); cout << "\n";

    cout << "\n=== [2] Testing Rectangle Class (Composition) ===\n";
    Rectangle rect(1, 2, 4, 5);
    rect.print();

    cout << "\n=== [3] Testing Triangle Class (Composition) ===\n";
    Triangle tri(0, 0, 5, 0, 3, 4);
    tri.print();

    cout << "\n=== [6] Testing circle Class (Composition) ===\n";
    circle c1(10, 10, 5.5);
    c1.print();

    cout << "\n=== [4] Testing Rectangle Class (Aggregation) ===\n";
    Rect ragg;
    ragg.setpontall(&p1, &p2);
    ragg.print();

    cout << "\n=== [5] Testing Triangle Class (Aggregation Triangle) ===\n";
    Point a(1, 1), b(2, 3), c(4, 6);
    Tre t;
    t.setpointrall(&a, &b, &c);
    t.print();


    cout << "\n=== [7] Testing cr Class (Aggregation Circle) ===\n";
    Point center(7, 8);
    cr c2;
    c2.setall(&center,9.5);
    c2.print();

    cout << "\n=== END OF TESTS ===\n";
    return 0;


}


