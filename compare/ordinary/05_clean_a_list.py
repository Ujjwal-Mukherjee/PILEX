import numpy as np
scores = [56, 54, 62, 48, 999, 58, 61, 55]
q1, q3 = np.percentile(scores, [25, 75])
iqr = q3 - q1
scores = [x for x in scores if q1 - 1.5 * iqr <= x <= q3 + 1.5 * iqr]
print(min(scores), max(scores), np.mean(scores), np.median(scores))
