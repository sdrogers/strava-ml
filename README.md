# strava-ml
Strava ML Playground


# Setup

Install dependencies

`pip install -r requirements.txt`

Insert the relevant secret values into `config.ini`. You will need:

```ini
[DEFAULT]
client_id=12345
client_secret=ab4544395dshaasjas
```

Run the web app with

`uvicorn main:app --reload`

(omit the reload if you're not changing the codebase)