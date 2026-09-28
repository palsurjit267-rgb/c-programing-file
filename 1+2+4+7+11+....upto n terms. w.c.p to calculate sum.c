//1+2+4+7+11+....upto n terms. w.c.p to calculate sum of given seires
#include<stdio.h>
int main()
{
	int i=1,n;
	int term=1, sum=0;
	printf("Enter the number of trem :");
	scanf("%d",&n);
	while(i<=n)
	{
		sum=sum+term;
		term=term+i;
		i++;
	}
	printf("sum of the term series=%d",sum);
	return 0;
}
