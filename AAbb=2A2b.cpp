#include <iostream>
using namespace std;

int main()
{
	string s;
	getline(cin,s);
	s+="0";
	int l=s.length();
	int c=1;
	for(int i=1;i<l;i++)
	{
		if(s[i]!=s[i-1])
		{
			cout<<c<<s[i-1];
			c=1;
		}
		else
		{
			c+=1;
		}
	}
	return 0;
}
