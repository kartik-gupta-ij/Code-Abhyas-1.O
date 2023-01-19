#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t;
    cin>>t;
    // Write your code here.
    for(int i=0;i<t;i++){
    int num;
    cin>>num;
    if(num>3999){
        cout<<"Invalid input";
        break;
    }
      string res="";
      string sym[]={"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
      int val[]={1000,900,500,400,100,90,50,40,10,9,5,4,1};
        for(int i=0; i<13&&num>0; i++)
        {
            while(num>=val[i])
            {
                int div=num/val[i];
                num-=div*val[i];
                while(div--) res+=sym[i];
            }
        }
        cout<<res<<"\n";
    }
        return 0;
}