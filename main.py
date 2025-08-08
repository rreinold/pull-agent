from fastapi import FastAPI

app = FastAPI()

@app.get("/api/{subagent_role}")
async def get_role(subagent_role: str):
    return {"role_name": subagent_role, "message": f"Hello, {subagent_role}!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
