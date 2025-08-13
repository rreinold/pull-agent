set unstable
set script-interpreter := ['uv', 'run']

run:
    uvicorn pull_agent.main:app --reload

test:
    pytest
