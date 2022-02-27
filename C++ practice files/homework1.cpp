//assignment question 1  made by abhijeet a s 21BCE10074

#include <iostream>
using namespace std;

class shape
{
    void draw(){
        cout<<"draw shape";
    }
    void erase(){
        cout<<"erase shape \n";
    }
};

class circle : public shape
{
public:
    void draw(){
    cout<<"draw circle \n";
    }
    void erase(){
    cout<<"erase circle \n";
    }
};

class triangle : public shape
{
public:
    void draw(){
        cout<<"draw triangle \n";
    }
    void erase(){
        cout<<"erase triangle \n";
    }
};

class square : public shape
{
public:
    void draw(){
        cout <<"draw square \n";
    }
    void erase(){
        cout <<"erase square \n";
    }
};

int main(){
    circle c;
    c.draw();
    c.erase();
    triangle t;
    t.draw();
    t.erase();
    square s;
    s.draw();
    s.erase();
    return 0;
}