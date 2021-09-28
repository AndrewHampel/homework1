from hwfunctions import fun_factor, fun_inc
from dask import delayed



def delayed_increment(c, start, end):
    # use fun_inc
    
    # Use delay operation to create parallel version
    operation = [delayed(fun_inc)(i) for i in range(start, end)]
    
    # Compute the sum 
    result = delayed(sum)(operation)
    return result


def delayed_factor(c, start, end):
    # use fun_factor
    
    # Use delay operation to create parallel version
    operation = [delayed(fun_factor)(i) for i in range(start, end)]
    
    # Compute the sum 
    result = delayed(sum)(operation)
    return result


def future_increment(c, start, end):
    # use fun_inc
    
    # Create a list called my_result
    my_result = []
    
    # Append increments to my_result 
    for i in range(start, end):
        my_result.append(fun_inc(i))
      
    # Segment result into different sections
    increment = [my_result[i::4] for i in range(4)]
    
    # Create a list called final_result 
    final_result = []
    
    # Append each segment to the list
    for seg in increment:
        final_result.append(sum(seg))
    
    # Compute the sum and return result
    return c.submit(sum, final_result)


def future_factor(c, start, end):
    # use fun_factor
    
    # Create a list called my_result 
    my_result = []
    
    # Add facor values to the list
    for i in range(start, end):
        a = c.submit(fun_factor, i)
        my_result.append(a)
    
    # Compute sum and return result
    return c.submit(sum, my_result)
    
