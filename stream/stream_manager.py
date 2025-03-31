# stream/stream_manager.py

from stream.simulated_stream import SimulatedStream
from stream.api_stream import APIPollingStream

def get_stream(source_type="simulated", **kwargs):
    if source_type == "simulated":
        return SimulatedStream(kwargs["df"], kwargs.get("delay", 0)).stream()

    elif source_type == "api":
        return APIPollingStream(kwargs["fetch_fn"], kwargs.get("polling_interval", 60)).stream()
    elif source_type == "websocket":
        return WebSocketStream(kwargs["url"], ...)

    else:
        raise ValueError(f"Unsupported stream type: {source_type}")
