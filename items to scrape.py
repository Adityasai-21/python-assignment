import csv

# Sample scraped data (list of lists)
scraped_data = [
    ['Product URL', 'Product Name', 'Product Price(INR)', 'Rating', 'Number of reviews'],
    ['https://www.amazon.in/American-Tourister-BACKPACK-COMPARTMENT-ORGANIZER/dp/B0BTD4S4XF/ref=sr_1_17?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-17', 'American Tourister VALEX BLACK LAPTOP BACKPACK 28 Ltrs,Volume, LAPTOP COMPARTMENT, BOTTLE POCKET, FRONT ORGANIZER', '1,199', '4.3', '560'],
		['https://www.amazon.in/Number-Backpack-Compartment-Charging-Organizer/dp/B09VTDMRY7/ref=sr_1_18?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-18', 'FUR JADEN Anti Theft Number Lock Backpack Bag with 15.6 Inch Laptop Compartment, USB Charging Port & Organizer Pocket for Men Women Boys Girls', '679', '4.0', '4,920'],
		['https://www.amazon.in/Wesley-Milestone-Waterproof-Backpack-Business/dp/B085S444JV/ref=sr_1_19?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-19', 'Wesley Milestone 2.0 Casual Waterproof Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Travel Backpack (Dimensions:13x18 inches) (Compatible with 39.62cm(15.6inch laptop) 30 L, Charcoal black', '550', '4.3', '11,840'],
		['https://www.amazon.in/GEAR-Black-Blue-Backpack-years/dp/B019HA8AYG/ref=sr_1_20?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-20', 'Gear CarryOn 16L Foldable Water Resistant School Bag//Backpack/College Bag for Men/Women - Blue Black', '224', '3.7', '6,833'],
		['https://www.amazon.in/TRUE-Emperor-Anti-Theft-backpack-charging/dp/B0BYB631NR/ref=sr_1_21?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-21', 'TRUE HUMAN® Emperor Anti-Theft Pocket backpack With USB charging Port Laptop,office,college,travel bag for men and women(Epower)', '680', '3.6', '182'],
        ['https://www.amazon.in/LOOKMUSTER-Waterproof-Backpack-College-Business/dp/B0BZW8KW18/ref=sr_1_22?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-22', 'LOOKMUSTER 15.6 inch 30 L Casual Waterproof Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Unisex Travel Backpack', '439', '3.9', '33'],
	    ['https://www.amazon.in/Martucci-Casual-Travelling-Laptop-Backpack/dp/B088B4P6ZW/ref=sr_1_23?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-23','Martucci 15.6 inch 30 L Casual Waterproof Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Unisex Travel Backpack(Black)', '549', '3.9', '7,663'],
	    ['https://www.amazon.in/NORTH-ZONE-Waterproof-Backpack-Dimensions/dp/B0BS6QM2GD/ref=sr_1_24?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-24', 'NORTH ZONE Casual Waterproof Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Travel Backpack (Dimensions:13x18 inches) (Compatible with 39.62cm(15.6inch laptop) 30 L', '630', '4.0', '476'],
	    ['https://www.amazon.in/Arctic-Fox-Liters-String-Backpack/dp/B08L6Q9V1H/ref=sr_1_25?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-25', 'Arctic Fox 15 Liters Draw String Bag Lavender Backpack', '229', '4.3','3,390'],
	    ['https://www.amazon.in/Rucksack-Travel-Backpack-Trekking-Compartment/dp/B07YDGQQN5/ref=sr_1_26?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-26', 'Fur Jaden 55 LTR Rucksack Travel Backpack Bag for Trekking, Hiking with Shoe Compartment','849','4.3', '5,474' ],
	    ['https://www.amazon.in/ADISA-Laptop-Backpack-Office-College/dp/B09TPX22NF/ref=sr_1_27?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-27','ADISA 15.6 inch Laptop Backpack Office Bag College Travel Back Pack 32 Ltrs z-Navy Blue','549','3.9','1,016'],
	    ['https://www.amazon.in/Half-Moon-Resistant-Backpack-Compartment/dp/B0BHX7GY16/ref=sr_1_28?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-28','Half Moon Large 37L Laptop Bag Backpack for men Women Boys and Girls Lugggage Travel Bags with 17.3 inches Laptop Compartment & Rain Cover', '849','3.9','3,224'],
	    ['https://www.amazon.in/FATMUG-Laptop-Bag-Men-Convertible/dp/B084LF4RT5/ref=sr_1_29?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-29','FATMUG Laptop Bag For Men - Convertible Backpack For Office And Travel Dark Grey,Oxford Fabric','1,599',  '4.4', '2,170'],
	    ['https://www.amazon.in/School-school-partition-Collage-Backpack/dp/B09NNYCQ1Q/ref=sr_1_30?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-30', 'URBAN CARRIER School Bag For girls school bags for boys Class 5-10 Large 4 partition 45 L Laptop Collage Office Travel Unisex Backpack','431','3.5','953'],
	    ['https://www.amazon.in/Bagneeds-Synthetic-Leather-Briefcase-Messenger/dp/B0855F8174/ref=sr_1_31?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-31','Bagneeds Mens Black Synthetic Leather Briefcase Best Laptop Messenger Bag Satchel for Men','759','4.1','4,493'],
	    ['https://www.amazon.in/POLESTAR-Vintage-Laptop-Backpack-bagpack/dp/B081GSQ9D9/ref=sr_1_32?crid=2M096C61O4MLT&keywords=bags&qid=1690120030&sprefix=ba%2Caps%2C283&sr=8-32','POLESTAR Vintage 15.6 inch 32 LTR Casual Laptop Backpack/Office Bag/School Bag/College Bag/Business Bag/Unisex Backpack, Water Resistant and Light Weight, 1 year Warranty', '549','3.9', '9,028'],
	    ['https://www.amazon.in/WALKENT-Premium-Support-Pockets-Elprine/dp/B0C7KP65DP/ref=sr_1_22_sspa?crid=2M096C61O4MLT&keywords=bags&qid=1690118919&sprefix=ba%2Caps%2C283&sr=8-22-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9idGY&psc=1','WALKENT Waterproof Laptop Bag for Men with Side Bottle Pockets, Cushioned Straps & More P2','4,990','4.0','407'],
	    ['https://www.amazon.in/Lenovo-15-6-Inches-Everyday-Backpack/dp/B08R7RPVJF/ref=sr_1_20?crid=2M096C61O4MLT&keywords=bags&qid=1690118919&sprefix=ba%2Caps%2C283&sr=8-20', 'Lenovo 15.6" 39.62cm Slim Everyday Backpack, Made in India, Compact, Water-resistant, Organized storage:Laptop sleeve,tablet pocket,front workstation,2-side pockets,Padded adjustable shoulder straps', '839', '4.3', '3,713'],
	    ['https://www.amazon.in/SAFARI-Ltrs-Casual-Backpack-DAYPACKNEO15CBSEB/dp/B07Q7CNPMV/ref=sr_1_18?crid=2M096C61O4MLT&keywords=bags&qid=1690118919&sprefix=ba%2Caps%2C283&sr=8-18', 'Safari Compact Size 15 Ltrs Casual Backpack For Unisex Adult - Sea Blue', '248', '4.0', '20,013'],
	    ['https://www.amazon.in/Lunars-Bingo-Laptop-Resistant-48L/dp/B08YZ8FFBZ/ref=sr_1_16?crid=2M096C61O4MLT&keywords=bags&qid=1690118919&sprefix=ba%2Caps%2C283&sr=8-16', 'Lunars Bingo - 48 L Laptop Office/School/Travel/Business Backpack Water Resistant - Fits Up to 15.6 Inch Laptop Notebook with 1 Year Warranty', '899', '3.9', '9,897'],

]

# Specify the file name
csv_file_name = "scraped_data.csv"

# Open the CSV file in write mode
with open(csv_file_name, mode='w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Write the data to the CSV file row by row
    for row in scraped_data:
        csv_writer.writerow(row)

print(f"Data has been written to {csv_file_name} successfully.")
