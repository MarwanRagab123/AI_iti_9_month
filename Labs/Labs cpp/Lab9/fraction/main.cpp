#include <iostream>

using namespace std;

class fraction{
    int numerator;
    int denominator;

public:
    fraction(int _numerator=0 ,int _denominator=1){
        numerator=_numerator;
        denominator=_denominator;
    }
    void setNumerator(int _numerator){
        numerator=_numerator;
    }

    void setDenominator(int _denominator){
        denominator=_denominator;
    }
    void setAll(int _numerator,int _denominator){
        numerator=_numerator;
        denominator=_denominator;
    }

    int getNumerator(){
        return numerator;
    }

    int getDenominator(){
        return denominator;
    }

    int gcd(int x,int y){
        if(x==0){
            return 0;
        }
        else{
        while(y!=0){
           int temp=y;
            y=x%y;
            x=temp;
        }
        return x;
    }
    }
    void simplify(){
        int g=gcd(numerator,denominator);

        numerator=numerator/g;
        denominator=denominator/g;

    }

    void print(){
        if (numerator==0){
            cout<<numerator<<endl;
        }
        else{cout<<numerator<<"/"<<denominator<<endl;}
    }

};

fraction addF(fraction f1,fraction f2){
    fraction res;
    int af1=f1.getNumerator();
    int bf1=f1.getDenominator();
    int af2=f2.getNumerator();
    int bf2=f2.getDenominator();
    res.setNumerator(af1*bf2+af2*bf1);
    res.setDenominator(bf1*bf2);

    return res;

}

int main()
{
    fraction f1(1, 2);
    fraction f2(3, 4);

    fraction sum=addF(f1,f2);

    sum.simplify();

    sum.print();



    fraction f3(0,10);

    f3.simplify();
    f3.print();





}
