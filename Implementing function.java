/******************************************************************************

You are required to implement the following function 

int LargeSmallSum(int arr[]);

The function accepts an integer arr of size ’length’ as its arguments you are required to return the sum of the second largest element from the even positions and the second smallest from the odd position of given ‘arr’ 

Assumption

All array elements are unique 

Treat the 0th position a seven 

Note

Return 0, if the array is empty 

Return 0, if array length is 3 or less than 3 

Example 

Input 

6

3 2 1 7 5 4 

Output 

7 

Explanation 

Second largest among even position elements (1 3 5) is 3 

Second smallest among odd position elements (7 4 2) is 4 

Thus output is 3+4 = 7 

Input format
The first input is the size of the array

The next line of integers is the array of elements

Output format
The output integer is the result as required.


*******************************************************************************/
import java.util.*;

class Main
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in) ;
        int n , x ;
        n = sc.nextInt() ; 
        
        Vector<Integer> v1 = new Vector<Integer>() ;
        Vector<Integer> v2 = new Vector<Integer>() ;
        
        for(int i = 0 ; i<n ; i++)
        {
            x = sc.nextInt() ;
            if(i%2 == 0) v1.add(x) ;
            else v2.add(x) ;
        }
        Collections.sort(v1) ;
        Collections.sort(v2) ;
        Collections.reverse(v1) ;
        
        LinkedHashSet<Integer> hashSet = new LinkedHashSet<Integer>(v1) ;
        v1.clear() ;
        v1.addAll(hashSet) ;
        
        LinkedHashSet<Integer> hashSet1 = new LinkedHashSet<Integer>(v2) ;
        v2.clear() ;
        v2.addAll(hashSet1) ;
        
        System.out.print(v2.get(1) + v1.get(1)) ;
    }
}