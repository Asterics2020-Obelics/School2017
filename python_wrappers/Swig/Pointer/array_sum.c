/// Sum of array elements.
/**	@param tab  : float pointer ,    array to sum
 * 	@param n    : unsigned int  ,    array n
 * 	@return     : float         ,    sum of array elements
*/
float array_sum(float* tab, int n){

    float result = 0.;
        for ( int i =0; i < n; ++i){
            result += tab[i];
        }
        return result;
}
