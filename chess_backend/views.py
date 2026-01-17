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
    """Serve Flutter app from static files"""
    path = request.path.lstrip('/')
    static_dir = Path(__file__).resolve().parent.parent / 'static'
    
    print(f"DEBUG: Request path: {request.path}")
    print(f"DEBUG: Stripped path: {path}")
    print(f"DEBUG: Static dir: {static_dir}")
    print(f"DEBUG: Static dir exists: {static_dir.exists()}")
    
    if path == '' or path == '/':
        # Serve index.html for root path
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
        # Try to serve static assets
        file_path = static_dir / path
        print(f"DEBUG: Looking for asset: {file_path}")
        print(f"DEBUG: Asset exists: {file_path.exists()}")
        
        if file_path.exists() and file_path.is_file():
            # Read file based on type
            if file_path.suffix.lower() in ['.html', '.htm', '.css', '.js']:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            else:
                with open(file_path, 'rb') as f:
                    content = f.read()
            
            # Set content type
            if file_path.suffix.lower() == '.js':
                content_type = 'application/javascript'
            elif file_path.suffix.lower() == '.css':
                content_type = 'text/css'
            elif file_path.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.ico']:
                content_type = 'image/*'
            elif file_path.suffix.lower() in ['.html', '.htm']:
                content_type = 'text/html'
            else:
                content_type = 'application/octet-stream'
            
            print(f"DEBUG: Serving asset: {path} with type: {content_type}")
            return HttpResponse(content, content_type=content_type)
        else:
            error_msg = f"Asset not found: {path}<br>Static dir: {static_dir}"
            print(f"DEBUG: {error_msg}")
            return HttpResponse(error_msg, status=404)
