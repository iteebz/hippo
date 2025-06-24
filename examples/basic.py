from mnemos import remember, recall

remember("Memory is all you need.", tags=["mnemos", "focus"])

results = recall("memory")
print(results[0].text)  # "Memory is all you need."