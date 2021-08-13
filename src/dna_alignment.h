#ifndef DNA_ALIGNMENT_H
#define DNA_ALIGNMENT_H

#ifdef __cplusplus
extern "C" {
#endif

// typedef struct alignment {
// } alignment;

int hamming(const char*, const char*);
int score_identity(char, char);
int score_transition_transversion(char, char);
double global_align_score(const char*, const char*, double);
double local_align_score(const char* x, const char* y);
const char* local_align_trace(const char* x, const char* y);

#ifdef __cplusplus
}
#endif

#endif // DNA_ALIGNMENT_H
