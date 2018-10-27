
class Rectangle{

private:
	int width;
	int length;
public:
	void set(int w, int l);
	int area();
	/*Rectangle(int w, int l){
		width = w;
		length = l;
	} */
}

// if a class is declared with no constructors, the compiler
// automatically assumes default constructor and copy constructor
// for it.

// default constructor
Rectangle::Rectangle(){};

// copy constructor
Rectangle::Rectangle(const Rectangle &r){
	width = r.width;
	length = r.length;
}

// initialize with default constructor
Rectangle r1;
Rectangle *r3 = new Rectangle();

// initialize with copy constructor
Rectangle r4;
r4.set(60, 80);

Rectangle r5 = r4;
Rectangle r6(r4);
Rectangle *r7 = new Rectangle(r4);