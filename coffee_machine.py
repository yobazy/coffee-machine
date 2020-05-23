cash = 550
water = 400
milk = 540
beans = 120
cups = 9

while cups != 0:
    print('Write action (buy, fill, take, remaining, exit):')
    choice = input()
    if choice == 'buy':
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        coffeeType = input()
        if coffeeType != 'back':
          if coffeeType == '1':
              waterNeed = 250
              milkNeed = 0
              beansNeed = 16
              cost = 4
          elif coffeeType =='2':
              waterNeed = 350
              milkNeed = 75
              beansNeed = 20
              cost = 7
          elif coffeeType =='3':
              waterNeed = 200
              milkNeed = 100
              beansNeed = 12
              cost = 6
          water = water - waterNeed
          milk = milk - milkNeed
          beans = beans - beansNeed
          cash = cash + cost
          cups -= 1
          mats = {'water':water,
                  'milk':milk,
                  'beans':beans,
                  'cups':cups}
          for key, value in mats.items():
            if 0 >= value:
              x = key
          if water<=0 or milk<=0 or beans<=0 or cups<=0:
            print("Sorry, not enough "+str(x)+"!")
            print()
            water = water + waterNeed
            milk = milk + milkNeed
            beans = beans + beansNeed
            cash = cash - cost
            cups += 1
          else:
            print("I have enough resources, making you a coffee!")
            print()

    elif choice == 'fill':
        print("Write how many ml of water to add:")
        waterAdd = int(input())
        print("Write how many ml of milk to add:")
        milkAdd = int(input())
        print("Write how many g of coffee beans to add:")
        beansAdd = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cupsAdd = int(input())
        water += waterAdd
        milk += milkAdd
        beans += beansAdd
        cups += cupsAdd
        print()

    elif choice == 'take':
        print("I gave you "+ str(cash))
        cash = 0

    elif choice == 'remaining':
        print()
        print("The coffee machine has:")
        print(str(water) + (" of water"))
        print(str(milk) + (" of milk"))
        print(str(beans) + (" of coffee beans"))
        print(str(cups) + (" of disposable cups"))
        print("$"+str(cash)+" of money")
        print()

    elif choice == 'exit':
      cups=0
