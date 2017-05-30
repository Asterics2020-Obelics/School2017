
#include "array_sum.h"

/// Sum of array elements.
/**	@param tab  : float pointer ,    array to sum
 * 	@param size : unsigned int  ,    array size
 * 	@return     : float         ,    sum of array elements
*/
float array_sum(float* tab, unsigned int size){

    float result = 0.;
        for ( unsigned int i =0; i < size; ++i){
            result += tab[i];
        }
        return result;
}