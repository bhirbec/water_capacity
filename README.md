# Water Capacity Problem

## High-level approach

### Key Observation

It's easy to compute the water capacity between the highest points.

```
                   max1
        left         |           max2      right
<----- subprob ----->|<-- easy -->|<----- subprob ----->
                     |            |
                     |            |
========================================================
```

### A closer look at the left subproblem

If we find the max then we can compute the water capacity between `max` and `max1`. We also have another `left subproblem`

```
                                                   max1
                                                    |
                    max                             |
                     |                              |
        left         |                              |
<----- subprob ----->|<----------- easy ----------->|
                     |                              |
=====================================================
```

### A closer look at the right subproblem

If we find the max then we can compute the water capacity between `max2` and `max`. We also have another `right subproblem`

```   
max2            
|                                                   
|                 max                                 
|                  |                              
|                  |              right                
|<----- easy ----->|<---------- subproblem --------->
|                  |                              
=====================================================
```

We can implement a recursive solution.
