int a = 56;
int * p = &a;






struct vec2 {
    float x;
    float y;

    vec2(flot x, float y) {
        this->x = x;
        this->y = y;
    }

    void add(other) {
        this->x += other->x;
        this->y = other->y;
    }
}

vec2 v;

vec2 * a = new vec2(23, 45); // pointer 8bytes

vec2 * v2 = &v;

v2->x = 12;

*(v2).x = 23;

