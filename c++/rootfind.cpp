#include <iostream>
#include <cstdlib>
#include <cmath>
#include "function.cpp"

using namespace std;

const double ACCURACY = 10e-12;
const double AUREO = 2 / (sqrt(5) - 1);

struct Interval {
	double a, b;
	int iterations;
	int errorCode;
};

struct Root {
	double x;
	int iterations;
	int errorCode;
};

Interval* findInterval(const RuntimeFunction& func, double z, int maxIter)
{
	double a, b;

	if (z == 0)
	{
		a = -0.05;
		b = 0.05;
	}
	else
	{
		a = 0.95 * z;
		b = 1.05 * z;
	}
		
	double fa = func.run(a);
	double fb = func.run(b);
	int i = 0;

	while (fa * fb > 0 && i++ < maxIter)
	{
		if (abs(fa) < abs(fb))
		{
			a -= AUREO * (b - a);
			fa = func.run(a);
		}
		else
		{
			b += AUREO * (b - a);
			fb = func.run(b);
		}
	}

	Interval* interval = new Interval;
	interval->a = a;
	interval->b = b;
	interval->iterations = i;
	interval->errorCode = fa * fb >= 0;

	return interval;
}

Root* bissection(const RuntimeFunction& func, double a, double b, double tolerance, int maxIter)
{
	double fa = func.run(a);
	double fb = func.run(b);

	double xVar = abs(b - a) / 2;
	double x = a + xVar;
	double fx = func.run(x);

	int i = 0;

	while (xVar > tolerance && abs(fx) > tolerance && i++ < maxIter)
	{
		if (fx * fa < 0)
		{
			b = x;
			fb = func.run(b);
		}
		else
		{
			a = x;
			fa = func.run(a);
		}

		xVar = xVar / 2;
		x = a + xVar;
		fx = func.run(x);
	}

	int errorCode = 1;

	if (fa * fb < 0)
	{
		if (abs(fx) > tolerance)
			errorCode = 2;
		else if (i == maxIter)
			errorCode = 3;
		else
			errorCode = 0;
	}

	Root* root = new Root;
	root->x = a + xVar;
	root->iterations = i;
	root->errorCode = errorCode;

	return root;
}

int main(int argc, char* argv[])
{
	string funcStr;
	if (argc > 1) funcStr = argv[1];
	else return 1;

	double z = 0;
	if (argc > 2) z = atof(argv[2]);

	int iter = 40;
	if (argc > 3) iter = atoi(argv[3]);

	RuntimeFunction func("runtime_function");
	func.compile(funcStr);

	Interval* interval = findInterval(func, z, iter);
	Root* root = bissection(func, interval->a, interval->b, ACCURACY, iter);

	cout
		<< "Interval: ("
		<< interval->a << ", "
		<< interval->b << ", "
		<< interval->iterations << ", "
		<< interval->errorCode << ")" << endl
		<< "Root: ("
		<< root->x << ", "
		<< root->iterations << ", "
		<< root->errorCode << ")" << endl;

	return 0;
}