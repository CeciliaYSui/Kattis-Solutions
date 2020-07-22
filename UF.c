#include <stdio.h>
#include <stdlib.h>

int *parent, *rank; 

int findSet(int i) {
    return (parent[i] == i) ? i : (parent[i] = findSet(parent[i]));  
}

int isSameSet(int i, int j){
    return findSet(i) == findSet(j); 
}

void unionSet(int i, int j){
    int x = findSet(i);
    int y = findSet(j);
    if (x != y){
        if (rank[x] > rank[y]){
            parent[y] = x;
        }
        else{
            parent[x] = y; 
            if (rank[x] == rank[y])
                rank[y]++; 
        }
    }
}

int main() {
    int N, Q, a, b, i; 
    char op;
    scanf("%d %d", &N, &Q);
    if (Q) {
        rank = (int*)malloc((size_t)(N << 3));
        parent = rank + N;
        for (i = 0; i < N; i++) {
            rank[i] = 1;
            parent[i] = i;
        }
        while (Q-->0) {
            scanf(" %c %d %d", &op, &a, &b);
            if (op == '?'){
                printf(isSameSet(a,b) ? "yes\n" : "no\n"); 
            }
            else {
                unionSet(a,b); 
            }
        }
    }
    free(rank);
    return 0;
}