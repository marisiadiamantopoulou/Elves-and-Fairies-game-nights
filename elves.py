gamers = []

def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print('Missing information')

ravenna = {
    'name': "Ravenna Alani" ,
    'availability': ['Monday', 'Tuesday', 'Friday']
}
add_gamer(ravenna, gamers)


add_gamer({'name':'Rosita Malena','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Krystian Rein','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Marilyn Nicol','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Mary Ann','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Marcelina Bellamy', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Jude Vassilis','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Stefanos Samuel','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Dean Cándido','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Panagiota Gwenda','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
print(gamers)

def build_daily_frequency_table():
    return {
        "Monday":    0,
        "Tuesday":   0,
        "Wednesday": 0,
        "Thursday":  0,
        "Friday":    0,
        "Saturday":  0,
        "Sunday":    0,
    }
count_availability = build_daily_frequency_table()

def count_night_availability(gamers_list, availability_table):
    for gamer in gamers_list:
        for day in gamer['availability']:
            availability_table[day] += 1

# Initialize the availability table
count_availability = build_daily_frequency_table()

# Call the function to count availability
count_night_availability(gamers, count_availability)

# Print the availability counts for each night
for day, count in count_availability.items():
    print(f"{day}: {count} gamers available")

def find_best_night(availability_table):
    best_night = None
    max_attendance = -1  # Initialize with a negative value

    for day, count in availability_table.items():
        if count > max_attendance:
            max_attendance = count
            best_night = day

    return best_night

# Find the best night
best_night = find_best_night(count_availability)

if best_night:
    print(f"The best night for game night is {best_night} with {count_availability[best_night]} gamers available.")
else:
    print("No gamers are available on any night.")

def available_gamers_for_best_night(gamers_list, day):
    list_of_available_people = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            list_of_available_people.append(gamer)
    return list_of_available_people

attending_game_night = available_gamers_for_best_night(gamers, best_night)
print(attending_game_night)

form_email = """
Dear {name},
The Aurora Comics and Games is happy to host "{game}" night and wishes you will attend. Come by on {day_of_week} and have a blast!

Magically Yours,
the Aurora Comics and Games"""

def send_email(gamers_who_can_attend,  day,  game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name = gamer['name'], day_of_week=day , game=game))

send_email(attending_game_night, best_night, 'Elves and Fairies')

# Create a list of gamers who cannot attend on the best night
unable_to_attend_best_night = [gamer for gamer in gamers if best_night not in gamer['availability']]
print(unable_to_attend_best_night)

# Create a dictionary to store alternative night availability counts
alternative_night_counts = build_daily_frequency_table()

# Count availability for alternative nights for gamers who cannot attend on the best night
count_night_availability(unable_to_attend_best_night, alternative_night_counts)

# Find the alternative night with the most availability
alternative_night = find_best_night(alternative_night_counts)

if alternative_night:
    print(f"Alternative night with the most availability: {alternative_night} with {alternative_night_counts[alternative_night]} gamers available.")
else:
    print("No alternative nights with availability.")

available_second_game_night = available_gamers_for_best_night(gamers, alternative_night)
send_email(available_second_game_night, alternative_night, "Elves and Fairies!")