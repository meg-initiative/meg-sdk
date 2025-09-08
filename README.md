# MEG Compliance SDK
![MEG Logo](https://github.com/meg-initiative/meg/blob/main/meg_logo.png)

This repository contains the official Software Development Kit (SDK) and middleware for the [**Minimal Ethical Governance (MEG) Protocol**](https://github.com/meg-initiative/meg).

Our goal is to make MEG compliance as simple as possible. The **MEG Quickstart Middleware** is a drop-in solution that makes any AI model **Level 1 (Bronze) Compliant** with just a few lines of code.

---

### Quickstart: Become MEG Bronze Compliant in 5 Minutes

#### For Python:
```python
# 1. Install the library
pip install meg-compliance

# 2. Wrap your model's generation function
from meg_compliance import MEG_Bronze_Wrapper

def my_ai_function(prompt):
  # Your existing AI logic here...
  response = "This is a response from the AI."
  return response

# This is now a MEG-compliant function!
compliant_ai_function = MEG_Bronze_Wrapper(my_ai_function, engine_name="MyAI_v1.0")

# Use it as you normally would
user_prompt = "Hello, world!"
response = compliant_ai_function(user_prompt)

# Audit logs are automatically created in the default location
