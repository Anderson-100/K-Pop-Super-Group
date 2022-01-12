# Author: Anderson Hsiao
import os
import random

all_artists = []
user_supergroup = []

def main():
  member_count = int_input("How many members would you like in your group? (3-15): ", 3, 15)
  choice = int_input("Who would you like to include?\n1. Boy Groups\n2. Girl Groups\n3. Solo Artists\n4. All of the above\n", 1, 4)
  
  load_artists(choice)
  play_game(member_count)
  print_supergroup()

def int_input(message: str, range_min: int, range_max: int):
  while True:
    try:
      choice = int(input(message))
      if range_min <= choice <= range_max:
        break
      else:
        raise ValueError

    except ValueError:
      print(f"Error: Please enter an integer between {range_min} and {range_max}.")

  return choice

def load_artists(choice: int):
  print("Loading artists...")
  
  if choice == 1:
    parse_files(1)

  elif choice == 2:
    parse_files(2)

  elif choice == 3:
    parse_files(3)

  elif choice == 4:
    parse_files(1)
    parse_files(2)
    parse_files(3)
  
  print("Loading complete.")

def parse_files(folder: int):
  # boy groups
  if folder == 1:
    folder_name = "boy_groups" 

  elif folder == 2:
    folder_name = "girl_groups"

  elif folder == 3:
    folder_name = "solo_artists"

  folder_contents = os.listdir(folder_name)

  for file in folder_contents:
    with open(f"{folder_name}/{file}", "r") as f:

      group = f.readline()
      group = group[:-1]

      for artist in f:
        if "\n" in artist:
          all_artists.append((artist[:len(artist)-1], group))
        else:
          all_artists.append((artist, group))

  # print(all_artists)

def play_game(loops: int):
  for _ in range(loops):
    print()
    options = []
    for i in range(1,6):
      option = all_artists.pop(random.randint(0, len(all_artists)-1))
      options.append(option)
      print(f"{i}. {option}")
    
    choice = int_input("Enter your pick: ", 1, 5)

    # put the user's selection into their supergroup
    user_supergroup.append(options.pop(choice-1))

    # put the rest back into the list
    for artist in options:
      all_artists.append(artist)

def print_supergroup():
  print("\n\n\nYOUR SUPERGROUP:")
  for member in user_supergroup:
    print(member)

if __name__ == "__main__":
  main()