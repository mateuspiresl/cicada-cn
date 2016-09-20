#include <iostream>
#include "function.cpp"

using namespace std;

int main()
{
	Function func("my_func");
	func.compile("x + x");

	cout << func.run(10.0) << endl;

	return 0;
}