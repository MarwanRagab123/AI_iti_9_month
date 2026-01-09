#include <iostream>

using namespace std;

class Complex{
    double imagine;
    double real;
public:
    Complex(int _real=0,int _imagine=0){
        real=_real;
        imagine=_imagine;
    }

    void setImagine(double _imagine){
        imagine=_imagine;
    }

    void setReal(double _real){
        real=_real;
    }

    void setAll(double _real,double _imagine){
        real=_real;
        imagine=_imagine;

    }

    double getReal(){
        return real;
    }

    double getImagine(){
        return imagine;
    }

    void printf(){
        if(imagine>0){
            cout<<real<<" + "<<imagine<<"i"<<endl;
        }

        else if(imagine==0) {

                cout<<real<<endl;

        }else{
            cout<<real<<" - "<<-1*imagine<<"i"<<endl;
        }

    }

    Complex add(Complex c){

        Complex res;
        res.real=real+c.real;
        res.imagine=imagine+c.imagine;
        return res;

    }

    Complex substract(Complex c){

        Complex res;
        res.real=real-c.real;
        res.imagine=imagine-c.imagine;
        return res;

    }

};
Complex add(Complex c1,Complex c2);
Complex substract(Complex c1,Complex c2);

int main()
{
cout<<"test 1\n";
Complex c1;
c1.printf();

cout<<"test 2\n";

Complex c2(5);
c2.printf();

cout<<"test 3\n";

Complex c3(5,2);
c3.printf();


}
//standalone function
Complex add(Complex c1,Complex c2){
    Complex res;
    res.setReal(c1.getReal()+c2.getReal());
    res.setImagine(c1.getImagine()+c2.getImagine());
    return res;
}

Complex substract(Complex c1,Complex c2){
    Complex res;
    res.setReal(c1.getReal()-c2.getReal());
    res.setImagine(c1.getImagine()-c2.getImagine());
    return res;
}
