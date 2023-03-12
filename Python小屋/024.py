def main():
    with open("data24.txt") as f:
        data = f.read()
    datas = data.split(",")
    return [int(i) * 10 for i in datas]
