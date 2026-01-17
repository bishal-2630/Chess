"""
Django views for serving Flutter app
"""
from django.http import HttpResponse
from pathlib import Path

def serve_flutter_app(request):
    """Serve the Flutter app"""
    path = request.path.lstrip('/')
    base_dir = Path(__file__).resolve().parent.parent
    
    # Serve assets (JS, CSS, images)
    if path and path != '':
        file_path = base_dir / path
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
            
            return HttpResponse(content, content_type=content_type)
        else:
            return HttpResponse(f"Asset not found: {path}", status=404)
    
    # Serve main HTML for root path
    index_path = base_dir / 'index.html'
    if index_path.exists():
        with open(index_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return HttpResponse(html_content, content_type='text/html')
    else:
        return HttpResponse("Flutter app not found", status=404)
