FROM python:3.12

RUN pip install uv

WORKDIR /code

COPY ./pyproject.toml /code/pyproject.toml

RUN uv sync

COPY ./pull_agent /code/pull_agent
COPY ./subagents /code/subagents

EXPOSE 5000/tcp
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:5000/status || exit 1

CMD ["uv","run", "uvicorn", "pull_agent.main:app","--host", "0.0.0.0", "--port", "5000"]