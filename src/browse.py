from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from playwright.sync_api import sync_playwright

playwright_manager = sync_playwright().start()
browser = playwright_manager.chromium.launch(headless=False)
page = browser.new_context().new_page()

class RequestHandler(BaseHTTPRequestHandler):
    
    def respond(self, http_code, content):
        self.send_response(http_code)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(content)
    
    def do_GET(self):
        query = parse_qs(urlparse(self.path).query)
        target_url = query.get('url', [None])[0]
        if not target_url: return
        
        try:
            page.goto(target_url)
            page.wait_for_selector('html', timeout=10000)
            text = page.locator('body').inner_text()
            response_text = f"browsing: {target_url}\ntitle: {page.title()} text: {text}"
            self.respond(200, response_text.encode('utf-8'))
        except Exception as e:
            self.respond(500, f"browsing failed: {str(e)}".encode('utf-8'))

def run():
    server = HTTPServer(('localhost', 0), RequestHandler)
    print(f"Server running. Check: http://localhost:{server.server_port}/?url=https://example.com")
    
    try:
        server.serve_forever()
    finally:
        browser.close()
        playwright_manager.stop()
        server.server_close()

if __name__ == "__main__":
    run()
