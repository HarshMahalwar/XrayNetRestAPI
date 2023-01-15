#include<stdio.h>

int gcd(int k1)
{
    int num = 26;
    while(num)
    {
        k1 %= num;
        k1 ^= num;
        num ^= k1;
        k1 ^= num;
    }
    return k1;
}

int main()
{
    char str[5];
    for(int i = 0; i < 5; i++)
        scanf("%c", &str[i]);
    int k1, k2;
    scanf("%d", &k1);
    scanf("%d", &k2);
    int array[5];
    for(int i = 0; i < 5; i++)
        array[i] = str[i] - 'a';
    for(int i = 0; i < 5; i++)
    {
        array[i] = (array[i] * k1 + k2) % 26;
        str[i] = array[i] + 'a';
    }
    int k_inverse = -1;
    printf("%s\n", str);

    if(gcd(k1) == 1){
        for(int i = 0; i < 26; i++)
        {
            if((k1 * i) % 26 == 1)
                k_inverse = i;
        }
    }
    if(k_inverse == -1){
        printf("error");
        return 0;
    }
    for(int i = 0; i < 5; i++)
    {
        array[i] = ((26 + array[i] - k2) * k_inverse) % 26;
        str[i] = array[i] + 'a';
    }
    printf("%s", str);
    return 0;
}
