// author:  Shane Drabing
// license: MIT
// email:   shane.drabing@gmail.com


#ifndef DNA_ALIGNMENT_H
#define DNA_ALIGNMENT_H

#ifdef __cplusplus
extern "C" {
#endif


int score_identity(char, char);
int score_transition_transversion(char, char);
double global_align_score(const char*, const char*, double);
const char* local_align_trace(const char* x, const char* y);


#ifdef __cplusplus
}
#endif

#endif // DNA_ALIGNMENT_H
