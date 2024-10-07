import controlPanel as control
import passwordManager as passManage

def show_banner():
    banner = """
            **********************************************
            *                                            *
            *          WELCOME TO SAKHASAFE              *
            *      Your Wisdom-Driven Security           *
            *                                            *
            **********************************************
        """
    print(banner)

if __name__ == "__main__":
    show_banner()    
    control.main()
    passManage.interface(control.username)

    input("Program sona erdi. Çıkmak için bir tuşa basın...")