#include <triangulation/ntriangulation.h>
#include <cstring>

#define MAXLEN 1000 // TODO: Work out what the real upper bound should be.

using namespace regina;

bool interesting(NTriangulation* t) {
    return t->isThreeSphere();
}

// Return true iff we didn't just receive a termination request.
int main() {
    unsigned long tot = 0;

    char input[MAXLEN];
    while (true) {
        int res = scanf("%s", input);
        if (feof(stdin) || ! res)
            break;

        NTriangulation* t = NTriangulation::fromIsoSig(input);
        if (interesting(t)) {
            printf("%s\n", input);
            ++tot;
        }
        delete t;
    }

    fprintf(stderr, "Total found: %ld\n", tot);
    return 0;
}

