#include <iostream>

using namespace std;

class Complex{
    double imagine;
    double real;
public:
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
        if(imagine>=0){
            cout<<real<<" + "<<imagine<<"i"<<endl;
        }

        else {
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
    Complex c1,c2,c3;
    c1.setAll(6,4);
    c2.setAll(3,2);

    cout<<"----------------add and substract member function-----------------\n";
    c3=c1.add(c2);

    cout<<"Add= ";
    c3.printf();

    c3=c1.substract(c2);
    cout<<"Substract= ";
    c3.printf();

    cout<<"----------------add and substract StandAlone function-----------------\n";
    c1.setAll(6,4);
    c2.setAll(3,2);
    c3=add(c1,c2);

    cout<<"Add= ";
    c3.printf();

    c3=substract(c1,c2);
    cout<<"Substract= ";
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
