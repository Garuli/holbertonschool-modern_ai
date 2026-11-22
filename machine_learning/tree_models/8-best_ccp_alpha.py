#!/usr/bin/env python3
"""Module that selects the best ccp_alpha for post-pruning."""


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    """Pick the alpha with best test score, smallest gap, largest alpha."""
    best_test = max(test_scores)
    candidates = [i for i in range(len(clfs))
                  if test_scores[i] == best_test]
    best_gap = min(abs(train_scores[i] - test_scores[i])
                   for i in candidates)
    candidates = [i for i in candidates
                  if abs(train_scores[i] - test_scores[i]) == best_gap]
    best = max(candidates, key=lambda i: ccp_alphas[i])
    return ccp_alphas[best], clfs[best]
