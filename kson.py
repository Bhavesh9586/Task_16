import requests
import jmespath

# ----------------- Common Setup -----------------
product_id = "609849777"     # for product details
review_id = "494420036"      # for review stats

# ---------- Headers for both APIs ----------
headers_reviews = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'access-control-allow-origin': '*',
    'content-type': 'application/json',
    'jwt-token': 'null',
    'origin': 'https://www.jiomart.com',
    'priority': 'u=1, i',
    'referer': 'https://www.jiomart.com/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    'userid': '0',
    'vertical': 'jiomart',
}

cookies = {
    'nms_mgo_pincode': '400020',
    'nms_mgo_city': 'Mumbai',
    'nms_mgo_state_code': 'MH',
}

headers_product = {
    **headers_reviews,
    'x-requested-with': 'XMLHttpRequest',
    'sec-fetch-site': 'same-origin',
}

# ----------------- Fetch Review Data -----------------
review_url = f"https://reviews-ratings.jio.com/customer/op/v1/review/product-statistics/{review_id}"
response_review = requests.get(review_url, headers=headers_reviews)
review_data = response_review.json()

average_rating = jmespath.search("data.averageRating", review_data)
ratings_count = jmespath.search("data.ratingsCount", review_data)
rating_details = jmespath.search("data.ratingsCountDetails", review_data)

# ----------------- Fetch Product Data -----------------
product_url = f"https://www.jiomart.com/catalog/productdetails/get/{product_id}"
response_product = requests.get(product_url, headers=headers_product, cookies=cookies)
product_data = response_product.json()

product_name = jmespath.search("data.gtm_details.name", product_data)
brand = jmespath.search("data.gtm_details.brand", product_data)
seller = jmespath.search("data.seller_name", product_data)
mrp = jmespath.search("data.mrp", product_data)
price = jmespath.search("data.selling_price", product_data)
discount = jmespath.search("data.discount_pct", product_data)
availability = jmespath.search("data.availability_status", product_data)

# ----------------- Print All Results -----------------
print("\n--- Product Details ---")
print("Product Name:", product_name or "Not Available")
print("Brand:", brand or "Not Available")
print("Seller Name:", seller or "Not Available")
print("MRP:", mrp or "Not Available")
print("Selling Price:", price or "Not Available")
print("Discount (%):", discount or "Not Available")
print("Availability:", availability or "Not Available")

print("\n--- Review Statistics ---")
print("Average Rating:", average_rating or "Not Available")
print("Total Ratings:", ratings_count or "Not Available")

# Print star ratings using loop (1 to 5 stars)
if isinstance(rating_details, dict):
    for i in range(1, 6):
        count = rating_details.get(str(i), 0)
        print(f"{i}-Star Ratings:", count)
else:
    print("Star Ratings: Not Available")

#api2
print("mrp",mrp)
print("selling_price",price)
print("discount_pct",discount)
print("availability_status",availability)
print("data.gtm_details.name",product_name)
print("data.gtm_details.brand",brand)
print("data.seller_name",seller)

