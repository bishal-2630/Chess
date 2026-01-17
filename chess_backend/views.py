"""
Django views for Chess Game API
"""
from django.http import HttpResponse
from pathlib import Path

def health_check(request):
    """Health check endpoint for Railway"""
    return HttpResponse("Chess Game API is running! ✅", content_type='text/plain')

def test_view(request):
    """Simple test view"""
    return HttpResponse("""
        <h1>Django is Working! 🎉</h1>
        <p><strong>Request path:</strong> {request.path}</p>
        <p><strong>Method:</strong> {request.method}</p>
        <p><strong>Static directory:</strong> {Path(__file__).resolve().parent.parent / 'static'}</p>
        <p><strong>Files in static:</strong></p>
        <ul>
    """.format(
        request=request,
        files="".join([f"<li>{f.name}</li>" for f in (Path(__file__).resolve().parent.parent / 'static').iterdir()])
    ), content_type='text/html')

def serve_flutter_app(request):
    """Serve Flutter app and its assets"""
    from django.http import FileResponse, Http404
    import mimetypes
    
    path = request.path.lstrip('/')
    
    # Root path - serve index.html
    if path == '' or path == '/':
        path = 'index.html'
    
    # Build full path to static file
    static_dir = Path(__file__).resolve().parent.parent / 'static'
    file_path = static_dir / path
    
    # Security check - ensure file is within static directory
    try:
        file_path = file_path.resolve()
        static_dir = static_dir.resolve()
        if not str(file_path).startswith(str(static_dir)):
            raise Http404("Invalid path")
    except:
        raise Http404("Invalid path")
    
    # Check if file exists
    if not file_path.exists() or not file_path.is_file():
        raise Http404(f"File not found: {path}")
    
    # Determine content type
    content_type, _ = mimetypes.guess_type(str(file_path))
    if content_type is None:
        content_type = 'application/octet-stream'
    
    # Serve the file
    return FileResponse(open(file_path, 'rb'), content_type=content_type)
