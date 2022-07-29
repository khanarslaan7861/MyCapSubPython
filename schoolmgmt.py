import csv


def write_csv(s_info_l):
    with open('s_info.csv', 'a', newline='') as csv_file:
        write = csv.writer(csv_file)
        if csv_file.tell() == 0:
            write.writerow(("Name", "Age", "Contact", "Email"))
        write.writerow(s_info_l)


if __name__ == "__main__":
    m_info = True
    s_num = 1
    while m_info:
        inf = ["Name", "Age", "Contact", "Email"]
        s_info = input(f"Enter student info for student #{s_num} (Name:Age:Contact:Email): ")
        s_info_list = s_info.split(':')
        print("Entered info: ")
        for i in range(len(s_info_list)):
            print(f'{inf[i]}: {s_info_list[i]}')
        check = input("Confirm Input?: (yes/no): ").lower()
        if check == "yes":
            write_csv(s_info_list)
            m_info_check = input("Enter info for other student? (yes/no): ").lower()
            if m_info_check == "yes":
                s_num += 1
                m_info = True
            elif m_info_check == "no":
                m_info = False
        elif check == "no":
            print("Please re-enter your information ")
