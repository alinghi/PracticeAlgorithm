#include <stdio.h>
int main()
{
    char x[11];
    char *j;
    int ans = 0;
    for (int i = 0; i < 11; i++)
        x[i] = '\0';
    scanf("%s", &x);
    if (x[0] == '0')
    {
        if (x[1] == 'x')
        {
            j = x + 2;
            while (*j)
            {
                if ((*j) >= '0' && (*j) <= '9')
                    ans = ans * 16 + ((*j) - '0');
                else
                    ans = ans * 16 + ((*j) - 'a' + 10);
                j = j + 1;
            }
        }
        else
        {
            j = x + 1;
            while (*j)
            {
                ans = ans * 8 + ((*j) - '0');
                j = j + 1;
            }
        }
    }
    else
    {
        j = x;
        while (*j)
        {
            ans = ans * 10 + ((*j) - '0');
            j = j + 1;
        }
    }
    printf("%d", ans);
    return 0;
}
