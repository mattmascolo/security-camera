# HLS Video Streaming with Flask

This project provides a simple setup to stream video using HLS (HTTP Live Streaming) and a lightweight Flask web server. It captures video using `libcamera-vid`, processes it with `ffmpeg`, and serves the stream over a local network through a Flask-based interface.

## Features

- **Live Video Capture**: Streams live video using `libcamera-vid`.
- **HLS Streaming**: Processes the video stream into HLS format for playback in browsers.
- **Flask Web Server**: Serves the HLS video stream with a simple HTML5 video player.
- **Responsive Cleanup**: Ensures processes are terminated gracefully when the script stops.

## Requirements

### Hardware
- Raspberry Pi or similar device with camera support.

### Software
- `libcamera-vid`
- `ffmpeg`
- Python 3.x
- Flask
- `hls.js` for video playback

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mattmascolo/security-camera.git
   cd https://github.com/mattmascolo/security-camera.git
   ```

2. Install Python dependencies:
   ```bash
   pip install flask
   ```

3. Ensure `libcamera-vid` and `ffmpeg` are installed:
   ```bash
   sudo apt install libcamera-apps ffmpeg
   ```

4. Run the script:
   ```bash
   ./start_stream.sh
   ```

5. Access the video stream in your browser:
   - Navigate to `http://<your-device-ip>:5000` in a browser on the same network.

## Project Structure

- `start_stream.sh`: Main script to initialize the video stream and Flask server.
- `stream_server.py`: Flask application for serving the HLS video stream.
- `static/hls/`: Directory where HLS video files are stored.

## Notes

- The video stream is served on port `5000` by default. Ensure this port is open on your device.
- This setup is intended for local network use. For external access, additional security measures should be implemented.
- The `debug=True` mode in Flask is enabled for development. Disable it in production for security.

## Troubleshooting

- **Video stream not loading**:
  - Ensure the camera is connected and properly configured.
  - Check that `libcamera-vid` and `ffmpeg` are installed and working.

- **Cannot access the stream in the browser**:
  - Confirm the IP address of your device and that it's reachable from the client device.
