import json

customer_problem = """
I am looking for somebody who knows how to use Leptos, a front-end framework for Rust.  https://leptos.dev/

We need a web app  that can integrate with a JS library https://github.com/gnaudio/jabra-browser-integration/tree/master

This library is used to interface with our telephone, which is provided by AWS (Amazon Connect).

The app needs three parts

1. User Authentication

2. A softphone interface provided by the library above

3. A user table that will show available users.  This data can be obtained from querying the Amazon Connect API - https://docs.aws.amazon.com/connect/latest/APIReference/API_ListAgentStatuses.html

4. Caller ID, which can be built by querying Salesforce, where we have a database of phone numbers.
"""

out = {"job_description": customer_problem}

output = json.dumps(out)