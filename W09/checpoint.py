with open('provinces.txt', "rt") as text_file:
        province_list = []
        for line in text_file:
            clean_line = line.strip()
            province_list.append(clean_line)    

        province_list.pop()
        print(province_list)
        count_coun = province_list.count("Alberta")
        print(count_coun)
        for i in range(len(province_list)):
            if province_list[i] == 'AB':
                province_list[i] = 'Alberta'
        province_list.pop(0)
        count_coun = province_list.count("Alberta")
        print(count_coun)