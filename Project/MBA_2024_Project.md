# [PY-P] Project - Barcelona restaurants in TripAdvisor

## Introduction

**TripAdvisor** is a US travel and restaurant website company that shows hotel and restaurant reviews, accommodation bookings and other travel-related content. Headquartered in Needham, Massachusetts. TripAdvisor is the largest "social travel website" in the world, with about 315 million reviewers (active and inactive) and about 500 million reviews of hotels, restaurants, attractions and other travel-related businesses. TripAdvisor was an early adopter of **user-generated content**. The website services are free to users, who provide most of the content, and the website is supported by a hotel booking facility and an advertising business model.

## Part 1: Credit card checks

Customers of TripAdvisor (reviewers, restaurants, etc.) often need to share payment details with them. TripAdvisor wants you to implement several functions to test that the information provided corresponds to valid payment information. When answering the following questions, provide the code and the execution of any tests you have done.

**Question 1:** Create a function `obtain_card_number` that asks the Python user to provide a credit card number, and then returns it. 

**Question 2** Create a function `validate_card_format` that returns `True` if a parameter `number` contains a number with 16 digits. Assume that the user will enter `number` as a string. If it helps you, assume that the first digit is never 0, and that there are no spaces in the card number. Do not use string methods we have not seen in our lectures.

**Question 3** Create a function `validate_card_number` that returns `True` if the number is a valid card number.

The last digit of a credit card number is a *check digit*, meaning that it's calculated from the rest using a formula (https://en.wikipedia.org/wiki/Luhn_algorithm). This means that if any digit is wrongly entered, the *check digit* won't match and the number is wrong. Here are the steps to calculate the check digit:

1. Remove the check digit from the card number. Example: 13573 -> 1357
2. Take the remaining digits. Starting from the rightmost digit, and moving left, every second digit is multiplied by two. Example: 1357 -> 7\*2, 5, 3\*2, 1 -> 14, 5, 6, 1
3. Sum the digits (or the digits of their doubles), and name it `s`. Example: 14, 5, 6, 1 -> 1+4+5+6+1 = 17
4. Calculate (10 - (s mod 10) ) mod 10. Remember the modulo function is calculated using the %, so 's mod 10' is `s%10`. Example: (10- (17 mod 10)) mod 10 = (10-7) mod 10 = 3

If calculation result from step 4 matches the last digit of the cart, it passes the check.

**Question 4**: Use the functions defined in questions 1 to 3 to define a new function `ask_and_check`. Use it to ask the user a credit card number and print on screen "VALID" or "INVALID" based on passing both of the format and check digit tests (questions 2 and 3 respectively). Note that even if you weren't able to complete the previous questions, you can still write the code for this one.

**Question 5:** Vectorize `validate_card_format` and `validate_card_number` and test them with the following numbers. Check that the result matches the expectated result, provided within the parenthesis.

- Number 1: 1234567890A23456 (Wrong Format)
- Number 2: 123456789013456  (Wrong Format)
- Number 3: 1234567890123456 (Right Format, Wrong Check Digit)
- Number 4: 1234567890123452 (Right Format, Right Check Digit)

When testing the numbers, if your function yields an error try modifying the code to avoid it. If you cannot, leave it with an error output and explain why it happens.

## Part 2: Restaurants in Barcelona
TripAdvisor proposals are grouped in different categories, such as *Hotels*, *Things to do*, *Restaurants*, *Flights*, etc. The data for this project have been scraped from the webpages devoted to Restaurants in Barcelona. The starting URL is `https://www.tripadvisor.com/Restaurants-g187497-Barcelona_Catalonia.html`. Note that `g187497` identifies Barcelona. Replacing `.com` by `.es`, you get the Spanish version. The information is about the same, but `tripadvisor.es` shows reviews on Spanish (some of them are automatic translations from English), while `tripadvisor.com` shows reviews in English.

The data have been captured in April, 2023. At that time, 8,662 restaurants from Barcelona were posted at `tripadvisor.com`. For this project, only the 450 top ranked restaurants have been selected. In this project you will analyze the TripAdvisor data set from three different points of view, each time using Python.

### The data set

In the source file `trip.csv`, every row corresponds to a restaurant. The columns are:

* `rank`, the current rank of the restaurant in TripAdvisor.

* `name`, the name of the restaurant as it appears in the TripAdvisor's URL's. Example: 'BelleBuon'.

* `id`, a unique identifier for the restaurant. This ID is expected to be found as part of the link to the restaurant, in the same way that the ID of Barcelona ('g187497') is found as part of the URL of the restaurants in Barcelona. Example: 'd12207253'.

* `bubble`, the number of bubbles that approximate the average rating of the restaurant. It comes as a multiple of 0.5.

* `reviewCount`, the total number of reviews for that restaurant.

* `priceRange`, with values 'Fine Dining', 'Mid-range' y 'Cheap Eats'. In the webpage, these categories are indicated with dollar symbols ('\$\$\$\$', '\$\$ - \$\$\$' and '\$', respectively).

* `claimed`, a True/False column indicating whether the restaurant's page displays the message "Claimed" on the right side of the restaurant's name. This message tells us that somebody from the business manages the listing.

* `travelers`, a True/False column indicating whether the restaurant has a **Traveler's Choice Award**.

* `photos`, the number of **photos** of that restaurant available at its website. It is shown in a link *See all (# photos)*.

* `thefork`, a True/False column indicating whether the restaurant has an option for **reserving a table** through TheFork.

* `justeat`, a True/False column indicating whether the restaurant has an option for **ordering online** to get food delivered by Just Eat.

* `cuisines`, a collection of **culinary options** placed in the *Details* section of the page, under the heading *CUISINES*. It may be missing. Example: 'Italian, Mediterranean, European, Northern-Italian, Southern-Italian'.

* `diets`, a collection of **dietary options** placed in the *Details* section, under the heading *SPECIAL DIETS*. It may be missing. Example: 'Vegetarian Friendly, Vegan Options, Gluten Free Options'.

* `meals`, a collection of **meal's options** placed in the *Details* section, under the heading *MEALS*. It may be missing. Example: 'Lunch, Dinner, Drinks'.

* `features`, a collection of **features** placed in the *Details* section, under the heading *FEATURES*. It may be missing. Example: 'Reservations, Outdoor Seating, Seating, Serves Alcohol, Full Bar, Free Wifi, Accepts Credit Cards, Table Service, Wine and Beer, Dog Friendly, Gift Cards Available'.

* `neigh`, the **neighborhood** where the restaurant is. It is placed in the *Location and contact* section. Example: 'El Baix Guinardo'.

* `excellent`, the number of reviews in English with rating 5.

* `verygood`, the number of reviews in English with rating 4.

* `average`, the number of reviews in English with rating 3.

* `poor`, the number of reviews in English with rating 2.

* `terrible`, the number of reviews in English with rating 1.

* `revEnglish`, the number of reviews in English.

* `revSpanish`, the number of reviews in Spanish.

### Questions

Answer the following questions, including the code you have used and its execution.

**Question 6:** Import the data to a Pandas data frame, with the restaurant ID as the index. Check the content.

**Question 7.** How is the distribution of the number of reviews? And the number of photos? Are they related?

**Question 8.** The proportion of reviews in foreign languages (i.e. not Spanish) can be used as an indicator of how "touristic" is a restaurant. Examine the distribution of this proportion. Is it related to the total number of reviews?

**Question 9.** Have more expensive restaurants a higher proportion of reviews in foreign languages?

**Question 10.** Does having dietary options make a difference in the price, the average rating or the number of reviews?
