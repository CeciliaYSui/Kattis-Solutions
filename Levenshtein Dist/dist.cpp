#include <iostream>
#include <algorithm>
using namespace std;

// compute Levenshtein distance between a & b
int dist(string a,string b)
{
    // a is empty, insert whatever is left in b
    if (a=="") return b.length();

    // b is empty, insert whatever is left in a
    if (b=="") return a.length();

    // first characters match, shrink the problem
    if (a[0] == b[0]) return dist(a.substr(1),b.substr(1));

    // try all possible edits
    return 1 + min({
        dist(a,b.substr(1)),            // insert at a[i] char in b[j]
        dist(a.substr(1),b),            // remove a[i]
        dist(a.substr(1),b.substr(1))   // replace a[i] with b[j]
    });
}

int main(int argc,char *argv[]) 
{
    cout << dist(argv[1],argv[2]) << "\n";
}
