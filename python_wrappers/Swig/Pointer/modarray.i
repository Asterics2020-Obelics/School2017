%module modarray

%{
    #define SWIG_FILE_WITH_INIT
    #include "array_sum.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (float* IN_ARRAY1, int DIM1) {(float* tab, int n)}


%include "array_sum.h"
