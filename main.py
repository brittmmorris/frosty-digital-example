from fastapi import FastAPI
from frosty_ai import Frosty
from dotenv import load_dotenv
import os

load_dotenv()

router_id = os.getenv("ROUTER_ID")
router_key = os.getenv("ROUTER_KEY")

frosty_sdk = Frosty(router_id, router_key)

app = FastAPI()

@app.get("/")
async def test_chat():
    try:
        chat_result = frosty_sdk.chat(
            [{"role": "user", "content": "tell me a 10 word joke about the weather"}]
        )
        return {"chat": chat_result}
    except Exception as e:
        return {"error": str(e), "type": str(type(e))}
