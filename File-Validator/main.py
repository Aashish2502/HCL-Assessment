import os

# First define the Allowed file types with their signatures(magic numbers), allowed maximum size of the file, and their corresponding extensions.

ALLOWED_FILE_TYPES = {
    "jpg": {"signature": ["FFD8FF"], "max_size": 5 * 1024 * 1024, "extensions":[".jpg",".jpeg"]},  # 5 MB
    "png": {"signature": ["89504E47"], "max_size": 5 * 1024 * 1024, "extensions":[".png"]},  # 5 MB
    "pdf": {"signature": ["25504446"], "max_size": 10 * 1024 * 1024, "extensions":[".pdf"]},  # 10 MB
}

# Read the file signature by reading the unique sequences of bytes at the beginning of a file.

def read_signature(file_path):
    try:
        with open(file_path,'rb') as file:
            signature = file.read(8).hex().upper()
        return signature
    except Exception as e:
        return (f"Error while reading the signature {e}")
        

## Validate the signature using the allowed file types and return the file type.

def validate_signature(signature):
    for file_type, props in ALLOWED_FILE_TYPES.items():
        for sign in props["signature"]:
            if signature.startswith(sign):
                return file_type
    return None

# Validate the extensions
def validate_extention(file_path, valid_file_type):
    extention = (os.path.splitext(file_path))[1]
    
    allowed_extention = ALLOWED_FILE_TYPES[valid_file_type]["extensions"]
    return extention in allowed_extention

## Validating the uploaded file using the functions defined above.

def validate_uploaded_file(file_path):

    # Check if file does exist or not
    if not os.path.exists(file_path):
        return "Error: No file exist."
    
    # Read the signature:
    file_sign = read_signature(file_path)
    if not file_sign:
        return "Error: Unable to read signature."
    
    # Validate the signature
    valid_file_type = validate_signature(file_sign)
    if not valid_file_type:
        return ("Error: Unsupported file type. Please upload the coorect file.")
    

    # Check the size limit of the file
    size = os.path.getsize(file_path)
    max_size = ALLOWED_FILE_TYPES[valid_file_type]["max_size"]

    if size==0:
        return "Error: Empty File."
    elif size> max_size:
        return f"Error: Exceeded the allowed size for {valid_file_type} (max: {max_size/(1024*1024)} MB)."
    
    # Cehck the file extention:
    file = os.path.basename(file_path)
    if not validate_extention(file, valid_file_type):
        return "Error: File extension does not match."
    
    return "File Uploaded successfully."


   
if __name__=="__main__":

    print(validate_uploaded_file("Aashish_Waghmare_Resume.pdf"))
    print(validate_uploaded_file('IMG_20220403_022831.jpg'))

