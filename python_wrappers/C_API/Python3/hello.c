#include <string.h>
#include <stdlib.h>


char * hello(const char * what){
  size_t what_size = strlen(what);
  char* result = (char*) malloc( (what_size + 6) * sizeof(char));
  strcpy(result, "Hello "); 
  strcat(result, what);
  return result;
}

