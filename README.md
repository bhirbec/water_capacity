# Water Capacity Problem

## High-level approach

### Key Observation

It's easy to compute the water capacity between two maximums.

```
                   max1
                     |           max2
<----- subprob ----->|<-- easy -->|<----- subprob ----->
                     |            |
                     |            |
========================================================
```

### Step 1

We find the max and setup two pointers (called `left` and `right`) at its position.

```
   max_left = max_right
            |
            |
            |
            |
============|============================================
       left = right
```

### Step 2

We find the next max and compute the water capacity between the two maximums.

```
           max_left
            |              max_right
            |               |
            |               |
            |               |
============|===============|============================
           left            right
```

### Step 3

We find the next max but this time we're facing 3 cases.

**1. The new max is located between `left` and `right`.**

```
           max_left
            |              max_right
            |        m      |
            |        |      |
            |        |      |
============|===============|============================
           left      i     right
```

We can skip this case since we already computed the capacity between these two points.

**2. The new max is located after the `right` pointer.**

```
           max_left
            |              max_right
            |               |             m
            |               |             |
            |               |             |
============|===============|=============|==============
           left            right          i
```
We can compute the capacity between `right` and `i`. Then we update the position of the `right` pointer.

```
           max_left
            |              
            |                             max_right
            |                             |
            |                             |
============|=============================|===========
           left                           right
```

**3. The new max is located before the `left` pointer.**

This case is similar to the previous one but we compute the capacity between `i` and `left`, and we update the `left` pointer.

### Next steps

We repeat the last step until the entire array has been visited.


