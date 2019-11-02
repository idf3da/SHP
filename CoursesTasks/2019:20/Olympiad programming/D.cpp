#include <iostream>
using namespace std;

int main() {
    long long x0,y0,x1,y1,x2,y2,x3,y3,x11,x12,y11,y12,s = 0;
    
    cin >> x0 >> y0 >> x1 >> y1;

    cin>> x2 >> y2 >> x3 >> y3;

    x11 = max(min(x0,x1),min(x2,x3));
    x12 = min(max(x0,x1),max(x2,x3));
    y11 = max(min(y0,y1),min(y2,y3));
    y12 = min(max(y0,y1),max(y2,y3));
    
    if ((x12 - x11 > 0) && (y12 - y11 > 0)){
      s = (x12 - x11) * (y12 - y11);
    }
    cout << s;
    return 0;
}