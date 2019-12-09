#include <iostream>
#include <string>

using namespace std;

string numtobi(int a){
    int t=0;
    string s="";
    while (a>0){
        s=(a%2?"1":"0")+s;
        a/=2;
    }
    return s;
}
int main(){
   string s,sn="";
   int k=0,sum=0;
   cout<<"Input message:";
   getline(cin,s);
   sn=s;
   for(int i=0;i<s.length();i++){
       sn+=numtobi(int(s[i]));
       sum+=int(s[i]);
   }
    for(int i=0;i<sum%255+12;i++){
        sn+=sn[0];
        sn.erase(0);
        for(int j=0;j<s.length();j++){
            k=(k*int(s[j])+int(s[s.length()-j+1]))%1000;
        }
    }
   cout<<"HASHSUM = "<<k;
   return 0; 
}