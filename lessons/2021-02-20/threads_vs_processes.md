Characteristics|Threads|Processes
---|---|---
Spawn|Within one process|Independent processes
Start|Fast|Slower compared to threads
Memory|Shared|Separate per process
GIL|Important|One per process, no impact
Common usage|I/O-bound|CPU-bound
Started|Thread after thread|In parallel
Killable|No|Yes