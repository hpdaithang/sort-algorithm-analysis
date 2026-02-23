#include<bits/stdc++.h>

using namespace std ;
double a[1000005] ;

string name1 = "data/test01_inc.txt" ,
name2 = "data/test02_dec.txt" ,
name3 = "data/test03_rand_int.txt" ,
name4 = "data/test04_rand_int.txt" ,
name5 = "data/test05_rand_int.txt" ,
name6 = "data/test06_rand_float.txt"  ,
name7 = "data/test07_rand_float.txt" ,
name8 = "data/test08_rand_float.txt" ,
name9 = "data/test09_rand_float.txt" ,
name10 = "data/test10_rand_float.txt";

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ifstream fin(name10);
    for(int i = 1 ; i <= 1000000 ;i ++) fin >> a[i] ;
    auto start = chrono::high_resolution_clock::now();
    sort(a + 1, a + 1000001);
    auto end_t = chrono::high_resolution_clock::now();
    for(int i = 1 ; i <= 1000000 ; i ++) cout << a[i] << " " ;
    chrono::duration<double> elapsed = end_t - start;
    cout << "\n\n" ;
    cout << "Time taken: " << elapsed.count() * 1000 << " ms\n";
}


