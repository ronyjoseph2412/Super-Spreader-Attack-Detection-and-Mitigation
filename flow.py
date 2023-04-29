
import grpc
from p4.v1 import p4runtime_pb2, p4runtime_pb2_grpc

# P4Runtime server address and port
server_address = 'localhost'
server_port = 50051

# Create a P4Runtime client
channel = grpc.insecure_channel('localhost:9090')
client = p4runtime_pb2_grpc.P4RuntimeStub(channel)

# Send a request to get the flow entries from the switch
request = p4runtime_pb2.ReadRequest()
request.device_id = 0
request.table_entry.CopyFrom(p4runtime_pb2.TableEntry())
request.table_entry.table_id = 0
request.table_entry.is_default_action = False

response = client.Read(request)

# Print the flow entries
for entity in response.entities:
    if entity.WhichOneof('entity') == 'table_entry':
        table_entry = entity.table_entry
        for match_field in table_entry.match:
            print("Match Field: ", match_field.field_id, "Value: ",match_field.exact.value)
        # for action in table_entry.action.action:
        #     print(f"Action Name: {action.action.name}")
        #     for param in action.params:
        #         print(f"Parameter: {param.param_id} Value: {param.value}")
        # print("Priority: {table_entry.priority}")
        # print(f"Is Default Entry: {table_entry.is_default_action}")
        # print(f"Cookie: {table_entry.cookie}")
        # print(f"Idle Timeout: {table_entry.idle_timeout}")
        # print(f"Hard Timeout: {table_entry.hard_timeout}")
