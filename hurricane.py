# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def newDamages(listToCheck):
  newList = []
  for item in listToCheck:
    if item == 'Damages not recorded':
      newList.append('Damages not Recorded')
    elif 'B' in item:
      index = item.find('B')
      value = str(item[0:index])
      total = float(value) * 1000000000
      newList.append(total)
    elif 'M' in item:
      index = item.find('M')
      value = str(item[0:index])
      total = float(value) * 1000000
      newList.append(total)
    else:
      newList.append(str(item))
  return newList

testList = newDamages(damages)
print(testList)

# write your construct hurricane dictionary function here:
hurricane_dictionary = {}
for (a, b, c, d, e, f, g) in zip(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
      hurricane_dictionary[a] = {"name": a, "month": b, "year": c, "max_sustained_winds": d, "areas_affected": e, "damages": f, "deaths": g}

print(hurricane_dictionary)

# write your construct hurricane by year dictionary function here:
hurricane_dictionary_year = {}
for (a, b, c, d, e, f, g) in zip(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
      hurricane_dictionary_year[c] = {"name": a, "month": b, "year": c, "max_sustained_winds": d, "areas_affected": e, "damages": f, "deaths": g}

print(hurricane_dictionary_year)

# write your count affected areas function here:
def areaAffected(listToCheck):
  areaAffectedDict = {}
  for list in listToCheck:
    for item in list:
      if item in areaAffectedDict:
        areaAffectedDict[item] += 1
      else:
        areaAffectedDict[item] = 1
  return areaAffectedDict

hurricaneAffect = areaAffected(areas_affected)
print(hurricaneAffect)

# write your greatest number of deaths function here:
for key,values in hurricaneAffect.items():
  print("The most affected hurricane location " + key + " with a value of " + str(values))
  break

# write your catgeorize by mortality function here:
def numberOfDeaths(listToCheck):
  deathsDictionary = {}
  list_with_scales = []
  for item in listToCheck:
    if item == 0:
      list_with_scales.append(0)
    elif item <= 100:
      list_with_scales.append(1)
    elif item <= 500:
      list_with_scales.append(2)
    elif item <= 1000:
      list_with_scales.append(3)
    elif item <= 10000:
      list_with_scales.append(4)
    else:
      list_with_scales.append(5)
  for a,b in zip(names, list_with_scales):
    deathsDictionary[a] = b
  print(deathsDictionary)

numberOfDeaths(deaths)

# write your greatest damage function here:
def greatest_damage(list_check):
  new_cost_list = []
  for item in list_check:
    if item == 'Damages not recorded':
      new_cost_list.append(0)
    elif item[-1] == 'M':
      number = float(item[0:len(item)-1])
      final_number = number * 1000000
      new_cost_list.append(final_number)
    elif item[-1] == 'B':
      number = float(item[0:len(item)-1])
      final_number = number * 1000000000
      new_cost_list.append(final_number)
    else:
      new_cost_list.append(item)
  print(new_cost_list)
  highest = new_cost_list[0]
  for item in new_cost_list:
    if item > highest:
      highest = item
  print("The highest damage recorded was " + str(highest))
greatest_damage(damages)

# write your catgeorize by damage function here:
def categorize_damage(list_to_check):
  new_cost_list = []
  for item in list_to_check:
    if item == 'Damages not recorded':
      new_cost_list.append(0)
    elif item[-1] == 'M':
      number = float(item[0:len(item)-1])
      final_number = number * 1000000
      new_cost_list.append(final_number)
    elif item[-1] == 'B':
      number = float(item[0:len(item)-1])
      final_number = number * 1000000000
      new_cost_list.append(final_number)
    else:
      new_cost_list.append(item)
  categorize_damages_list = []
  for item in new_cost_list:
    if item == 0:
      categorize_damages_list.append(0)
    elif item < 100000000:
      categorize_damages_list.append(1)
    elif item < 1000000000:
      categorize_damages_list.append(2)
    elif item < 10000000000:
      categorize_damages_list.append(3)
    elif item < 50000000000:
      categorize_damages_list.append(4)
    else:
      categorize_damages_list.append(5)
  categorize_damages = {}
  for (a,b) in zip(names, categorize_damages_list):
    categorize_damages[a] = b
  print(categorize_damages)

categorize_damage(damages)