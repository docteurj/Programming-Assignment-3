#!/bin/bash

TEST_DIR="q1-tests"
SCRIPT="source/main.py"

echo "--- Checking/Generating Expected Outputs ---"
for in_file in "$TEST_DIR"/*.in; do
    out_file="${in_file%.in}.out"
    if [ ! -f "$out_file" ]; then
        echo "Generating $out_file..."
        python "$SCRIPT" < "$in_file" > "$out_file"
    fi
done

echo -e "\n--- Running Tests ---"
FAIL_COUNT=0
for in_file in "$TEST_DIR"/*.in; do
    out_file="${in_file%.in}.out"
    
    if python "$SCRIPT" < "$in_file" | diff -q - "$out_file" > /dev/null; then
        echo "[PASS] $in_file"
    else
        echo "[FAIL] $in_file"
        echo "Diff details:"
        python "$SCRIPT" < "$in_file" | diff - "$out_file"
        FAIL_COUNT=$((FAIL_COUNT + 1))
    fi
done

if [ "$FAIL_COUNT" -eq 0 ]; then
    echo -e "\nAll tests passed successfully!"
else
    echo -e "\n$FAIL_COUNT test(s) failed. Check the diffs above."
    exit 1
fi