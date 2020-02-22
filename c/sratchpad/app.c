/* a scratchpad playground to write some c code and talk about concepts */

/* Variables and Data types in C */
// int 32 bit whole numbers
// short 16 bit whole number
// char 8 bit whole number
// float 32 bit decimal based number
// double 64 bit decimal based number

// type label [= value];
long long l = 2; // 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000010 
int num = 2; // 00000000 00000000 00000000 00000010
short s = 2; //     00000000 00000010
char c = 2; // 00000010
s = 34;
num = 56;

float f = 12.5f;
double d = 12.5;





/* Operators in C */
s = s + 2;
// +, -, /, *
// <, >, ==

/* Conditionals in C */

if (s == 2) {
 s = 3;
} else if (s == 34) {

} else {

}

/* Looping in C */
for (int i = 0; i < 10; i++) {

}

while(s < 12) {
    s++;
}

/* Functions in C */
// return type label (arguments) { }
int add(int a, int b) {
    return a + b;
}

void dosomething(int mything) {
    // do nothing
    mything++;
}

/* Structures in C */

struct point {
    float x;
    float y;
} Point;

Point p;
p.x = 12;
p.y = 12;

Point add_point(Point a, Point b) {
    Point c;
    c.x = a.x + b.x;
    c.y = a.y + b.y;
    return c;
}

Point p2 = add_point(p, p);
p2.x // => 24

