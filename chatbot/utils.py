# chatbot/utils.py
# from transformers import AutoModelForCausalLM, AutoTokenizer
from difflib import get_close_matches
# import torch

# model_name = "microsoft/DialoGPT-small"
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# Pad token set karo agar missing ho
# if tokenizer.pad_token is None:
#     tokenizer.pad_token = tokenizer.eos_token

# model = AutoModelForCausalLM.from_pretrained(model_name)

# FAQ dictionary: sawal aur jawab
FAQ = {
    "order kaise kare": "Cart mein product add karein, checkout par payment complete karein.",
    "return policy kya hai": "Product delivery ke 7 din ke andar return kiya ja sakta hai.",
    "payment methods": "Credit/debit card, UPI, wallets aur cash on delivery available hain.",
    "shipping time kitna hai": "Shipping generally 3-7 din ke andar hoti hai.",
    "account kaise banaye": "Register page par apna email aur password se account banayein.",
    "password reset kaise kare": "Login page par 'Forgot password' link se apna email daalein.",
    "customer support number kya hai": "Email help@stylesphere.com ya call 12345-67890 par karein.",
    "bulk order par discount milega": "Bulk orders par special discount available hai. Sales ko contact karein.",
    "gift wrapping available hai kya": "Checkout par gift wrapping ka option milega.",
    
    # Orders & Shipping
    "order kaise place kare": "Apne pasand ka product cart me add kar ke checkout karein.",
    "order track kaise kare": "Order confirmation email me tracking number diya jata hai, usse track kar sakte hain.",
    "shipping time kitna lagta hai": "Shipping generally 3-7 din me hoti hai.",
    "international shipping karte hain kya": "Haan, international shipping available hai. Shipping charge alag se lagega.",
    "shipping charges kya hain": "Shipping charges order value aur location par depend karte hain.",
    "order cancel kaise kare": "Order shipment se pehle cancel kiya ja sakta hai, customer support se contact karein.",
    "order deliver nahi hua toh kya karein": "Customer support se turant contact karein, hum aapki madad karenge.",

    # Payments & Refunds
    "payment method kya hain": "Credit/debit card, net banking, UPI, wallets aur COD available hain.",
    "payment secure hai kya": "Ha, hamari site SSL secured hai aur payment gateways bhi safe hain.",
    "refund policy kya hai": "Return ke baad refund 7-10 din me process ho jata hai.",
    "payment fail hua toh kya karein": "Payment fail hone par bank se contact karein ya customer support se sampark karein.",
    "cash on delivery available hai kya": "Haan, specific locations me COD available hai.",

    # Returns & Exchanges
    "return policy kya hai": "Product delivery ke 7 din ke andar return ya exchange kiya ja sakta hai.",
    "return kaise karein": "Customer support ko email karein ya return request form bharain.",
    "return charges kitne hain": "Return shipping charges location aur item par depend karte hain.",
    "damaged product mila toh kya karein": "Hume turant report karein, hum replacement ya refund denge.",

    # Account & Support
    "account kaise banaye": "Register page par apni email aur password se account bana sakte hain.",
    "password reset kaise karein": "Forgot password link par click karke email se reset kar sakte hain.",
    "account details update kaise karein": "Account settings me jaake apni details update karein.",
    "contact support kaise karein": "Email help@stylesphere.com ya phone 12345-67890 par sampark karein.",

    # Products & Offers
    "products ki quality kaisi hai": "Hamare products high quality ke hai, authentic brands se hain.",
    "bulk order par discount milta hai kya": "Haan, bulk orders par special discount milta hai.",
    "gift wrapping available hai kya": "Checkout par gift wrap option milega.",
    "latest offers kaise pata chalega": "Newsletter subscribe karein aur website par banner check karte rahein.",

    # Security & Privacy
    "mera data safe hai kya": "Bilkul, hamari privacy policy strict hai aur data secure rakha jata hai.",
    "privacy policy kya hai": "Hamari website me privacy policy page par detail me bataya gaya hai.",

    # Miscellaneous
    "delivery address change kaise kare": "Order shipment se pehle support team ko contact karen.",
    "invoice kaise milega": "Order confirmation email ke sath invoice bhi milega.",
    "return status kaise check kare": "Account me login karke ya customer support se pooch sakte hain.",
}

def get_chatbot_response(user_input):
    user_input_lower = user_input.lower()
    questions = list(FAQ.keys())

    # Fuzzy matching se best match dhundo
    matches = get_close_matches(user_input_lower, questions, n=1, cutoff=0.5)
    if matches:
        return FAQ[matches[0]]

    # FAQ me na mile to DialoGPT se response banao
    # inputs = tokenizer(user_input + tokenizer.eos_token, return_tensors="pt", padding=True)
    # input_ids = inputs["input_ids"]
    # attention_mask = inputs["attention_mask"]

    # chat_history_ids = model.generate(
    #     input_ids,
    #     attention_mask=attention_mask,
    #     max_length=100,
        # pad_token_id=tokenizer.pad_token_id,
    # )

    # response = tokenizer.decode(chat_history_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    # return response or "Mujhe maaf kijiye, main aapki baat samajh nahi paya."
