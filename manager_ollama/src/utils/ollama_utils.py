from templates import templates

llama_version = "llama2:13b"


def extract_requirements(filtered_text):
    prompt = (
        "Get all core information about techinical System Requirements from this text:"
        + filtered_text
    )

    payload = {
        "model": llama_version,
        "prompt": prompt,
        "stream": False,
    }

    return payload


def generate_config(data):
    prompt = (
        "Considering the requirements:"
        + data
        + "<GENERATE_JSON> Create a JSON following rules:"
        + templates.get_rules()
        + "<FILL_JSON> Return only the json with this structure:"
        + templates.get_structure()
    )

    payload = {
        "model": llama_version,
        "prompt": prompt,
        "format": "json",
        "stream": False,
        "options": {
            "temperature": 0.2,
            "top_k": 0.2,
            "top_p": 0.9,
        },
    }

    return payload
