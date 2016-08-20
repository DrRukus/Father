#include <iostream>
#include <string>
#include <vector>
using namespace std;

std::vector<string> stringArray(string, string);

int main(int argc, char* argv[]) {

    string str1 = "First element";
    string str2 = "Second element";
    //string strArr[2] = stringArray("First element", "Second element");
    vector<string> strArr(2);
    strArr = stringArray(str1, str2);
    //strArr[0] = "First element";
    //strArr[1] = "Second element";

    cout << strArr[0] << endl;
    cout << strArr[1] << endl;

    return 0;
}

std::vector<string> stringArray(string str1, string str2) {
    //string outputArray[2] = {str1, str2};
    std::vector<string> outputVector(2);
    outputVector[0] = str1;
    outputVector[1] = str2;
    return outputVector;
}
