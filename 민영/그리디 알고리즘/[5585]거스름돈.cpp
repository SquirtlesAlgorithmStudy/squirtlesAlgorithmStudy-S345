#include <iostream>
using namespace std;

int main() {
    int a[6]= { 500, 100, 50, 10, 5, 1 };
    int price;
    cin >> price;
   
    int change = 1000 - price;
    int i = 0, count = 0;
    while (change != 0 && i != 6) {
        if (change >= a[i]) {
            count += change / a[i];
            //cout << "temp = " << change << ", a[ "<< i-1 <<" ] = "<< a[i - 1] << ", count = " << count << endl;
            change = change % a[i];
            i++;
        }
        else {
            i++;
        }
    }

    cout << count;
    return 0;
}