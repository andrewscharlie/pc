I have a feeling that any sort of a graph algorithm might be too slow for this - it seems like 1000 nodes might make it blow up. Trying to think of other algorithms, it seems like a decent approach might be to do a quick diff of the two bit strings, seeing what nodes need to be deactivated (switched from 0 to 1) and which need to be activated (1 to 0). However, the 3rd test input proves that this naive approach won't work:

```
4 1111 0000
100 1 1 1 1

Yields:
Case 3: 106
```