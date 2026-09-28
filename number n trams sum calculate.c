// 2+5+8+11+14+....upto n terms. w.c.p to calculate sum of given seires
#include<stdio.h>
int main()
{
	int term=2, sum=0,i=1,n;
	printf("Enter the number of trem :");
	scanf("%d",&n);
	while(i<=n)
	{
		sum=sum+term;
		term=term+3;
		i++;
	}
	printf("sum of the term series=%d",sum);
	return 0;
}
