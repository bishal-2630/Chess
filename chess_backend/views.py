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
    """Serve Flutter app - let Railway handle static files"""
    path = request.path.lstrip('/')
    
    print(f"DEBUG: Request path: {request.path}")
    print(f"DEBUG: Stripped path: {path}")
    
    if path == '' or path == '/':
        # Serve index.html for root path
        static_dir = Path(__file__).resolve().parent.parent / 'static'
        index_path = static_dir / 'index.html'
        print(f"DEBUG: Looking for index.html at: {index_path}")
        print(f"DEBUG: Index exists: {index_path.exists()}")
        
        if index_path.exists():
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"DEBUG: Serving index.html successfully")
            return HttpResponse(content, content_type='text/html')
        else:
            error_msg = f"Flutter app not found<br>Looking for: {index_path}"
            print(f"DEBUG: {error_msg}")
            return HttpResponse(error_msg, status=404)
    else:
        # For any other path, return 404 - Railway handles /static/ automatically
        return HttpResponse(f"Use /static/ for assets: {path}", status=404)
