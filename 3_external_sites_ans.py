import sys
import collections

sites = collections.defaultdict(set)
for filename in sys.argv[1:]:
    for line in open(filename):
        i = 0
        while True:
            site = None
            # Ищет строку с http:// в строчке файла, возвращает индекс где найдено, и -1, если не найдено
            i = line.find("http://", i)
            # Если строка найдена
            if i > -1:
                i += len("http://")
                for j in range(i, len(line)):
                    # isalnum проверяет состоит ли строка только из цифр и букв
                    if not (line[j].isalnum() or line[j] in ".-"):
                        site = line[i:j].lower()
                        break
                if site and "." in site:
                    sites[site].add(filename)
                i = j
            else:
                break

for site in sorted(sites):
    print("{0} is referred to in:".format(site))
    for filename in sorted(sites[site], key = str.lower):
        print("    {0}".format(filename))