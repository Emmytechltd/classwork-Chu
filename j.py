from twilio.rest import Client 
 
account_sid = 'AC9db87bf9310280c51dc1e87bd8460029' 
auth_token = '[Redacted]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(         
                              to='+2347067797360' 
                          ) 
 
print(message.sid)