import logging
from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    stream_url = url_for('static', filename='hls/stream.m3u8')
   
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Live Stream</title>
        <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
    </head>
    <body>
        <h2>Security Camera Stream</h2>
        <video id="video" controls autoplay muted></video>
        <script>
            var video = document.getElementById('video');
            if (Hls.isSupported()) {{
                var hls = new Hls();
                hls.loadSource('{stream_url}');
                hls.attachMedia(video);
                hls.on(Hls.Events.MANIFEST_PARSED, function() {{
                    video.play();
                }});
                hls.on(Hls.Events.ERROR, function(event, data) {{
                    console.log('HLS.js error:', data);
                }});
            }} else if (video.canPlayType('application/vnd.apple.mpegurl')) {{
                video.src = '{stream_url}';
                video.addEventListener('loadedmetadata', function() {{
                    video.play();
                }});
            }}
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)