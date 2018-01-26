# NAME

pyprefixspan:

pyprefixspan - Python implementation for the algorithm PrefixSpan (Prefix-projected Sequential Pattern mining).

# INSTALL

    pip install pyprefixspan

# SYNOPSIS

    from pyprefixspan import pyprefixspan
    
    data = [
        'a c d',
        'a b c',
        'c b a',
        'a a b'
    ]
    
    p = pyprefixspan(data)
    p.run()
    p.out
    # p.out got as follow.
    #  {'a': 5, 'a c': 2, 'a b': 2, 'c': 3, 'b': 3}
    
    options:
    # set minimum support (default: 2)
    p.setminsup(2)
    
    # set minimum pattern length (default: 1)
    p.setlen(1)
    
# DESCRIPTION

pyprefixspan is pure perl implementation
for the algorithm PrefixSpan (Prefix-projected Sequential Pattern mining) 
by designed Pei et al.

This module is not fast.

Reference

\* PrefixSpan: Mining Sequential Patterns Efficiently by Prefix-Projected Pattern Growth Jian Pei, Jiawei Han, Behzad Mortazavi-asl, Helen Pinto, Qiming Chen, Umeshwar Dayal and Mei-chun Hsu IEEE Computer Society, 2001, pages 215.

# LICENSE

The MIT License (MIT)

Copyright (C) 2018 Yukio TAKAHASHI

This library is free software; you can redistribute it and/or modify
it under the same terms as Python itself.

# AUTHOR

Yukio TAKAHASHI <takman@tuna.jpn.org>
