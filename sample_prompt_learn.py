# Create a test file called test_sample_prompts.py
# Copy this entire code and run: python test_sample_prompts.py

# First, let's create a mock PROMPTS dictionary (like the one imported in the real code)
PROMPTS = {
    "generate_image": [
        "Create a beautiful artwork of",
        "Generate a stunning image showing", 
        "Make an artistic representation of",
        "Design a creative visual of"
    ],
    "edit_image": [
        "Modify this image to show",
        "Enhance the photo by adding"
    ],
    "virtual_try_on": [
        "Show the person wearing this product"
    ],
    "empty_mode": [],  # Empty list
    "none_mode": None  # This will test our safety mechanism
}

# Now let's define the sample_prompts function
def sample_prompts(mode: str, count: int | None = None):
    """Return up to `count` prompts for a mode (all if count is None).
    Safeguards against IndexError if prompt lists are shortened.
    """
    print(f"\n🔍 Called sample_prompts(mode='{mode}', count={count})")
    
    # Step 1: Get the prompt list safely
    plist = PROMPTS.get(mode, []) or []
    print(f"   Step 1: PROMPTS.get('{mode}', []) = {PROMPTS.get(mode, [])}")
    print(f"   After 'or []': plist = {plist}")
    print(f"   Length of plist: {len(plist)}")
    
    # Step 2: Check conditions
    if count is None or count >= len(plist):
        print(f"   Step 2: count is None? {count is None}")
        print(f"   Step 2: count >= len(plist)? {count >= len(plist) if count is not None else 'N/A'}")
        print(f"   ✅ Returning entire list: {plist}")
        return plist
    
    # Step 3: Slice the list
    result = plist[:count]
    print(f"   Step 3: plist[:{count}] = {result}")
    print(f"   ✅ Returning sliced list: {result}")
    return result

# TEST CASES - Run each one and see the output!

print("=" * 60)
print("🧪 TESTING SAMPLE_PROMPTS FUNCTION")
print("=" * 60)

# Test Case 1: Normal case - get some prompts
print("\n📝 TEST 1: Get 2 prompts from 'generate_image'")
result1 = sample_prompts("generate_image", 5)
print(f"📤 RESULT: {result1}")

# # Test Case 2: Get all prompts (count=None)
# print("\n📝 TEST 2: Get ALL prompts from 'generate_image' (count=None)")
# result2 = sample_prompts("generate_image", None)
# print(f"📤 RESULT: {result2}")

# # Test Case 3: Ask for more than available
# print("\n📝 TEST 3: Ask for 10 prompts but only 4 exist")
# result3 = sample_prompts("generate_image", 10)
# print(f"📤 RESULT: {result3}")

# # Test Case 4: Mode doesn't exist
# print("\n📝 TEST 4: Non-existent mode")
# result4 = sample_prompts("non_existent_mode", 2)
# print(f"📤 RESULT: {result4}")

# # Test Case 5: Empty mode
# print("\n📝 TEST 5: Empty mode (exists but empty list)")
# result5 = sample_prompts("empty_mode", 2)
# print(f"📤 RESULT: {result5}")

# # Test Case 6: None value mode (tests the 'or []' safety)
# print("\n📝 TEST 6: Mode with None value")
# result6 = sample_prompts("none_mode", 2)
# print(f"📤 RESULT: {result6}")

# # Test Case 7: Count is 0
# print("\n📝 TEST 7: Count is 0")
# result7 = sample_prompts("generate_image", 0)
# print(f"📤 RESULT: {result7}")

# # Test Case 8: Exact match (ask for exactly what's available)
# print("\n📝 TEST 8: Ask for exactly 2 from 'edit_image' (which has 2)")
# result8 = sample_prompts("edit_image", 2)
# print(f"📤 RESULT: {result8}")

# print("\n" + "=" * 60)
# print("🎯 SUMMARY OF WHAT WE LEARNED:")
# print("=" * 60)
# print("✅ Function NEVER crashes, even with bad inputs")
# print("✅ Returns empty list [] for non-existent modes")  
# print("✅ Returns all prompts when count=None")
# print("✅ Returns all prompts when count > available")
# print("✅ Safely slices list when count < available")
# print("✅ Handles edge cases like empty lists and None values")

# # BONUS: Show the actual PROMPTS dictionary
# print(f"\n📋 Original PROMPTS dictionary:")
# for key, value in PROMPTS.items():
#     print(f"   '{key}': {value}")