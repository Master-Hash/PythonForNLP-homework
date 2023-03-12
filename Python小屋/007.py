def main(lst: list[int]) -> list[int]:
    if len(lst) in (0, 1):
        return lst
    else:
        first = lst[0]
        t = main(list(filter(lambda x: x != first, lst[1:])))
        return [first, *t]


# if __name__ == "__main__":
#     print(main([2, 2, 3, 1, 1]))
