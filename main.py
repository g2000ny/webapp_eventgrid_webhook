from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from datetime import datetime, timezone 
import jsonify 

app = FastAPI()

@app.post("/event-handler")
async def handle_event(request: Request):
    """
        Debatch event grid events and handle them 
    """
    event_payload = await request.json()
    all_events_handled = True 

    # Event Grid sends a subscription validation event when you create a subscription
    # This code handles the validation handshake
    for event in event_payload:
        if event['eventType'] == 'Microsoft.EventGrid.SubscriptionValidationEvent':
            validation_code = event['data']['validationCode']
            # To complete the validation, respond back with the validation code
            return JSONResponse(content={"validationResponse": validation_code})
    
        # else:
        #     all_events_handled = all_events_handled and handle_event_grid_data(event_payload)
        
    # Here you would add your code to handle the Event Grid events
    # print("Received Event:", event_payload)
    
    # Responding back to Event Grid with a 202 Accepted status code
    # if all_events_handled:
    #     return JSONResponse(content="good", status_code=status.HTTP_202_ACCEPTED)
    # else:
    #     return JSONResponse(content="not all events are handled", status_code=status.HTTP_202_ACCEPTED)
        
    return JSONResponse(content="good", status_code=status.HTTP_202_ACCEPTED)

async def handle_event_grid_data(data: dict) -> None: 
    return 




# @app.get("/eventgrid")
# async def handle_validation(validationCode: str):

#     now_st = datetime.now(timezone.utc).strftime("%Y-%m%d %H:%M:%S")
#     print(f"inside get read_root at:{now_st}")
#     # test_content = "calling from FastAPI"
#     return {"validationCode": validationCode}

# @app.route('/api/events', methods=['POST'])
# async def event_grid_listener(request: Request):
#     # Event Grid sends a subscription validation event when you create a subscription
#     # This code handles the validation handshake
#     event = await request.json()
#     if event[0]['eventType'] == 'Microsoft.EventGrid.SubscriptionValidationEvent':
#         validation_code = event[0]['data']['validationCode']
#         validation_url = event[0]['data']['validationUrl']
#         # To complete the validation, respond back with the validation code
#         return jsonify({
#             "validationResponse": validation_code
#         })
#     else:
#         # Handle other events here
#         print('Event received:', event)
#         # Your logic to handle the event data
#         return 'Event received', 202

# @app.post("/eventgrid")
# async def read_post(request: Request):
#     try:
#         now_st = datetime.now(timezone.utc).strftime("%Y-%m%d %H:%M:%S")
#         print(f"inside post read_root at:{now_st}")
        
#         event_data = await request.json()
#         print(f"event_data: {event_data}")

#         # test_content = "calling from FastAPI"
#         # return test_content
#         return {"message": f"msg received at: {now_st}"}
    
#     except Exception as e:
#         print(f"Error: {e}")
