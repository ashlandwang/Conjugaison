import CSVImporter
import random


__dict = CSVImporter.import_csv()

# INPUT: dict0
# OUTPUT：Array [infinitive， conjugaison]


def update_now(typec):

    # 变位类型标志转换
    ind = 0
    if typec == "Indicatif Présent":
        ind = 5
    elif typec == "Participe Présent":
        ind = 2
    elif typec == "Participe Passé":
        ind = 3
    elif typec == "Indicatif Imparfait":
        ind = 11
    elif typec == "Indicatif Passé Simple":
        ind = 17
    elif typec == "Indicatif Futur Simple":
        ind = 23
    elif typec == "Conditionnel Présent":
        ind = 29
    elif typec == "Subjonctif Présent":
        ind = 35
    elif typec == "Subjonctif Imparfait":
        ind = 41
    elif typec == "Impératif Présent":
        ind = 47



    dict0 = __dict

    if ind > 4:
        verbe = random.choice(dict0)
        p = verbe[ind:ind + 6]
        pv = []
        for i in range(0, 6):
            if p[i] != "":
                pv.append(i)
        pn = random.choice(pv)
        print(p, pv, pn)
        qa = [verbe[0], p[pn], pn]
    else:
        verbe = random.choice(dict0)
        qa = [verbe[0], verbe[ind]]
        print(qa)

    # print(qa[0], qa[1])
    return qa


