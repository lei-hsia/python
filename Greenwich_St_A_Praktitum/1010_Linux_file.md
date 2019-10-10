
1. If you want to find and print the top 10 largest files names (not directories) in a particular directory and its sub directories:

``` $ find . -printf '%s %p\n'|sort -nr|head ```

2. To restrict the search to the present directory use "-maxdepth 1" with find.

```$ find . -maxdepth 1 -printf '%s %p\n'|sort -nr|head```

3. And to print the top 10 largest "files and directories":

```$ du -a . | sort -nr | head```

**Use "head -n X" instead of the only "head" above to print the top X largest files (in all the above examples)**
