def main():
    ext = input("File name : ").lower().strip()
    print(open_file(ext),end ="")


def open_file(input):
    match input.split(".")[-1]:
        case "gif" | "png" :
            return "image/" + input.split(".")[-1]
        case "pdf" | "zip":
            return "application/"+input.split(".")[-1]
        case "txt":
            return "text/plain"
        case "jpeg" | "jpg" :
             return "image/jpeg"
        case _:
            return "application/octet-stream"





main()
