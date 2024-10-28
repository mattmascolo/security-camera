#!/bin/bash

# Directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# HLS output directory
HLS_DIR="$SCRIPT_DIR/static/hls"

# Ensure the HLS directory exists
mkdir -p "$HLS_DIR"

# Start the streaming process
libcamera-vid -t 0 --inline --listen -o - | \
ffmpeg -i - \
-vf "vflip" \
-c:v libx264 -crf 23 -preset ultrafast \
-f hls \
-hls_time 4 \
-hls_list_size 0 \
-hls_flags delete_segments+append_list \
-hls_segment_filename "${HLS_DIR}/stream%d.ts" \
"${HLS_DIR}/stream.m3u8" &

# Store the PID of the streaming process
STREAM_PID=$!

# Start the Python web server
python3 "$SCRIPT_DIR/stream_server.py" &

# Store the PID of the Python process
PYTHON_PID=$!

# Function to clean up processes
cleanup() {
    echo "Cleaning up..."
    kill $STREAM_PID
    kill $PYTHON_PID
    exit
}

# Set up trap to call cleanup function on script exit
trap cleanup EXIT

# Wait for both processes
wait $STREAM_PID $PYTHON_PID