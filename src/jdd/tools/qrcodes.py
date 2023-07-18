import qrcode
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

def make_qr(outdir):
    urls = input('Which URL(s) you want to create a QR code for ?\n'
                 "Please write each url separated with a comma\n"
                 "Like this : 'https://url1.com','https://url2.com\n").split(',')
    names = input('Provide the name you want to give to your qr_code files\n'
                  'Please separate each name with comma and give it as numerous as urls\n').split(',')
    assert len(urls) == len(names), 'ERROR : Not same number of urls and names !'
    print(f"{Fore.BLUE}Generating QR codes ....{Style.RESET_ALL}\n")
    for i in range(len(urls)):
        img = qrcode.make(urls[i])
        img.save(outdir + names[i] + ".png")
    print("Done")
    print(f"{Fore.GREEN}{Style.BRIGHT}QR code(s) generated under {outdir} directory{Style.RESET_ALL}\n")