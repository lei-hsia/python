fake price: add all existing columns in the original file;

when it's done, the data size is significantly larger than when there are only fake price columns in the data: 
it's 3.05GB, and doubles the size when I want to ```stage``` the file first.

Solution: split the file. 

Steps: 
1. there're 36 million records in the original file;
2. I've tested that I can add 10 million each time and VM would not explode/exhaust RAM;
3. Repeat this 3 times.
