import hashlib


def json_to_sha256_with_salt(json_obj, salt):
    try:
        request_str = str(json_obj)
        request_str = request_str.replace("\'", "\"")
        request_str = request_str.replace(" ", "")

        request_hash = hashlib.sha256(request_str.encode("utf-8") + salt.encode("utf-8")).hexdigest()

        return request_hash
    except Exception as ex:
        print('Error: SHA256_generator: ', ex)
        return ""



