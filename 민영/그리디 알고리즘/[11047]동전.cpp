#include <iostream>
using namespace std;

int main() {
    int n = 0 , k, i;
    cin >> n >> k;
    int *a;
    a = new int[n];

    for (i = 0; i < n; i++) {
        cin >> a[i];
    }
   
    int temp = k, count =0;

    while (temp != 0 && i != 0) {
        if (temp >= a[i - 1]) {
            count += temp / a[i - 1];
            //cout << "temp = " << temp << ", a[ "<< i-1 <<" ] = "<< a[i - 1] << ", count = " << count << endl;
            temp = temp % a[i - 1];
            i--;
        }
        else {
            i--;
        }
    }

    cout << count;
    return 0;
}