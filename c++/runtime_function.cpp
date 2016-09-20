#include <iostream>
#include <cstdlib>
int main(int argc, char* argv[]) {
double x = atof(argv[1]);
std::cout << (x*x*x - 10);
return 0;
}