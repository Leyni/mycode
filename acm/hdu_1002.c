#include <stdio.h>
#include <string.h>

const int MAXN = 2000;
const int BASE = 10;

struct Number {
    int v[MAXN];
    int len;
};

void String2Number(const char* s, struct Number* n) {
    int slen = strlen(s);
    n->len = slen;
    for (int i = 0; i < slen; i++) {
        n->v[i] = s[slen - i - 1] - '0';
    }
}

void Plus(const struct Number* n1, const struct Number* n2, struct Number* n3) {
    n3->len = (n1->len > n2->len) ? n1->len : n2->len;

    for (int i = 0; i < n3->len; i++) {
        n3->v[i] += n1->v[i] + n2->v[i];
        if (n3->v[i] >= BASE) {
            n3->v[i + 1] += 1;
            n3->v[i] -= BASE;
        }
    }
    if (n3->v[n3->len] != 0) {
        n3->len++;
    }
}

void PrintNumber(const struct Number* n) {
    for (int i = 0; i < n->len; i++) {
        printf("%d", n->v[n->len - i - 1]);
    }
}

int main() {
    int t;
    char s1[MAXN];
    char s2[MAXN];
    struct Number n1;
    struct Number n2;
    struct Number n3;

    scanf("%d", &t);
    
    for (int i = 1; i <= t; i++) {
        scanf("%s %s", s1, s2);

        memset(n1.v, 0, sizeof(int) * MAXN); n1.len = 0;
        memset(n2.v, 0, sizeof(int) * MAXN); n2.len = 0;
        memset(n3.v, 0, sizeof(int) * MAXN); n3.len = 0;

        String2Number(s1, &n1);
        String2Number(s2, &n2);

        Plus(&n1, &n2, &n3);

        printf("Case %d:\n", i);
        PrintNumber(&n1);
        printf(" + ");
        PrintNumber(&n2);
        printf(" = ");
        PrintNumber(&n3);
        printf("\n");
        if (i != t) {
            printf("\n");
        }
    }

    return 0;
}
