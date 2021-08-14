// author:  Shane Drabing
// license: MIT
// email:   shane.drabing@gmail.com


#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <math.h>

#include "dna_alignment.h"


int score_identity(char xx, char yy) {
    if (xx == yy) {
        return 1;
    }
    return -1;
}


int score_transition_transversion(char xx, char yy) {
    if (xx == yy) {
        return 1;
    }
    switch (xx) {
    case 'A':
        return (yy == 'G') ? -1 : -5;
    case 'C':
        return (yy == 'T') ? -1 : -5;
    case 'G':
        return (yy == 'A') ? -1 : -5;
    case 'T':
        return (yy == 'C') ? -1 : -5;
    }
    return -5;
}


double global_align_score(const char* x, const char* y, double pt_gap) {
    // declare variables
    double** mat;
    char xx, yy;
    int u, v, u_lt_v, i, j, ii, jj;
    double score, max_score, min_score;
    double pt_mod, a, b, c;

    // grab the string lengths
    u = strlen(x);
    v = strlen(y);

    // allocate memory
    mat = (double**)malloc((1 + u) * sizeof(double*));
    for (i = 0; i <= u; i++) {
        mat[i] = (double*)malloc((1 + v) * sizeof(double));
    }

    // initialize matrix values
    for (i = 0; i <= u; i++) {
        for (j = 0; j <= v; j++) {
            mat[i][j] = pt_gap * (i + j);
        }
    }

    // for each cell to compute
    for (i = 0; i < u; i++) {
        ii = i + 1;
        xx = x[i];
        for (j = 0; j < v; j++) {
            jj = j + 1;
            yy = y[j];

            // possible scores
            a = mat[i][j] + score_transition_transversion(xx, yy);
            b = mat[ii][j] + pt_gap;
            c = mat[i][jj] + pt_gap;

            // pick the best score, update the matrix
            mat[ii][jj] = (a >= b && a >= c) ? a : (b >= c) ? b : c;
        }
    }
    
    // bottom right corner holds the global score
    score = mat[ii][jj];

    // calculate max score
    u_lt_v = (u < v);

    max_score = (
        score_transition_transversion('A', 'A') * (u_lt_v ? u : v) +
        pt_gap * (u_lt_v ? (v - u) : (u - v))
    );

    min_score = (
        score_transition_transversion('A', 'C') * (u_lt_v ? u : v) +
        pt_gap * (u_lt_v ? (v - u) : (u - v))
    );

    // free our memory
    for (i = 0; i < u; i++) {
        free(mat[i]);
    }
    free(mat);

    // return the scores
    return (score - min_score) / (max_score - min_score);
}


const char* local_align_trace(const char* x, const char* y) {
    // declare variables
    double** mat;
    char xx, yy;
    char* build;
    size_t build_len, u, v, u_lt_v, i, j, ii, jj;
    int best_i, best_j;
    double best_score;
    double pt_mod, pt_gap, a, b, c;

    // set pt_gap
    pt_gap = -2;

    // grab the string lengths
    u = strlen(x);
    v = strlen(y);

    // allocate memory
    build = (char*)malloc((u + v) * sizeof(char));
    build_len = 0;

    mat = (double**)malloc((1 + u) * sizeof(double*));
    for (i = 0; i <= u; i++) {
        mat[i] = (double*)malloc((1 + v) * sizeof(double));
    }

    // initialize matrix values
    for (i = 0; i <= u; i++) {
        for (j = 0; j <= v; j++) {
            mat[i][j] = pt_gap * i;
        }
    }

    // for each cell to compute
    for (i = 0; i < u; i++) {
        ii = i + 1;
        xx = x[i];
        for (j = 0; j < v; j++) {
            jj = j + 1;
            yy = y[j];

            // possible scores
            a = mat[i][j] + (3 * score_identity(xx, yy));
            b = mat[ii][j] + pt_gap;
            c = mat[i][jj] + pt_gap;

            // pick the best score, update the matrix
            mat[ii][jj] = (
                (a >= b && a >= c) ? a :
                (b >= c) ? b :
                (c > 0) ? c : 0
            );
        }
    }
    
    // find best score
    best_score = -INFINITY;
    for (i = 0; i <= u; i++) {
        for (j = 0; j <= v; j++) {
            if (mat[i][j] > best_score) {
                best_score = mat[i][j];
                best_i = i;
                best_j = j;
            }
        }
    }

    i = best_i;
    j = best_j;

    // traceback
    while ((i > 0 || j > 0) && mat[i][j] != 0) {
        ii = i - 1;
        jj = j - 1;

        if ((i > 0 && j > 0) &&
            (mat[ii][jj] >= mat[ii][j]) &&
            (mat[ii][jj] >= mat[i][jj])) {

            build[build_len++] = y[jj];
            i = ii;
            j = jj;
        } else if ((i > 0) && (j <= 0) || (mat[ii][j] >= mat[i][jj])) {
            i = ii;
        } else if (j > 0) {
            build[build_len++] = y[jj];
            j = jj;
        }
    }

    // terminate
    build[build_len++] = '\0';

    // free our matrix memory
    for (i = 0; i <= u; i++) {
        free(mat[i]);
    }
    free(mat);

    return build;
}
