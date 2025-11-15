#include <iostream>
using namespace std;

// ANSI Colors
#define RESET   "\033[0m"
#define GREEN   "\033[32m"
#define RED     "\033[31m"
#define YELLOW  "\033[33m"
#define CYAN    "\033[36m"

// ================= Point =================
class Point {
    int x;
    int y;
public:
    Point() {
        x = 0; y = 0;
        cout << GREEN << "[Point] Paramless Constructor\n" << RESET;
    }
    Point(int _x) {
        x = _x; y = 0;
        cout << GREEN << "[Point] One param Constructor\n" << RESET;
    }
    Point(int _x, int _y) {
        x = _x; y = _y;
        cout << GREEN << "[Point] Two param Constructor\n" << RESET;
    }
    void setpoint(int _x, int _y) { x = _x; y = _y; }
    void print() { cout << "(" << x << "," << y << ")\n"; }
    ~Point() { cout << RED << "[Point] Destructor\n" << RESET; }
};

// ================= Rectangle (Composition) =================
class Rectangle {
    Point ul;
    Point lr;
public:
    Rectangle(int x1, int y1, int x2, int y2) : ul(x1, y1), lr(x2, y2) {
        cout << CYAN << "[Rectangle Composition] Constructor\n" << RESET;
    }
    ~Rectangle() { cout << RED << "[Rectangle Composition] Destructor\n" << RESET; }
    void print() { ul.print(); lr.print(); }
};

// ================= Triangle (Composition) =================
class Triangle {
    Point r1, r2, r3;
public:
    Triangle(int x1, int y1, int x2, int y2, int x3, int y3)
        : r1(x1, y1), r2(x2, y2), r3(x3, y3) {
        cout << CYAN << "[Triangle Composition] Constructor\n" << RESET;
    }
    ~Triangle() { cout << RED << "[Triangle Composition] Destructor\n" << RESET; }
    void print() { r1.print(); r2.print(); r3.print(); }
};

// ================= Circle (Composition) =================
class circle {
    Point r;
    double raduis;
public:
    circle(int x1, int y1, double r) : r(x1, y1), raduis(r) {
        cout << CYAN << "[Circle Composition] Constructor\n" << RESET;
    }
    ~circle() { cout << RED << "[Circle Composition] Destructor\n" << RESET; }
    void print() {
        cout << "Center: "; r.print();
        cout << "Radius: " << raduis << "\nArea: " << 3.14 * raduis * raduis << "\n";
    }
};

// ================= Rectangle (Aggregation) =================
class Rect {
    Point* ul;
    Point* lr;
public:
    Rect() { cout << YELLOW << "[Rectangle Aggregation] Constructor\n" << RESET; }
    ~Rect() { cout << RED << "[Rectangle Aggregation] Destructor\n" << RESET; }
    void setpontall(Point* _ul, Point* _lr) { ul = _ul; lr = _lr; }
    void print() { ul->print(); lr->print(); }
};

// ================= Triangle (Aggregation) =================
class Tre {
    Point* r1; Point* r2; Point* r3;
public:
    Tre() { cout << YELLOW << "[Triangle Aggregation] Constructor\n" << RESET; }
    ~Tre() { cout << RED << "[Triangle Aggregation] Destructor\n" << RESET; }
    void setpointrall(Point* _r1, Point* _r2, Point* _r3) {
        r1 = _r1; r2 = _r2; r3 = _r3;
    }
    void print() { r1->print(); r2->print(); r3->print(); }
};

// ================= Circle (Aggregation) =================
class cr {
    Point* r;
    double rad;
public:
    cr() { cout << YELLOW << "[Circle Aggregation] Constructor\n" << RESET; }
    ~cr() { cout << RED << "[Circle Aggregation] Destructor\n" << RESET; }
    void setall(Point* _r, double _rad) { r = _r; rad = _rad; }
    void print() {
        cout << "Center: "; r->print();
        cout << "Radius: " << rad << "\n";
    }
};

// ================= MAIN =================
int main() {
    cout << "\n=== [1] Testing Point Class ===\n";
    Point p1(2, 3);
    Point p2(5, 7);

    cout << "\n=== [2] Rectangle (Composition) ===\n";
    Rectangle rect(1, 2, 4, 5);
    rect.print();

    cout << "\n=== [3] Triangle (Composition) ===\n";
    Triangle tri(0, 0, 5, 0, 3, 4);
    tri.print();

    cout << "\n=== [4] Circle (Composition) ===\n";
    circle c1(10, 10, 5.5);
    c1.print();

    cout << "\n=== [5] Rectangle (Aggregation) ===\n";
    Rect ragg;
    ragg.setpontall(&p1, &p2);
    ragg.print();

    cout << "\n=== [6] Triangle (Aggregation) ===\n";
    Point a(1, 1), b(2, 3), c(4, 6);
    Tre t;
    t.setpointrall(&a, &b, &c);
    t.print();

    cout << "\n=== [7] Circle (Aggregation) ===\n";
    Point center(7, 8);
    cr c2;
    c2.setall(&center, 9.5);
    c2.print();

    cout << "\n=== END OF TESTS ===\n";
    return 0;
}
