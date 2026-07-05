import subprocess
import json

def get_battery():
    try:
        result = subprocess.check_output(
            ["termux-battery-status"],
            text=True
        )

        data = json.loads(result)

        return (
            f"Battery {data['percentage']}% hai. "
            f"Status: {data['status']}."
        )

    except Exception as e:
        return f"Battery status nahi mil saka: {e}"
