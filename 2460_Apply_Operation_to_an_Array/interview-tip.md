# Interview Tip: In-Place Algorithms

In-place algorithms overwrite the input to save space, but sometimes this can cause problems. Here are a couple of situations where an in-place algorithm might not be suitable:

1. The algorithm needs to run in a multi-threaded environment without exclusive access to the array. Other threads might need to read the array as well and may not expect it to be modified.
2. Even if there is only a single thread or the algorithm has exclusive access to the array while running, the array might need to be reused later or by another thread once the lock has been released.

In an interview, always check whether the interviewer is okay with you overwriting the input. Be prepared to explain the pros and cons of doing so if asked!