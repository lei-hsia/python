
// define a class hierarchy
// class DerivedClassName:access-level BaseClassName
class Polygon{
protected:
	int numVertices;
	float xCorrd; float yCorrd;
public:
	void set(float x, float y, int nV);
}

class Triangle : public Polygon{

public:
	float area();
}

/* private inheritance: all public/protected members of the base
	class become the private members of the derived class

	public inheritance: all public members of the base class become
	public members of the derived class, all protected members
	of the base class become protected members of derived class

	protected inheritance: all public/protected members of the 
	base class become the protected members of the derived class
*/