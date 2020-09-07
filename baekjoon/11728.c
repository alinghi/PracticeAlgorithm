#include <stdio.h>

void hanoi(int from, int to, int number);

int main(void)
{
    int input;
    int out;
    scanf("%d", &input);
    out = 1;
    for (int i = 0; i < input; i++)
    {
        out *= 2;
    }
    printf("%d\n", out - 1);
    hanoi(1, 3, input);
    return 0;
}

void hanoi(int from, int to, int number)
{
    int temp = 6 - from - to;
    if (number == 0)
        return;
    hanoi(from, temp, number - 1);
    printf("%d %d\n", from, to);
    hanoi(temp, to, number - 1);
}
