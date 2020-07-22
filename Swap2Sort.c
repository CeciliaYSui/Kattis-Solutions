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
    if (rank[x] > rank[y]){
        parent[y] = x;
    }
    else{
        parent[x] = y; 
        if (rank[x] == rank[y])
            rank[y]++; 
    }
}

int main() {
    int N, Q, a, b, i, j; 
    scanf("%d %d", &N, &Q);
    rank = (int*)malloc((size_t)(N<<3));
    parent = rank + N;
    for (i = 0; i < N; i++) {
        rank[i] = 0;
        parent[i] = i;
    }
    while (Q-->0) {
        scanf(" %d %d", &a, &b);
        unionSet(a-1,b-1); 
    }
    for (j = 0; j <= N/2; j++){
        if (!isSameSet(j,N-j-1)){
            printf("No\n"); 
            return 0; 
        }
    }
    printf("Yes\n"); 
    return 0;
}