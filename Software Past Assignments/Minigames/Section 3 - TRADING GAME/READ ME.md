# READ ME - IMPORTANT INFORMATION

---

> ***DEVELOPER FEATURE: SIR, IF YOU ARE LOOKING TO GET MORE CREDITS TO TEST THE GAME WITHOUT HAVING TO DO THE HARD WORK, THERE IS A 5x5 PIXEL ZONE FROM 0,0 TO 5,5 IN THE TOP RIGHT CORNER WHER IF YOU CLICK WHIST ON AN EARTH YOU WILL GET AN ADITIONAL 1,000 CREDITS (THIS FEATURE DOES NOT EXPIRE).***


> WHEN BEGIING THE GAME, EVERY NOW AND THEN (UNCONTROLALY) PYGAME DECIDES THAT THE FONT IN THE FOLDER DOESN'T EXIST EVEN AS IT IS IN THE FOLDER, THIS IS A PYGAME BUG NOT A FANDOM TRADE BUG WHICH I HAVE REPORTED AND PYGAME WILL LOOK INTO FIXING.

> IF YOU LEAVE THE GAME RUNNING AND CHANGE DESKTOPS OR DO NOT INTERACT FOR A PERIOD OF TIME, TERMINAL CALLS "ABORT TRAP 6" TO CLOSE THE PROGRAM AS IT IS IN A LOOP AND DOESN'T WANT TO BREAK THE COMPUTER, THIS IS UNAVOIDIBLE AND HAPPEN AS IT IS NOT A FULLY EXPORTED APP AND IS RATHER RUNNING THROUGH TERMINAL WHICH HAS SAFE GUARDS WHICH DON'T RECOGISE THAT YOU HAVE JUST LEFT THE GAME FOR A BIT.

---

## Infinity Stones

##### Use infinity stones by clicking on them, different stones have different refresh rates, abilities and ways to unlock them, see below. If the game is closed, the progress collecting infinity stones will disapere, and Thanos will steal any infinity stones you had, this means you quest to unlock the stones must begin again!

### Power (Purple)
###### Unlock: Get 50 or more of a singe stock
###### Ability: Gives you one of each stock on current earth

### Space (Blue)
###### Unlock: Get 750 credits
###### Ability: Allows travel through the multiverse

### Time (Green)
###### Unlock: Get 2,000 credits
###### Ability: Pauses stock prices for a short amount of time

### Reality (Red)
###### Unlock: Get 20,000 credits
###### Ability: Randomises all stock prices on current earth

### Soul (Orange)
###### Unlock: Travel to Earth-616
###### Ability: Raises stock prices by aprox 5 dollars

### Mind (Yellow)
###### Unlock: Travel to Earth-12
###### Ability: Lowers stock prices by aprox 5 dollars

---

## Components

### Game Components

###### Buy, Sell and Inventory Managment: Fandom Trade has a buy sell interface that displays the quantity of stocks of companies as well as their prices. Beyond that, a file named amount.txt is written on when a stock is bought which is read when displaying the stock amount, and saved automatically for ease of a choice to load back up the game after closure.

###### Banking (Money Managment): A bank is accesable and present in the multiverse for loans and repayments. The bank stores your credits in a file called credits.txt and debt in a file called debt.txt that are witten on when a change is made such as a loan, repayment, sale or purchase.

###### Economy (Trade Paths): The econony in my game is vastly complex and stretches over 7 unique earths. Each earth and product has its own different stock fluxuations upon major news. Specific earths are optimal for different parts of the game as some earths have cheaper stocks while others have more expensive stocks. For the player, better trade routes at the begining of the game might be to be on low stock priced earths while later on, you may develop into higher priced earths.

###### Random Events: Several random events are imbeded in the game. Breaking News is the main random event as from a base of around a hundered custom news bullitens, there is a chance one will happen, and when this happens, the stocks of companies effected on the current earth may alter drastically. Different random fluxuations of the prices from the news will happen when a news story breaks. Other random events such as the random fluxuation of prices of stocks and luck of the draw market plummets and spikes also occur mid-game.


### Components of Developers Choice (Just Some)

###### Infinity Stones
> 6 Different Unique Power Ups (Components)

###### Multiverse

###### Load Game (Saved Game)

###### Customised Breaking News Headlines for each earth and company (Multiple)
> Changes Stock Price based on news

###### Loan Rejection (specific built formulae to caculate loan rejection based on in-game credits and accumulated debt