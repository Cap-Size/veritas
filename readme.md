# Veritas

A (soon to be) enterprise level tool for secrets (see definition) identification.

## Usage:
    python veritas.py


#### TODO
1. Create Filters (DONE)
1. Proper Arguements
1. A whole bunch of stuff that won't go here

#### Secrets

API keys, passwords, app IDs, certs, etc.


#### Big Thanks

I'd like to thank many people for their work in respective areas.

1. Michael Meli, Matthew R. McNiece, and Bradley Reaves
    - Their creation of a paper on finding secrets within GitHub was found during the creation of my tool and helped with the creation of filters that are a bif part of false-positive mitigation.
    - Their paper can be found [here](https://www.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_04B-3_Meli_paper.pdf)
1. Dylan Ayrey (dxa4481)
    - Creator of truffleHog
    - Helped in understanding how regex's implementation is so important/effective
    - List of regexes came from [here](https://github.com/dxa4481/truffleHogRegexes)