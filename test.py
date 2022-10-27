from serpapi import GoogleSearch

params = {
    "q": "Apple",
    "tbm": "isch",
    "ijn": "0",
    "api_key": "3ae0dc0bfe0ebfcc7474a2574e94bcdd3a41c49b89036da9fc2dbab590f5ebf3",
}

search = GoogleSearch(params)
results = search.get_dict()
images_results = results["images_results"]
