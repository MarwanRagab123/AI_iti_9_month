#include <iostream>
#include <windows.h>
#include <conio.h>
#define null -32
using namespace std;


void gotoxy( int column, int line )
  {
  COORD coord;
  coord.X = column;
  coord.Y = line;
  SetConsoleCursorPosition(
    GetStdHandle( STD_OUTPUT_HANDLE ),
    coord
    );
  }


void textattr(int i)
{
	SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), i);

}

int main()
{
    char menu[3][8]={"new","display","exist"};
    int hintx=0;
    char ch;
    do{
    for(int i=0;i<3;i++){
        gotoxy(10,7+i);
        if(i==hintx)
            textattr(0x04);
        else
            textattr(0x07);

        cout<<menu[i];


    }
    ch=getch();

    switch(ch){
    case - 32:
        ch=getch();
        switch(ch){
        case 72:
            hintx--;
            if(hintx<0){
                hintx=2;
            }
            break;
        case 80:
            hintx++;
            if(hintx>2){
                hintx=0;
            }
            break;
        }
        case 13:
            break;
        case 27:
            break;
    }
    }while(ch!=27);



}

