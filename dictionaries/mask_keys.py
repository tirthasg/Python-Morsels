def mask_keys(record, keys, mask_value="(MASKED)"):
    return {key: mask_value if key in keys else value for key, value in record.items()}


user_info = {"name": "Trey", "location": "San Diego", "secret": "I dislike nectarines"}
keys_to_mask = ["secret", "location"]
print(mask_keys(user_info, keys_to_mask))
