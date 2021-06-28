from scrapper import get_stock

# This is the link of google finance that we will scrap
link = "https://finance.google.com/"

# This will take the number of stocks that we want to take
num_stocks = int(input("Put the number of Stocks you want to know about: "))

# This is the array that we will store the stock names in
stocks = []

# This will take the stocks and store it into the stocks array
for i in range(num_stocks):
    stock = input("Put the Stock you want its Data: ")
    stocks.append(stock)

# This will start the script
if __name__ == "__main__":
    try:
        get_stock(link, stocks)

    except KeyboardInterrupt:
        print("\nGood Bye")

    except:
        print('This stock is not found\n')
