set unstable
set script-interpreter := ['uv', 'run']

run:
    uvicorn main:app --reload
