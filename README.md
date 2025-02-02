# intro_recommendersystem

Implement solution thought in class & Thompson sampling

#Our technique (Mai)

  - We arbitrarily test each medicine once in the first 10 days to ensure all treatments are evaluated at least once. After that, we prioritize treatments based on
their success rate ("true_probabilities"), selecting those with the highest number of positive outcomes. 
  - If a treatment fails 3 times, we eliminate it permanently (unless it's the last remaining option). 
  - This process continues, progressively refining the selection to focus on the most effective treatments while discarding ineffective ones.

Example of result:


#Thompson sampling: (Léon)
Look up Beta-distribution and multi-armed bandit 
scipy.stats.beta
