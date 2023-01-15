#include<stdio.h>

int main()
{
    int x = 535353;
    int y = (x << 16) | (x >> 16);
    printf("%d", y);
    return 0;
}