from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]


# Get all items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({"items": items})


# Get a specific item
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify({"item": item})
    return jsonify({"error": "Item not found"}), 404


# Create a new item
@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json(silent=True)
    if not data or "name" not in data:
        return jsonify({"error": "Field 'name' is required"}), 400
    new_id = max((item["id"] for item in items), default=0) + 1
    item = {"id": new_id, "name": data["name"]}
    items.append(item)
    return jsonify({"item": item}), 201


# Update an existing item
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    data = request.get_json(silent=True)
    if not data or "name" not in data:
        return jsonify({"error": "Field 'name' is required"}), 400
    item["name"] = data["name"]
    return jsonify({"item": item})


# Delete an item
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    items.remove(item)
    return jsonify({"message": "Item deleted"})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
