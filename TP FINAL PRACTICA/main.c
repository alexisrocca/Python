#include <stdio.h>
#include <stdlib.h>

// int main(int argc, char *argv[]) {
//     for (int i = 0; i < argc; i++) {
//         printf("argv[%d] = %s\n", i, argv[i]);
//     }
//     return 0;
// }

int main(int argc, char *argv[]) {
    
    char *nombre = argv[1];

    printf("Nombre: %s\n",nombre);

    return 0;
}
