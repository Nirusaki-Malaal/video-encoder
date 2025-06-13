#!/bin/bash

try() {
  for dir in downloads encodes temp; do
    if [ -d "$dir" ]; then
      rm -rf "$dir" || {
        echo "❌ Failed to remove $dir"
        return 1
      }
      echo "✅ Removed $dir"
    else
      echo "ℹ️  Directory '$dir' does not exist"
    fi
  done
}

catch() {
  echo "⚠️  Something went wrong during cleanup."
}

# Run the try-catch
try || catch



python3 -m bot
