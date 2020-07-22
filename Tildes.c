#include <stdio.h>
#include <stdlib.h>

int *parent, *rank, *size; 

int findSet(int i) {
    return (parent[i] == i) ? i : (parent[i] = findSet(parent[i]));  
}

int findSize(int i){
    return size[findSet(i)];
}

int isSameSet(int i, int j){
    return findSet(i) == findSet(j); 
}

void unionSet(int i, int j){
    int x = findSet(i);
    int y = findSet(j); 
    if ((i != j)&&(x != y)){
        if (rank[x] > rank[y]){
            parent[y] = x;
            size[parent[x]]++; 
        }
        else{
            parent[x] = y; 
            if (rank[x] == rank[y])
                rank[y]++; 
            size[parent[y]]++; 
        }
    }
}

int main() {
    int N, Q, a, b, i; 
    char op;
    scanf("%d %d", &N, &Q);
    if (Q) {
        rank = (int*)malloc((size_t)(N << 4));
        parent = rank + N;
        size = parent + N; 
        for (i = 0; i < N; i++) {
            rank[i] = 0;
            parent[i] = i;
            size[i] = 1; 
        }
        while (Q-->0) {
            scanf(" %c", &op); 
            if (op == 't'){
                scanf(" %d %d", &a, &b); 
                unionSet(a-1, b-1); 
            }
            else {
                scanf(" %d", &a); 
                printf("%d\n", findSize(a-1)); 
            }
        }
    }
    free(rank);
    return 0;
}