from math import e


def dec_to_base(N, base):
    if not hasattr(dec_to_base, 'table'):
        dec_to_base.table = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x, y = divmod(N, base)
    return dec_to_base(x, base) + dec_to_base.table[y] if x else dec_to_base.table[y]


while True:
    try:
        while True:
            name = input("Введіть значення: ")
            general = []
            general_line = []
            char_list = []
            tenderloin = ""
            total = ""
            total_line = []
            for i in name:
                line = str(ord(i))
                general_line.append(line)
                n = int(line)
                general.append(n)
            print("Крок 1: ", name, " = ", general)
            arithmetic_mean = str(sum(general) // len(name))
            print("Крок 2: ", arithmetic_mean)
            for c in arithmetic_mean:
                char_list.append(c)
            num = -1
            while num < len(arithmetic_mean):
                num += 1
                for b in general_line:
                    if len(b) < len(arithmetic_mean):
                        m_index = general_line.index(b)
                        general_line.remove(b)
                        b = b + char_list[num]
                        general_line.insert(m_index, b)
            print("Крок 3: ", general_line)
            general.clear()
            char_list.clear()
            for ini in general_line:
                total += ini
            for u in total.replace("0", ""):
                total_line.append(u)
            gim = 0
            for h in total_line:
                h_index = total_line.index(h)
                d = int(h)
                total_line.remove(h)
                total_line.insert(h_index, d)
            sum_all = sum(total_line[:len(total_line):4])
            print("Крок 4: ", sum_all)
            for element in general_line:
                element_int = int(element)
                general.append(element_int)
            value = sum(general) // sum_all
            result = value % e
            print("Крок 5: ", result)
            result_str = str(result)
            removed = result_str.replace(".", "")
            lin_num = []
            for ele in removed[1:15]:
                lin_num.append(ele)
            if lin_num[0] == "0":
                lin_num.remove("0")
                lin_num.insert(0, str(value)[0])
            for var in lin_num:
                tenderloin = tenderloin + var
            print("Крок 6: ", tenderloin)
            print("Крок 7(Хеш): ", dec_to_base(int(tenderloin), 36))
    except KeyError:
        print("Неправильний ввід")
    except ValueError:
        print("Неправилльний ввід")
    except ZeroDivisionError:
        print("Ти нічого не ввів")
    except OverflowError:
        print("Дуже ввелике значення")
