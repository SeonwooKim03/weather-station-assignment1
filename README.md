# weather-station-assignment1
Assignment 1 for Weather Station Pipeline architecture and sensor simulation

Sampler API Design
The Sampler component receives voltage readings from the Sensor and records sampled values. Communication between the Sensor and Sampler uses HTTPS and JSON data format.

Endpoint
POST /sample

Input JSON Example
{
  "voltage": 3.27,
  "timestamp": "2026-03-12T14:05:10Z"
}

Output JSON Example
{
  "status": "accepted",
  "sampledVoltage": 3.27
}

Design Explanation

The Sensor sends voltage readings to the Sampler using a POST request. The Sampler receives the JSON data, validates the voltage value, and records the sampled reading. 
JSON and HTTPS were chosen because they are widely supported and make the system easy to integrate with other components in the Weather Station pipeline.
