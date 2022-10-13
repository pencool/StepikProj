import sys
from collections import Counter

print(Counter({k: int(v) for k, v in [line.split() for line in
                                    sys.stdin]}).most_common()[-2][0])
