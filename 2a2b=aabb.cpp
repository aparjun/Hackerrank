#include <iostream>
#include <string>
using namespace std;

int main()
{
	string s;
	getline(cin,s);
	int l=s.length();
	int c=0;
	for(int i=0;i<l;i++)
	{
		if((s[i]-'0')>=0 && (s[i]-'0')<=9)
		{
			c=c*10+(s[i]-'0');
		}
		else
		{
			for(int j=0;j<c;j++)
			{
				cout<<s[i];
			}
			c=0;
		}
	}
	return 0;
}
