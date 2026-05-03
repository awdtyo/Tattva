#!/bin/bash
echo "Starting Automated Stress Test for Thermal Data Collection..."

# 1. Baseline (Idle) - 60 seconds
echo "Phase 1: Idle (Cooling down)..."
sleep 60

# 2. Medium Load (2 Cores) - 60 seconds
echo "Phase 2: Medium Load (50%)..."
timeout 60s yes > /dev/null & timeout 60s yes > /dev/null &
sleep 65

# 3. Full Load (All Cores) - 120 seconds
echo "Phase 3: High Load (100%)..."
timeout 120s yes > /dev/null & timeout 120s yes > /dev/null & 
timeout 120s yes > /dev/null & timeout 120s yes > /dev/null &
sleep 125

# 4. Recovery - 60 seconds
echo "Phase 4: Recovery..."
sleep 60

echo "Stress test complete."
