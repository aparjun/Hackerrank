#include <iostream>
using namespace std;

int main() {
	int n,m;
	cin>>n>>m;
	int ar[100][100]={0};
	for(int i=1;i<=n;i++)
	{
	    for(int j=1;j<=m;j++)
	    {
	        cin>>ar[i][j];
	    }
	}
	int c=0;
	int m1=-1000,x,y;
	for(int i=1;i<=n;i++)
	{
	    for(int j=1;j<=m;j++)
	    {
	        c=ar[i-1][j-1]+ar[i-1][j]+ar[i-1][j+1]+
	            ar[i][j-1]+ar[i][j+1]+
	            ar[i+1][j-1]+ar[i+1][j]+ar[i+1][j+1];
	           if(m1<c)
	           {
	               m1=c;
	               x=i;
	               y=j;
	           }
	        
	            
	        
	    }
	}
	cout<<x<<" "<<y<<" "<<m1;
	return 0;
}
