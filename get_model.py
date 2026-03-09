import requests

def get_active_model_port():
    url = "http://localhost:8080/v1/models"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        for model in data.get("data", []):
            args = model.get("status", {}).get("args", [])
            if "--port" in args:
                port_index = args.index("--port") + 1
                port_value = args[port_index]
                if port_value != "0":
                    return port_value
        return 0
    except Exception:
        return 0

if __name__ == "__main__":
    print(get_active_model_port())
