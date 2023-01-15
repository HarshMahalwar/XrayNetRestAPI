#include<stdio.h>int main()
{
    char str[5];
    for(int i = 0; i < 5; i++)
        scanf("%c", &str[i]);

    int array[5] = {0};
    for(int i = 0; i < 5; i++)
        array[i] = str[i] - 'a';
    int k;
    scanf("%d", &k);
    for(int i = 0; i < 5; i++){
        array[i] = (array[i] + k) % 26;
        str[i] = array[i] + 'a';
    }
    printf("%s", str);
    printf("\n");
    for(int i = 0; i < 5; i++){
        array[i] = (26 + array[i] - k) % 26;
        str[i] = array[i] + 'a';
    }
    printf("%s", str);
    return 0;
}
