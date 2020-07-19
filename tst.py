import tinvest
#from pydantic import BaseModel

TOKEN = "t.FeAhvntO9rW0Xez_WkisBwCr-yQ3mcPXfPh6zTzJcuULXWJ9mdoDpM7eROHzv-tTePBx8LLkSKJvxszjXhK2gw"

client = tinvest.SyncClient(TOKEN, use_sandbox=True)
api    = tinvest.SandboxApi(client)

response = api.sandbox_register_post(tinvest.SandboxRegisterRequest(broker_account_type=tinvest.BrokerAccountType.tinkoff))

if response.status_code == 200:
    print(response.parse_json())  # tinvest.PortfolioResponse

# Handle error

if response.status_code != 200:
    print(response.parse_error())  # tinvest.Error