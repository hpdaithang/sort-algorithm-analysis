#include<bits/stdc++.h>

using namespace std ;
double a[1000005] ;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ifstream fin("data/test10_rand_float.txt");
    for(int i = 1 ; i <= 1000000 ;i ++) fin >> a[i] ;
    auto start = chrono::high_resolution_clock::now();
    sort(a + 1, a + 1000001);
    auto end_t = chrono::high_resolution_clock::now();
    for(int i = 1 ; i <= 1000000 ; i ++) cout << a[i] << " " ;
    chrono::duration<double> elapsed = end_t - start;
    cout << "\n\n" ;
    cout << "Time taken: " << elapsed.count() * 1000 << " ms\n";
}


