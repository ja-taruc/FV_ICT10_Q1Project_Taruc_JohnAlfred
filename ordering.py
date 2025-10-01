from pyscript import Element

def confirm_info(event=None):
    # Get customer info
    fname = Element("fname").value
    lname = Element("lname").value
    contact = Element("contactnum").value
    address = Element("address").value

    # Prices of menu items
    prices = {
        "Pinikpikan": 100,
        "Etag": 150,
        "Patupat": 50,
        "Rice": 99,
        "Soda In Can": 75
    }

    # Safe conversion for quantities
    def safe_int(value):
        try:
            return int(value)
        except:
            return 0

    # Menu items with checkboxes and quantities
    items = [
        ("Pinikpikan", "pinikpikan_check", "pinikpikan_qty"),
        ("Etag", "etag_check", "etag_qty"),
        ("Patupat", "patupat_check", "patupat_qty"),
        ("Rice", "rice_check", "rice_qty"),
        ("Soda In Can", "sic_check", "sic_qty")
    ]

    total = 0
    order_summary = ""

    for name, check_id, qty_id in items:
        checked = Element(check_id).element.checked
        quantity = safe_int(Element(qty_id).value)
        if checked and quantity > 0:
            subtotal = prices[name] * quantity
            total += subtotal
            order_summary += f"{name} x {quantity} = ₱{subtotal}<br>"

    if not order_summary:
        order_summary = "No items selected<br>"

    result = f"""
    <b>Customer Name:</b> {fname} {lname}<br>
    <b>Contact Number:</b> {contact}<br>
    <b>Address:</b> {address}<br><br>
    <b>Order Summary:</b><br>{order_summary}
    <b>Total Amount:</b> ₱{total}
    """

    # Update divs
    Element("result").element.innerHTML = result
    Element("status").element.innerHTML = "<span style='color:lightgreen;'>Order confirmed successfully!</span>"