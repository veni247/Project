from Chap8_info1 import Laptop

def main():
    pc1 = Laptop(brand="ASUS", model="ASUS Vivobook X509JP-EJ013T", year=2019, storage=512)
    pc2 = Laptop(brand="Acer", model="Acer Nitro Gaming AN515-57-5669", year=2021, storage=512)
    
    print(pc1.display_info())
    print(pc2.display_info())
    
    pc1.upgrade_storage(256)
    pc2.upgrade_storage(256)
    
    print(pc1)
    print(pc2)
    
if __name__ == "__main__":
    main()
