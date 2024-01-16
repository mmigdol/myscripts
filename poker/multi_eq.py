import os
import argparse
import json

# Function to calculate equity for Day 2 in dollars
def calculate_equity_in_dollars(average_stack_in_bb, my_stack_in_bb, total_prize_pool, players_remaining):
    # Calculate equity in dollars based on your stack in BB
    print(f"calculate_equity_in_dollars: average_stack_in_bb={average_stack_in_bb}, my_stack_in_bb={my_stack_in_bb}, total_prize_pool={total_prize_pool}")
    Equity_In_Dollars = my_stack_in_bb / average_stack_in_bb * total_prize_pool / players_remaining
    return Equity_In_Dollars

# Function to calculate total current prize pool
def calculate_total_prize_pool(Total_Entries, Buy_In):
    Total_Prize_Pool = Total_Entries * Buy_In
    return Total_Prize_Pool

# Function to calculate total chips in play
def calculate_total_chips_in_play(Total_Entries, Starting_Stack):
    Total_Chips_In_Play = Total_Entries * Starting_Stack
    return Total_Chips_In_Play

# Function to calculate average stack size in BB
def calculate_average_stack_in_bb(Total_Entries, Starting_Stack, Remaining_Players, Big_Blind_Day2):
    Average_Stack_In_BB = (Total_Entries * Starting_Stack) / Remaining_Players / Big_Blind_Day2
    return Average_Stack_In_BB

# Function to calculate how many BB you have
def calculate_bb_you_have(S_Day2, Big_Blind_Day2):
    BB_You_Have = S_Day2 / Big_Blind_Day2
    return BB_You_Have

# Function to save inputs to a file
def save_inputs_to_file(filename, input_data):
    print("save_inputs_to_file")
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(json.dumps(input_data, indent=4))

# Function to parse command-line arguments
def parse_command_line_args():
    parser = argparse.ArgumentParser(description="Calculate poker equity for Day 2")
    parser.add_argument("-i", action="store_true", help="Prompt for input instead of using defaults")
    return parser.parse_args()

def calculate_equity_from_data(data):
    S_Day2 = data.get('S_Day2')
    Big_Blind_Day2 = data.get('Big_Blind_Day2')
    Total_Entries = data.get('Total_Entries')
    Starting_Stack = data.get('Starting_Stack')
    Remaining_Players = data.get('Players_Start_Day2')
    Buy_In = data.get('Buy_In')

    # Calculate total chips in play
    Total_Chips_In_Play = calculate_total_chips_in_play(Total_Entries, Starting_Stack)
    print(f"Total_Chips_In_Play: {Total_Chips_In_Play}")

    # Calculate total prize pool
    Total_Prize_Pool = calculate_total_prize_pool(Total_Entries, Buy_In)
    print(f"Total_Prize_Pool: {Total_Prize_Pool}")

    # Calculate average stack size in BB
    Average_Stack_In_BB = calculate_average_stack_in_bb(Total_Entries, Starting_Stack, Remaining_Players, Big_Blind_Day2)

    # Calculate how many BB you have
    BB_You_Have = calculate_bb_you_have(S_Day2, Big_Blind_Day2)

    # Calculate equity in dollars based on your stack in BB
    Equity_In_Dollars = calculate_equity_in_dollars(Average_Stack_In_BB, BB_You_Have, Total_Prize_Pool, Remaining_Players)

    result = {
        "Average_Stack_In_BB": Average_Stack_In_BB,
        "BB_You_Have": BB_You_Have,
        "Equity_In_Dollars": Equity_In_Dollars
    }
    return result

def main():
    args = parse_command_line_args()
    # Default input values
    default_filename = "poker_equity_inputs.json"
    default_data = {
        "S_Day2": 22751,
        "Big_Blind_Day2": 1200,
        "Total_Entries": 5539,
        "Starting_Stack": 4000,
        "Buy_In": 15,
        "Players_Start_Day2": 452,
        "Expected_Day_One_Flight_Stack_Result": 9000,
    }

    data = default_data

    # Check if the input file exists and load values if it does
    if not args.i and os.path.isfile(default_filename):
        with open(default_filename, 'r', encoding="utf-8") as file:
            data = json.load(file)

    current_equity_data = calculate_equity_from_data(data)

    # now modify data to reflect the expected day one flight stack result
    data['S_Day2'] += data['Expected_Day_One_Flight_Stack_Result']
    expected_equity_data = calculate_equity_from_data(data)

    # now calculate the difference between the two
    equity_difference = expected_equity_data['Equity_In_Dollars'] - current_equity_data['Equity_In_Dollars']
    print(f"equity_difference: {equity_difference}")

main()
