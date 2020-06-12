This one I had solve before at

    https://github.com/franklinvp/foobar/blob/master/foobar2018/extra_challenge5_Ion_Flux_Relabeling.py

but somehow it had a bug, and not in one of the secret test cases, but in the first one.
I either didn't test it properly or at all, or maybe did some refactoring after the fact
and introduced the bug.

Now it is fixed.

The bug was the case of the input node being of the form 2^k-1.
