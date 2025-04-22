from fastapi import FastAPI
from frosty_ai import Frosty

router_id = 'fa672a52-baf2-419f-9eae-e6e87ca61dc9'
router_key = 'b1b613e6-fa0c-411d-8fc7-5776a3c4a4be'

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
