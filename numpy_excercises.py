##numpy exerises

##1 how many negatives are there?

import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

mask_a = a[a < 0]
mask_a ##there are 4 negatives


##how many postives
pos_num = a[a > 0]
len(pos_num) ##there are 5

##3 how many even pos?
pos_and_even = pos_num[pos_num % 2 == 0]
len(pos_and_even) ##there are 3

##4 if you added 3, how many pos would there be?

c = a + 3
three_pos = c[c >0]
len(three_pos) ##there are 10

##5 if you squared?
squared = a**2
mean = squared.mean()
mean #mean == 74

standev = squared.std()
standev ## 144.0243

##6 centering
mean = a.mean()
centered = a - mean
centered

##7 calculate z score
z_scores = centered /a.std()
z_scores


 
