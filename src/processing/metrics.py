def compute_metrics(data):
    total_items = len(data)

    completed = [d for d in data if d.get("status") == "Done"]
    in_progress = [d for d in data if d.get("status") == "In Progress"]

    return {
        "total_items": total_items,
        "completed": len(completed),
        "in_progress": len(in_progress),
        "raw_data": data[:10]
    }