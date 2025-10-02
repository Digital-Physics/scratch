## Discounted Rewards (Geometric Sum)

**Infinite sum:**
- Series: $V = R + R \cdot \gamma + R \cdot \gamma^2 + ...$
- Closed-form: $V = R \cdot (1/(1 - \gamma))$
- Recursive: $V = R + \gamma \cdot V$

*Note: This represents the discounted, present value of a **fixed reward stream** R, not tied to any agent policy. It's the present value of receiving reward R at every step forever.*

*Example: With R = 10 and γ = 0.9, we get V = 10/(1 - 0.9) = 100*

**Partial sums (finite horizon):**
- Series: $S_n = R + R \cdot \gamma + R \cdot \gamma^2 + ... + R \cdot \gamma^n$
- Closed-form: $S_n = R \cdot \frac{1-\gamma^{n+1}}{1-\gamma}$
- Recursive: $S_n = R + \gamma \cdot S_{n-1}$

*With a limited horizon, you only sum rewards up to step n; still follows the same pattern.*

---

## Q-Value: Old Estimate

$Q(s, a)$ = Expected immediate reward + One-period, discounted Present Value of future rewards (following our current best policy estimate)

*This is our current guess of long-term value, built recursively from immediate reward plus future estimates.*

---

## Q-Learning Update: Sample-Based Estimate

**PV Estimate from Recent Experience (sample):**
- $r + \gamma \cdot \max_{a'} Q(s', a')$

*This is a one-step bootstrapped estimate: we observe the actual immediate reward r, then estimate future value using our current Q-function at the next state s'.*

**Q-Learning Update Rule (blended estimate):**
- $Q_{new}(s, a) = (1 - \alpha) \cdot \text{Old PV Estimate} + \alpha \cdot \text{PV Estimate from Recent Experience}$

*The new estimate is a weighted average: stick mostly with the old belief, but shift toward the new sample by the learning rate α.*
~
**Equivalent form (temporal-difference error):**
- $Q_{new}(s, a) = Q_{old}(s, a) + \alpha[(r + \gamma \cdot \max_{a'} Q(s', a')) - Q_{old}(s, a)]$

