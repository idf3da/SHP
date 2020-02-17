#include <stdlib.h>
#include <stdio.h>
#include <time.h>

unsigned int cur_rand = 1;

void rseed(unsigned int x) {
    cur_rand = x;
}

unsigned int rrand() {
    return cur_rand = (cur_rand * 1103515245 + 12345) % (1 << 31);
}

int main() {
    const char *flag = getenv("FLAG");
    printf("Send me a number\n");
    rseed(time(NULL));
    unsigned int p = rrand();
    unsigned int r;
    scanf("%u", &r);
    if (r == p) {
        printf("%s", flag);
    } else {
        printf("Nope");
    }
}