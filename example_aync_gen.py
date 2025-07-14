"""
Using await means:

No unnecessary CPU waiting

Your program can do other tasks while this runs
"""
import asyncio
import time

# This is our async generator function
async def fetch_products():
    products = ["Shoes", "Laptop", "Phone", "Book", "Camera"]
    
    for product in products:
        await asyncio.sleep(1)  # simulate network/API delay
        yield f"Fetched product: {product}"

# This is how you consume it
async def main():
    async for item in fetch_products():
        print(item)

# Run the async code
asyncio.run(main())