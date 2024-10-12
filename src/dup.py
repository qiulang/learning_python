import difPy
if __name__ == '__main__':
    dif = difPy.build("./img")
    search = difPy.search(dif, similarity="similar")
    print(search.result)
