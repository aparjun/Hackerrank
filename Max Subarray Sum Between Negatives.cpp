#include <iostream>
using namespace std;

int main() 
{
	int n,in,s=0,max=-10000000;
	in=0;
	int x,y;
	cin>>n;
	int ar[n+2];
	ar[0]=-1;
	ar[n+1]=-1;
	for(int i=1;i<=n;i++)
	{
		cin>>ar[i];
	}
	for(int i=0;i<=n+1;i++)
	{
		s=0;
		if(ar[i]<0)
		{
				for(int j=in+1;j<i;j++)
				{
					s+=ar[j];
				}
				if(max<=s)
				{
					if(max==s)
					{
						if(i-in<y-x)
						{
						 x=in;
						 y=i;
						} 
					}
					else
					{
					 max=s;
					 x=in;
					 y=i;
					} 
				}
				in=i;
		}
	}
	for(int i=x+1;i<y;i++)
	{
		cout<<ar[i]<<" ";
	}
	return 0;
}
