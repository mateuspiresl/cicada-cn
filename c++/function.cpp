#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>

#include <stdexcept>
#include <stdio.h>

using namespace std;

class RuntimeFunction {
private:
	string name;

	string executeCommand(const char* cmd) const
	{
	    char buffer[128];
	    string result = "";
	    FILE* pipe = popen(cmd, "r");

	    if (!pipe) throw runtime_error("popen() failed!");

	    try {
	        while (!feof(pipe)) {
	            if (fgets(buffer, 128, pipe) != NULL)
	                result += buffer;
	        }
	    } catch (...) {
	        pclose(pipe);
	        throw;
	    }

	    pclose(pipe);
	    return result;
	}

public:
	RuntimeFunction(string name) :
		name(name)
		{ }

	void compile(string function)
	{
		ofstream file;
		file.open((name + ".cpp").c_str());
		file 	<< "#include <iostream>\n"
				<< "#include <cstdlib>\n"
				<< "int main(int argc, char* argv[]) {\n"
					<< "double x = atof(argv[1]);\n"
					<< "std::cout << (" << function << ");\n"
					<< "return 0;\n"
				<< "}";
		file.close();

		system(("g++ -O2 " + name + ".cpp -o " + name).c_str());
	}

	double run(double x) const
	{
		stringstream ss;
		ss << name << ".exe " << x;

		string ret = executeCommand(ss.str().c_str());
		return atof(ret.c_str());
	}

};

/*int main(int argc, char* argv[])
{
	compile(argv[1]);
	double ret = run(atof(argv[2]));

	cout << ret << endl;

	return 0;
}*/