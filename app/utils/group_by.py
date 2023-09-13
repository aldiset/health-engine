from datetime import datetime

def group_data_by_created_at(data):
    grouped_data = []

    # Initialize dictionaries to hold health data and check-up history
    health_data_dict = {"data_kesehatan": []}
    check_up_history_dict = {"riwayat_periksa": []}

    for entry in data:
        for key, items in entry.items():
            for item in items:
            
                if key == "disease":
                    created_at_date = datetime.fromisoformat(item["created_at"]).date()
                    item_data = {"title": item["title"], "value": item["value"]}
                    if not health_data_dict["data_kesehatan"] or health_data_dict["data_kesehatan"][-1]["tanggal"] != created_at_date:
                        health_data_dict["data_kesehatan"].append({"tanggal": created_at_date, "data": []})
                    health_data_dict["data_kesehatan"][-1]["data"].append(item_data)

                elif key == "check_up_history":
                    created_at_date = datetime.fromisoformat(item["created_at"]).date()
                    check_up_history_dict["riwayat_periksa"].append(
                        {
                            "tanggal": created_at_date,
                            "nama_dokter": item["doctor_name"],
                            "diagnosis": item["diagnosis"],
                        }
                    )

    grouped_data.append(health_data_dict)
    grouped_data.append(check_up_history_dict)

    return grouped_data
