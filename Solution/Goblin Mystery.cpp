#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t;
    cin>>t;
    
    while(t--){
        int n;
        int k;
        cin>>n>>k;
        
        int arr[n];
        int cnt = 0;
        
        for(int i = 0;i<n;i++)
        {
            cin>>arr[i];
        }
        
        for(int i =0; i<n; i++){
            if((arr[i]+k)%7 == 0){
                cnt++;
            }
        }
        
        cout << cnt<<endl;
    }
    return 0;
}