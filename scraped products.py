import requests
from bs4 import BeautifulSoup
import csv

def scrape_amazon_products(url, num_pages=30):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    all_products = []
    for page in range(1, num_pages + 1):
        page_url = url + f'&page={page}'
        response = requests.get(page_url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch page {page}. Status Code: {response.status_code}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        product_listings = soup.find_all('div', {'data-component-type': 's-search-result'})

        for product in product_listings:
            product_data = {}

            # Extract ASIN
            asin = product.get('data-asin')
            product_data['ASIN'] = asin

            # Extract Product Description and Manufacturer
            product_desc_manufacturer = product.find('div', {'class': 'a-section a-spacing-none'})
            if product_desc_manufacturer:
                product_desc = product_desc_manufacturer.find('span', {'class': 'a-size-base-plus a-color-base'}).text.strip()
                product_data['Description'] = product_desc
                
                product_manufacturer = product_desc_manufacturer.find('span', {'class': 'a-size-base-plus a-color-secondary'}).text.strip()
                product_data['Manufacturer'] = product_manufacturer
            else:
                product_data['Description'] = 'Not available'
                product_data['Manufacturer'] = 'Not available'

            all_products.append(product_data)

    return all_products

if __name__ == "__main__":
    # List of URLs to scrape
    urls = [
        'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_',
        'https://www.amazon.in/s?k=shoes&crid=3H8XCLQJDMBW6&qid=1653311386&sprefix=shoes%2Caps%2C276&ref=sr_pg_',
        'https://www.amazon.in/s?k=earpods&crid=1J7PIQY6A3XWZ&sprefix=earpo%2Caps%2C236&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=mobiles&crid=PVW4K7BQWPKW&sprefix=mobile%2Caps%2C451&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=mens+cloths&crid=3BKG09NWTJ2PD&sprefix=mens+cloth%2Caps%2C518&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=iphones&crid=2Y8UDNATFX1HQ&sprefix=iphones%2Caps%2C316&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=redmi&crid=2G633XWWB5JZY&sprefix=redm%2Caps%2C333&ref=nb_sb_ss_ts-doa-p_2_4',
        'https://www.amazon.in/s?k=belts&crid=3IC7IWIHT83C6&sprefix=belts%2Caps%2C286&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=laptops&crid=1REOXPTQPIMDF&sprefix=laptops%2Caps%2C330&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=tvs&crid=2EW247FOB6HPV&sprefix=tv%2Caps%2C395&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=electronics&crid=1619S0R2YZ6A8&sprefix=electronic%2Caps%2C330&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=watches&crid=32M9BDUFYP870&sprefix=watche%2Caps%2C375&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=clocks&crid=35R1ETQF4JOTY&sprefix=clocks%2Caps%2C327&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=chairs&crid=VTXAX3F0VMUK&sprefix=chair%2Caps%2C310&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=tables&crid=1YT74N0DX4IZM&sprefix=table%2Caps%2C340&ref=nb_sb_noss_1',
        'https://www.amazon.in/American-Tourister-BACKPACK-COMPARTMENT-ORGANIZER/dp/B0BTD4S4XF/ref=sr_1_17?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%283&sr=8-17',    'https://www.amazon.in/Number-Backpack-Compartment-Charging-Organizer/dp/B09VTDMRY7/ref=sr_1_18?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%283&sr=8-18',
        'https://www.amazon.in/Wesley-Milestone-Waterproof-Backpack-Business/dp/B085S444JV/ref=sr_1_19?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-19',
        'https://www.amazon.in/GEAR-Black-Blue-Backpack-years/dp/B019HA8AYG/ref=sr_1_20?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-20',
        'https://www.amazon.in/TRUE-Emperor-Anti-Theft-backpack-charging/dp/B0BYB631NR/ref=sr_1_21?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-21',
        'https://www.amazon.in/LOOKMUSTER-Waterproof-Backpack-College-Business/dp/B0BZW8KW18/ref=sr_1_22?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-22',
        'https://www.amazon.in/Martucci-Casual-Travelling-Laptop-Backpack/dp/B088B4P6ZW/ref=sr_1_23?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-23',
        'https://www.amazon.in/NORTH-ZONE-Waterproof-Backpack-Dimensions/dp/B0BS6QM2GD/ref=sr_1_24?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-24',
        'https://www.amazon.in/Arctic-Fox-Liters-String-Backpack/dp/B08L6Q9V1H/ref=sr_1_25?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-25',
        'https://www.amazon.in/Rucksack-Travel-Backpack-Trekking-Compartment/dp/B07YDGQQN5/ref=sr_1_26?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-26',
        'https://www.amazon.in/ADISA-Laptop-Backpack-Office-College/dp/B09TPX22NF/ref=sr_1_27?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-27',
        'https://www.amazon.in/Half-Moon-Resistant-Backpack-Compartment/dp/B0BHX7GY16/ref=sr_1_28?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-28',
        'https://www.amazon.in/FATMUG-Laptop-Bag-Men-Convertible/dp/B084LF4RT5/ref=sr_1_29?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-29',
        'https://www.amazon.in/School-school-partition-Collage-Backpack/dp/B09NNYCQ1Q/ref=sr_1_30?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-30',
        'https://www.amazon.in/Bagneeds-Synthetic-Leather-Briefcase-Messenger/dp/B0855F8174/ref=sr_1_31?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-31',
        'https://www.amazon.in/POLESTAR-Vintage-Laptop-Backpack-bagpack/dp/B081GSQ9D9/ref=sr_1_32?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-32',
        'https://www.amazon.in/WALKENT-Premium-Support-Pockets-Elprine/dp/B0C7KP65DP/ref=sr_1_22_sspa?crid=2M096C61O4MLT&keywords=bags&qid=1690118919&sprefix=ba%2Caps%2C283&sr=8-22-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9idGY&psc=1',
        'https://www.amazon.in/Lenovo-15-6-Inches-Everyday-Backpack/dp/B08R7RPVJF/ref=sr_1_20?crid=2M096C61O4MLT&keywords=bags&qid=1690118919&sprefix=ba%2Caps%2C283&sr=8-20',
        'https://www.amazon.in/SAFARI-Ltrs-Casual-Backpack-DAYPACKNEO15CBSEB/dp/B07Q7CNPMV/ref=sr_1_18?crid=2M096C61O4MLT&keywords=bags&qid=1690118919&sprefix=ba%2Caps%2C283&sr=8-18',
        'https://www.amazon.in/Lunars-Bingo-Laptop-Resistant-48L/dp/B08YZ8FFBZ/ref=sr_1_16?crid=2M096C61O4MLT&keywords=bags&qid=1690118919&sprefix=ba%2Caps%2C283&sr=8-16',
        'https://www.amazon.in/s?k=suits+for+men&crid=331V4MT57LTJ&sprefix=suits%2Caps%2C319&ref=nb_sb_ss_ts-doa-p_4_5',
        'https://www.amazon.in/s?k=formal+pants+for+men&crid=H3S8ML21JAJX&sprefix=pats+for+men%2Caps%2C322&ref=nb_sb_ss_ts-doa-p_2_12',
        'https://www.amazon.in/s?k=camera&crid=1ZAQOUX3Y98DM&sprefix=camera%2Caps%2C357&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=canon&crid=2VQS3SH2RDR99&sprefix=canon%2Caps%2C306&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=printers&crid=3D9SY4C9ES79N&sprefix=printer%2Caps%2C312&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=musical+instrument&sprefix=musical%2Caps%2C253&ref=nb_sb_ss_ts-doa-p_1_7',
        'https://www.amazon.in/s?k=toys&crid=1JQR9PIDCJU4W&sprefix=toy%2Caps%2C288&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=cricket+bats&crid=2B245SEHQCK16&sprefix=cricket+ats%2Caps%2C436&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=refrigerator&crid=33Z496DK47T47&sprefix=refri%2Caps%2C392&ref=nb_sb_ss_ts-doa-p_2_5',
        'https://www.amazon.in/s?k=cooler+for+home&crid=RUJCABCCMEIO&sprefix=cool%2Caps%2C337&ref=nb_sb_ss_ts-doa-p_3_4',
        'https://www.amazon.in/s?k=rice+cooker&crid=3MMQRDBTD2A67&sprefix=rice+cooker+2+litre%2Caps%2C257&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=water+purifier+for+home&crid=N1087CZ5WXWV&sprefix=water+%2Caps%2C325&ref=nb_sb_ss_ts-doa-p_2_6',
        'https://www.amazon.in/s?k=mixer+grinder&crid=Y0QIJ3T659MU&sprefix=mix%2Caps%2C414&ref=nb_sb_ss_ts-doa-p_2_3',
        'https://www.amazon.in/s?k=grinder&crid=3BB5Z3XEHONI9&sprefix=mixer+grinder%2Caps%2C348&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=ac&crid=S7YXU97NPDS8&sprefix=a%2Caps%2C330&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=table+fans&crid=1NP78BHJNAUFP&sprefix=table+fan%2Caps%2C320&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=lights&crid=271KSJKLT7PEX&sprefix=light%2Caps%2C322&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=calenders&crid=3365J25Y3S8O4&sprefix=calender%2Caps%2C322&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=vivo&crid=28OQ7RWFNKHDH&sprefix=vivo%2Caps%2C309&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=adopter+changer&crid=7HPG0OXL30B5&sprefix=adop%2Caps%2C321&ref=nb_sb_ss_ts-doa-p_1_4',
        'https://www.amazon.in/s?k=heater&crid=19N63HV3668JS&sprefix=heate%2Caps%2C272&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=beds&crid=PRR4ABI84VM5&sprefix=bed%2Caps%2C305&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=helmets&crid=16Q4CEB51QFF2&sprefix=helmet%2Caps%2C317&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=bikes&crid=3TIZ8LKPJ9Z9&sprefix=bike%2Caps%2C393&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=cyc%3Bles&crid=1S0C4YDIAJBDE&sprefix=cyc+le%2Caps%2C335&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=weight+machines&crid=1XNGT46LODVPM&sprefix=weight+machine%2Caps%2C324&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=oppo&crid=3DAV6CWYS6CJ8&sprefix=opp%2Caps%2C454&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=realme&crid=23DBMUIAS45QO&sprefix=realm%2Caps%2C262&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=nokia&crid=1HYZEVDHZRBYK&sprefix=noki%2Caps%2C339&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=lava&crid=FJI88N1BX53V&sprefix=la%2Caps%2C338&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=whirpool&crid=1G4551UNXPTI4&sprefix=whirpoo%2Caps%2C298&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=battery+light&crid=1XUX2YJEDY7H3&sprefix=batter%2Caps%2C314&ref=nb_sb_ss_ts-doa-p_4_6',
        'https://www.amazon.in/s?k=invertors&crid=3Q49UMQ77GXKZ&sprefix=invertor%2Caps%2C289&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=sofas&crid=3HTJ3X5X4OIN4&sprefix=sofa%2Caps%2C331&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=spares&crid=1MKMJ9YDNT8IY&sprefix=spare%2Caps%2C328&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=power+banks&crid=2YOBG0KNWR9E8&sprefix=power+bank%2Caps%2C281&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=wireless+products&crid=1QFGNDXJTXNVR&sprefix=wireless+product%2Caps%2C282&ref=nb_sb_noss_2',
        'https://www.amazon.in/Qubo-Wireless-Doorbell-Instant-Intruder/dp/B08Y8KMQZ7/ref=sr_1_2_sspa?crid=1QFGNDXJTXNVR&keywords=wireless%2Bproducts&qid=1690314058&sprefix=wireless%2Bproduct%2Caps%2C282&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1',
        'https://www.amazon.in/s?k=instamart+groceries&crid=1HSCWMYFYF2OG&sprefix=insta+mart%2Caps%2C327&ref=nb_sb_ss_ts-doa-p_2_10',
        'https://www.amazon.in/s?k=interior+decoration+items&crid=1ISG6CZOJVESM&sprefix=interior%2Caps%2C305&ref=nb_sb_ss_ts-doa-p_1_8',
        'https://www.amazon.in/s?k=god+photos&crid=LI30ILBLE31P&sprefix=god+photo%2Caps%2C532&ref=nb_sb_noss_1',
        'https://www.amazon.in/dp/B07Y32TV19/ref=redir_mobile_desktop?_encoding=UTF8&aaxitk=5e06649cea411626e1d119d1e4a9030a&content-id=amzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d%3Aamzn1.sym.df9fe057-524b-4172-ac34-9a1b3c4e647d&hsa_cr_id=4371822110502&pd_rd_plhdr=t&pd_rd_r=6c7378c3-b262-4399-8328-a8ba232e38c0&pd_rd_w=YBGFe&pd_rd_wg=LvtW6&qid=1690314192&ref_=sbx_be_s_sparkle_mcd_asin_0_img&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&th=1',
        'https://www.amazon.in/dp/B0BXLG38L9/ref=sspa_dk_detail_3?psc=1&pd_rd_i=B0BXLG38L9&pd_rd_w=RRS4e&content-id=amzn1.sym.2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_p=2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_r=F3DE7CC2FXH3D0PWR86A&pd_rd_wg=8jnK3&pd_rd_r=6ff478de-aff9-4ffe-a71b-56cc6d33acd1&s=kitchen&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw',
        'https://www.amazon.in/s?bbn=4286663031&rh=n%3A3704992031%2Cn%3A%213704993031%2Cn%3A4286644031%2Cn%3A4286663031%2Cp_85%3A10440599031&pf_rd_i=4286644031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=d31afd9f-1046-4bcf-9e56-af4f5bd5e676&pf_rd_r=10T3XMEJ3BGC51ZW83G7&pf_rd_s=merchandised-search-5&pf_rd_t=101&ref=s9_acss_bw_cg_LawnGar_2c1_w',
        'https://www.amazon.in/IBELL-ED06-91-Speed-Electric-4200RPM/dp/B07PPSNDVB/ref=sr_1_8?pf_rd_i=4286644031&pf_rd_m=A1K21FY43GMZF8&pf_rd_p=d31afd9f-1046-4bcf-9e56-af4f5bd5e676&pf_rd_r=10T3XMEJ3BGC51ZW83G7&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1690314450&refinements=p_85%3A10440599031&rps=1&s=home-improvement&sr=1-8',
        'https://www.amazon.in/Hans-Lighting-Ceiling-Light-Blade/dp/B07GZ3XNJQ/ref=sr_1_23_sspa?crid=1ISG6CZOJVESM&keywords=interior+decoration+items&qid=1690314398&sprefix=interior%2Caps%2C305&sr=8-23-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1',
        'https://www.amazon.in/Qurox-Fancy-Casual-Laptop-Backpacks/dp/B0BX736B1G/ref=sr_1_2_sspa?keywords=bags&qid=1690314545&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1',
        'https://www.amazon.in/dp/B0BX73QBLX/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B0BX73QBLX&pd_rd_w=empZD&content-id=amzn1.sym.2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_p=2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_r=E507KFS81THS04TKJK0H&pd_rd_wg=eC8uH&pd_rd_r=1684069d-34fc-4490-bfb6-f4722adddc87&s=apparel&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw',
        'https://www.amazon.in/dp/B0C4PTT633/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B0C4PTT633&pd_rd_w=n8ZFo&content-id=amzn1.sym.2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_p=2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_r=C2EV8F9G6D9FHAGZYXBV&pd_rd_wg=zPUsa&pd_rd_r=aa58c9c2-8a6c-41d0-89a2-63d6ecf3ae73&s=apparel&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw',
        'https://www.amazon.in/AFN-FASHION-Casual-bagpack-Backpack/dp/B081X69ZL7/ref=pd_day0fbt_img_sccl_1/258-9138587-2426831?pd_rd_w=DRbZu&content-id=amzn1.sym.9fcd4617-323e-42b7-9728-3395e1b2fea0&pf_rd_p=9fcd4617-323e-42b7-9728-3395e1b2fea0&pf_rd_r=26KRX4KEP6N8GRV8QTBZ&pd_rd_wg=rSzYU&pd_rd_r=a5fee1f4-ac71-420e-870d-02c66fb0eb51&pd_rd_i=B081X69ZL7&psc=1',
        'https://www.amazon.in/dp/B09VCPS28Q/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B09VCPS28Q&pd_rd_w=5AeXu&content-id=amzn1.sym.2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_p=2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_r=AT31W501GC9E0MTZSVFB&pd_rd_wg=1wNtG&pd_rd_r=57b2d880-7919-4d0c-a843-54abf1976838&s=apparel&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw#customerReviews',
        'https://www.amazon.in/s?k=moto+mobiles&crid=1PY0BYMS6EEH0&sprefix=moto+mobile%2Caps%2C312&ref=nb_sb_noss_1',         'https://www.amazon.in/s?k=keyboards&crid=1JCZE9PWQCVOO&sprefix=keyboard%2Caps%2C320&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=screw+driver+tool+set+kit&crid=1Y02350RM284B&sprefix=screw%2Caps%2C318&ref=nb_sb_ss_ts-doa-p_1_5',
        'https://www.amazon.in/s?k=wallets&crid=RBMT2XW6NMAF&sprefix=wallet%2Caps%2C264&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=crocs&crid=2TZKM5PLCQNNQ&sprefix=croc%2Caps%2C272&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=sliders&crid=2LTB6DUNQKTYW&sprefix=slider%2Caps%2C350&ref=nb_sb_noss_1',             'https://www.amazon.in/s?k=sneakers&crid=3KCXC61BOVJ6F&sprefix=sneaers%2Caps%2C547&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=sandals+for+men&crid=VQ2B66W668NP&sprefix=sandals+for+men%2Caps%2C321&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=sandals+for+men&rh=n%3A1983519031&dc&ds=v1%3APpyQ14FBuwllMwEdHYHfPmaKAettbPSwtV6Ca9P4IXs&crid=VQ2B66W668NP&qid=1690314826&rnid=3576079031&sprefix=sandals+for+men%2Caps%2C321&ref=sr_nr_n_6',
        'https://www.amazon.in/Nike-Unisexs-Academy-Team-Sp21-University/dp/B08R7GMTYD/ref=sr_1_1?keywords=suitcases&qid=1690314944&s=shoes&sr=1-1&th=1',
        'https://www.amazon.in/dp/B08FX2W46Z/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B08FX2W46Z&pd_rd_w=njTBD&content-id=amzn1.sym.2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_p=2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_r=T3PKJ5HT83KE2VGD8PXF&pd_rd_wg=f9tAX&pd_rd_r=02791208-ce04-4ef4-83f5-ecb5606bbbbe&s=shoes&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw',
        'https://www.amazon.in/dp/B08FWY3ZV1/ref=sspa_dk_detail_1?pd_rd_i=B08FWY3ZV1&pd_rd_w=sWmZH&content-id=amzn1.sym.dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_p=dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_r=N1FTM5Y4NEWS7DG809DG&pd_rd_wg=oV8uy&pd_rd_r=d59d8d3d-8fda-4ddf-8096-8abd3ffae9b2&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFVNVY4SUVCMU9DU0gmZW5jcnlwdGVkSWQ9QTA2NTM1MjMyMTFUUklLMENQSkJBJmVuY3J5cHRlZEFkSWQ9QTA2Nzc5MTAxWjRWRklPWVpXMEtaJndpZGdldE5hbWU9c3BfZGV0YWlsX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1',
        'https://www.amazon.in/Stationary-Children-Stationery-Organizer-Students/dp/B0BTJCBKXT/ref=sr_1_7?crid=20S7ERFN86AUT&keywords=boys+things&qid=1690315038&s=luggage&sprefix=boys+thingg%2Cluggage%2C304&sr=1-7',
        'https://www.amazon.in/s?k=story+books&i=luggage&crid=3S106Q64M7IMK&sprefix=story+book%2Cluggage%2C250&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=gold+coin&i=jewelry&crid=1YC7RPVA09HWJ&sprefix=go%2Cjewelry%2C379&ref=nb_sb_ss_ts-doa-p_2_2',
        'https://www.amazon.in/s?k=bottles&i=jewelry&crid=UEPFYKA3Z39V&sprefix=botttles%2Cjewelry%2C276&ref=nb_sb_noss',
        'https://www.amazon.in/Personalized-Engraved-Stainless-Appreciation-Recognition/dp/B081PNQW28/ref=sr_1_4?crid=UEPFYKA3Z39V&keywords=bottles&qid=1690315156&s=jewelry&sprefix=botttles%2Cjewelry%2C276&sr=1-4&th=1',
        'https://www.amazon.in/dp/B0BT7MQZ25/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B0BT7MQZ25&pd_rd_w=GGLv9&content-id=amzn1.sym.dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_p=dcd65529-2e56-4c74-bf19-15db07b4a1fc&pf_rd_r=764NSGX4HS05WJ14HJ0H&pd_rd_wg=DPwmh&pd_rd_r=261d05df-6212-40ef-81c2-11d4dccd5511&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&smid=A32PAMSWP5EQ51&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFEWEg0UkJWUlc1N1ImZW5jcnlwdGVkSWQ9QTA5MDU4NzQxM0RRVVpYNDkwWEM0JmVuY3J5cHRlZEFkSWQ9QTAwMTU0ODIzMFpNS0VEOE82NjQ5JndpZGdldE5hbWU9c3BfZGV0YWlsX3RoZW1hdGljJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==',
        'https://www.amazon.in/dp/B0BT7S9J56/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B0BT7S9J56&pd_rd_w=o0eTV&content-id=amzn1.sym.2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_p=2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_r=0DB4H29BHX6V15KJ8DAJ&pd_rd_wg=vQbmA&pd_rd_r=bfa33760-853a-4e9c-8818-9bf6f57f167c&s=kitchen&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw',
        'https://www.amazon.in/ROZEN-partition-Collage-Backpack-NAVYBLUE/dp/B0BRTDQH8L/ref=pd_rhf_d_se_s_pd_sbs_rvi_sccl_2_1/258-9138587-2426831?pd_rd_w=hICFo&content-id=amzn1.sym.f2f99b52-a5ca-432b-8bfe-0d72feb3d1ba&pf_rd_p=f2f99b52-a5ca-432b-8bfe-0d72feb3d1ba&pf_rd_r=6HB309JZ7S38ATT89CSC&pd_rd_wg=Erofs&pd_rd_r=01d8bf08-ed61-4f76-85d6-b37155b8c203&pd_rd_i=B0BRT9Y4MR&th=1',
        'https://www.amazon.com/fire-tv-stick-4k-max-with-alexa-voice-remote/dp/B08MQZXN1X',
        'https://www.amazon.com/Bose-QuietComfort-Wireless-Headphones-Cancelling/dp/B079MFYL6X',
        'https://www.amazon.com/All-new-generation-International-Version-Charcoal/dp/B086FNYG8X',
        'https://www.amazon.com/Sony-WH-1000XM4-Wireless-Canceling-Headphones/dp/B08HDKHSSN',
        'https://www.amazon.com/dp/B07HGW8N7R/ref=shSac_dpClick_Asin_B07HGW8N7R',
        'https://www.amazon.com/s?k=carroms&crid=10CR93IUEDKV9&sprefix=carrom%2Caps%2C475&ref=nb_sb_noss_1',
        'https://www.amazon.com/s?k=shuttle+bats&crid=1GEU0FQ5VX8AN&sprefix=shuttle+bats+%2Caps%2C372&ref=nb_sb_noss_2',
        'https://www.amazon.com/s?k=football&sprefix=foot%2Caps%2C376&ref=nb_sb_ss_ts-doa-p_1_4',
        'https://www.amazon.com/s?k=volleyball&crid=BROXR27LX3NO&sprefix=vol%2Caps%2C425&ref=nb_sb_ss_ts-doa-p_1_3',
        'https://www.amazon.com/s?k=breaks&crid=1LEEK9FUDCO61&sprefix=break%2Caps%2C358&ref=nb_sb_noss_2',
        'https://www.amazon.com/s?k=tyres&crid=13ZCE8N90MW2Q&sprefix=tyre%2Caps%2C371&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=laptops&crid=1REOXPTQPIMDF&sprefix=laptops%2Caps%2C330&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=tvs&crid=2EW247FOB6HPV&sprefix=tv%2Caps%2C395&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=electronics&crid=1619S0R2YZ6A8&sprefix=electronic%2Caps%2C330&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=watches&crid=32M9BDUFYP870&sprefix=watche%2Caps%2C375&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=clocks&crid=35R1ETQF4JOTY&sprefix=clocks%2Caps%2C327&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=chairs&crid=VTXAX3F0VMUK&sprefix=chair%2Caps%2C310&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=tables&crid=1YT74N0DX4IZM&sprefix=table%2Caps%2C340&ref=nb_sb_noss_1',
        'https://www.amazon.in/American-Tourister-BACKPACK-COMPARTMENT-ORGANIZER/dp/B0BTD4S4XF/ref=sr_1_17?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%283&sr=8-17',    'https://www.amazon.in/Number-Backpack-Compartment-Charging-Organizer/dp/B09VTDMRY7/ref=sr_1_18?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%283&sr=8-18',
        'https://www.amazon.in/Wesley-Milestone-Waterproof-Backpack-Business/dp/B085S444JV/ref=sr_1_19?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-19',
        'https://www.amazon.in/GEAR-Black-Blue-Backpack-years/dp/B019HA8AYG/ref=sr_1_20?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-20',
        'https://www.amazon.in/TRUE-Emperor-Anti-Theft-backpack-charging/dp/B0BYB631NR/ref=sr_1_21?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-21',
        'https://www.amazon.in/LOOKMUSTER-Waterproof-Backpack-College-Business/dp/B0BZW8KW18/ref=sr_1_22?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-22',
        'https://www.amazon.in/Martucci-Casual-Travelling-Laptop-Backpack/dp/B088B4P6ZW/ref=sr_1_23?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-23',
        'https://www.amazon.in/NORTH-ZONE-Waterproof-Backpack-Dimensions/dp/B0BS6QM2GD/ref=sr_1_24?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-24',
        'https://www.amazon.in/Arctic-Fox-Liters-String-Backpack/dp/B08L6Q9V1H/ref=sr_1_25?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-25',
        'https://www.amazon.in/Rucksack-Travel-Backpack-Trekking-Compartment/dp/B07YDGQQN5/ref=sr_1_26?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-26',
        'https://www.amazon.in/ADISA-Laptop-Backpack-Office-College/dp/B09TPX22NF/ref=sr_1_27?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-27',
        'https://www.amazon.in/Half-Moon-Resistant-Backpack-Compartment/dp/B0BHX7GY16/ref=sr_1_28?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-28',
        'https://www.amazon.in/FATMUG-Laptop-Bag-Men-Convertible/dp/B084LF4RT5/ref=sr_1_29?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-29',
        'https://www.amazon.in/School-school-partition-Collage-Backpack/dp/B09NNYCQ1Q/ref=sr_1_30?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-30',
        'https://www.amazon.in/Bagneeds-Synthetic-Leather-Briefcase-Messenger/dp/B0855F8174/ref=sr_1_31?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-31',
        'https://www.amazon.in/POLESTAR-Vintage-Laptop-Backpack-bagpack/dp/B081GSQ9D9/ref=sr_1_32?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-32',
        'https://www.amazon.in/WALKENT-Premium-Support-Pockets-Elprine/dp/B0C7KP65DP/ref=sr_1_22_sspa?crid=2M096C61O4MLT&keywords=bags&qid=1690118919&sprefix=ba%2Caps%2C283&sr=8-22-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9idGY&psc=1',
        'https://www.amazon.in/Lenovo-15-6-Inches-Everyday-Backpack/dp/B08R7RPVJF/ref=sr_1_20?crid=2M096C61O4MLT&keywords=bags&qid=1690118919&sprefix=ba%2Caps%2C283&sr=8-20',
        'https://www.amazon.in/SAFARI-Ltrs-Casual-Backpack-DAYPACKNEO15CBSEB/dp/B07Q7CNPMV/ref=sr_1_18?crid=2M096C61O4MLT&keywords=bags&qid=1690118919&sprefix=ba%2Caps%2C283&sr=8-18',
        'https://www.amazon.in/Lunars-Bingo-Laptop-Resistant-48L/dp/B08YZ8FFBZ/ref=sr_1_16?crid=2M096C61O4MLT&keywords=bags&qid=1690118919&sprefix=ba%2Caps%2C283&sr=8-16',
        'https://www.amazon.in/s?k=suits+for+men&crid=331V4MT57LTJ&sprefix=suits%2Caps%2C319&ref=nb_sb_ss_ts-doa-p_4_5',
        'https://www.amazon.in/s?k=formal+pants+for+men&crid=H3S8ML21JAJX&sprefix=pats+for+men%2Caps%2C322&ref=nb_sb_ss_ts-doa-p_2_12',
        'https://www.amazon.in/s?k=camera&crid=1ZAQOUX3Y98DM&sprefix=camera%2Caps%2C357&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=canon&crid=2VQS3SH2RDR99&sprefix=canon%2Caps%2C306&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=printers&crid=3D9SY4C9ES79N&sprefix=printer%2Caps%2C312&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=musical+instrument&sprefix=musical%2Caps%2C253&ref=nb_sb_ss_ts-doa-p_1_7',
        'https://www.amazon.in/s?k=toys&crid=1JQR9PIDCJU4W&sprefix=toy%2Caps%2C288&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=cricket+bats&crid=2B245SEHQCK16&sprefix=cricket+ats%2Caps%2C436&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=refrigerator&crid=33Z496DK47T47&sprefix=refri%2Caps%2C392&ref=nb_sb_ss_ts-doa-p_2_5',
        'https://www.amazon.in/s?k=cooler+for+home&crid=RUJCABCCMEIO&sprefix=cool%2Caps%2C337&ref=nb_sb_ss_ts-doa-p_3_4',
        'https://www.amazon.in/s?k=rice+cooker&crid=3MMQRDBTD2A67&sprefix=rice+cooker+2+litre%2Caps%2C257&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=water+purifier+for+home&crid=N1087CZ5WXWV&sprefix=water+%2Caps%2C325&ref=nb_sb_ss_ts-doa-p_2_6',
        'https://www.amazon.in/s?k=mixer+grinder&crid=Y0QIJ3T659MU&sprefix=mix%2Caps%2C414&ref=nb_sb_ss_ts-doa-p_2_3',
        'https://www.amazon.in/s?k=grinder&crid=3BB5Z3XEHONI9&sprefix=mixer+grinder%2Caps%2C348&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=ac&crid=S7YXU97NPDS8&sprefix=a%2Caps%2C330&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=table+fans&crid=1NP78BHJNAUFP&sprefix=table+fan%2Caps%2C320&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=lights&crid=271KSJKLT7PEX&sprefix=light%2Caps%2C322&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=calenders&crid=3365J25Y3S8O4&sprefix=calender%2Caps%2C322&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=vivo&crid=28OQ7RWFNKHDH&sprefix=vivo%2Caps%2C309&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=adopter+changer&crid=7HPG0OXL30B5&sprefix=adop%2Caps%2C321&ref=nb_sb_ss_ts-doa-p_1_4',
        'https://www.amazon.in/s?k=heater&crid=19N63HV3668JS&sprefix=heate%2Caps%2C272&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=beds&crid=PRR4ABI84VM5&sprefix=bed%2Caps%2C305&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=helmets&crid=16Q4CEB51QFF2&sprefix=helmet%2Caps%2C317&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=bikes&crid=3TIZ8LKPJ9Z9&sprefix=bike%2Caps%2C393&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=cyc%3Bles&crid=1S0C4YDIAJBDE&sprefix=cyc+le%2Caps%2C335&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=weight+machines&crid=1XNGT46LODVPM&sprefix=weight+machine%2Caps%2C324&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=oppo&crid=3DAV6CWYS6CJ8&sprefix=opp%2Caps%2C454&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=realme&crid=23DBMUIAS45QO&sprefix=realm%2Caps%2C262&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=nokia&crid=1HYZEVDHZRBYK&sprefix=noki%2Caps%2C339&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=lava&crid=FJI88N1BX53V&sprefix=la%2Caps%2C338&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=whirpool&crid=1G4551UNXPTI4&sprefix=whirpoo%2Caps%2C298&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=battery+light&crid=1XUX2YJEDY7H3&sprefix=batter%2Caps%2C314&ref=nb_sb_ss_ts-doa-p_4_6',
        'https://www.amazon.in/s?k=invertors&crid=3Q49UMQ77GXKZ&sprefix=invertor%2Caps%2C289&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=sofas&crid=3HTJ3X5X4OIN4&sprefix=sofa%2Caps%2C331&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=spares&crid=1MKMJ9YDNT8IY&sprefix=spare%2Caps%2C328&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_',
        'https://www.amazon.in/s?k=shoes&crid=3H8XCLQJDMBW6&qid=1653311386&sprefix=shoes%2Caps%2C276&ref=sr_pg_',
        'https://www.amazon.in/s?k=earpods&crid=1J7PIQY6A3XWZ&sprefix=earpo%2Caps%2C236&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=mobiles&crid=PVW4K7BQWPKW&sprefix=mobile%2Caps%2C451&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=mens+cloths&crid=3BKG09NWTJ2PD&sprefix=mens+cloth%2Caps%2C518&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=iphones&crid=2Y8UDNATFX1HQ&sprefix=iphones%2Caps%2C316&ref=nb_sb_noss_2',
        'https://www.amazon.in/s?k=redmi&crid=2G633XWWB5JZY&sprefix=redm%2Caps%2C333&ref=nb_sb_ss_ts-doa-p_2_4',
        'https://www.amazon.in/s?k=belts&crid=3IC7IWIHT83C6&sprefix=belts%2Caps%2C286&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=laptops&crid=1REOXPTQPIMDF&sprefix=laptops%2Caps%2C330&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=tvs&crid=2EW247FOB6HPV&sprefix=tv%2Caps%2C395&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=electronics&crid=1619S0R2YZ6A8&sprefix=electronic%2Caps%2C330&ref=nb_sb_noss_1',
        'https://www.amazon.in/s?k=watches&crid=32M9BDUFYP870&sprefix=watche%2Caps%2C375&ref=nb_sb_noss_2',



    ]

    num_pages_to_scrape = 1
    all_products = []

    for url in urls:
        scraped_products = scrape_amazon_products(url, num_pages_to_scrape)
        all_products.extend(scraped_products)

    # Save the combined scraped data to a CSV file
    csv_filename = "products_file.csv"
    with open(csv_filename, mode='w', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['ASIN', 'Description', 'Manufacturer']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write the header row
        for product in all_products:
            writer.writerow(product)

    print(f"Scraped data has been written to {csv_filename}.")

