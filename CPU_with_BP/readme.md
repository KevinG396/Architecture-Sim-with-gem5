# Project Structure
### Caches.py is used to define L1ICache, L1DCache and L2Cache, other parts including Branch Predictor of the CPU (In Order Execution) are defined in cpu_bp.py.
### Two kinds of Branch Predictors can be used in the project: LocalBP and TournamentBP.

# Usage
#### Run $GEM5/build/ARM/gem5.opt --outdir="queens_tournament" cpu_bp.py --prog="queens" --bp="TournamentBP" --bp_size="8192" --bp_bits="2"
#### You can change bp, bp_size, bp_bits three parameters and record CPI and other metrics.
