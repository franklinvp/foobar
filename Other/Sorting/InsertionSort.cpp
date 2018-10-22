#include<vector>

using namespace std;

void insertsort(vector<int>& L) {
    int n{L.size()};
    int last{0};
    while (last < n) {
        for (int i = last + 1; --i;) {
            if (L[i] < L[i - 1]) {
                swap(L[i], L[i - 1]);
            }
        }
        ++last;
    }
}
