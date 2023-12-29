import pandas as pd

from api.tools.constants import MAPPING_OPERATIONS

operations = pd.DataFrame()

for main, detailed_operations in MAPPING_OPERATIONS.items():
    if detailed_operations is None:
        operations = pd.concat([operations, pd.DataFrame([main, None]).T])
    else:
        for detailed in detailed_operations:
            operations = pd.concat([operations, pd.DataFrame([main, detailed]).T])

operations.columns = ["main_operation", "detailed_operation"]
