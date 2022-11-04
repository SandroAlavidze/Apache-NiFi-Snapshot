import sys
from great_expectations import DataContext
context = DataContext(
    "/Users/sandroalavidze/Documents/Data Engineering/stagingValid/great_expectations")

my_checkpoint_name = "staging_checkpoint"

checkpoint_result = context.run_checkpoint(
    checkpoint_name=my_checkpoint_name,
)

if not checkpoint_result["_success"]:
    print('{"result":"fail"}')
    sys.exit(0)

print('{"result":"pass"}')
sys.exit(0)
