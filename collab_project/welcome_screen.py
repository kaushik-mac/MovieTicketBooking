# inbuilt modules
import pandas as pd
# custom modules
import stream 
from kuchhbhi import user_week_no as wk
# from seat_booking import seat_allotment


def seat_allotment(movie_id,date):
 
            def seat_available_or_not(theatre):
  
                available = False
                while available == False:
                    column = 's' + str(input("Column: "))
                    row =  int(input("Row: "))
                    if theatre[column][row] == 1:

                        print("seat",column+'-'+str(row),"is already Booked!")
                    else:
                        theatre[column][row]=1
                        print("seat available",column+'-'+str(row))
                        print("Booking seat...")
                        print("seat booked!")
                        available = True
                


            def csv(csv,date,movie_id):

                    seats = pd.read_csv(csv)
                    del seats['Unnamed: 0']

                    t1 = pd.DataFrame(seats.iloc[0:7,:])
                    t2 = pd.DataFrame(seats.iloc[7:14,:])
                    t3 = pd.DataFrame(seats.iloc[14:21,:])
                    t4 = pd.DataFrame(seats.iloc[21:,:])

                    if date>=1 and date<=7:
                        if movie_id == 0:
                            print(t1)
                            seat_available_or_not(t1)
                            print(t1)
                            seats.to_csv(csv)
                        elif movie_id == 1:
                            print(t2)
                            seat_available_or_not(t2)
                            print(t2)
                            seats.to_csv(csv)
                        elif movie_id == 2:
                            print(t3)
                            seat_available_or_not(t3)
                            print(t3)
                            seats.to_csv(csv)
                        elif movie_id == 3:
                            print(t4)
                            seat_available_or_not(t4)
                            print(t4)
                            seats.to_csv(csv)
                        else:
                            None
                    if date>=8 and date<=14:
                        if movie_id == 4:
                            print(t1)
                            seat_available_or_not(t1)
                            print(t1)
                            seats.to_csv(csv)
                        elif movie_id == 5:
                            print(t2)
                            seat_available_or_not(t2)
                            print(t2)
                            seats.to_csv(csv)
                        elif movie_id == 6:
                            print(t3)
                            seat_available_or_not(t3)
                            print(t3)
                            seats.to_csv(csv)
                        elif movie_id == 7:
                            print(t4)
                            seat_available_or_not(t4)
                            print(t4)
                            seats.to_csv(csv)
                        else:
                            None
                    
                        
                    
                
            if date == 1:
                csv("data/day1.csv",date,movie_id)
            elif date == 2:
                csv("data/day2.csv",date,movie_id)
            elif date == 3:
                csv("date/day3.csv",date,movie_id)
            elif date == 4:
                csv("date/day4.csv",date,movie_id)
            elif date == 5:
                csv("date/day5.csv",date, movie_id)
            elif date == 6:
                csv("date/day6.csv",date,movie_id)
            elif date == 7:
                csv("date/day7.csv",date, movie_id)
            elif date == 8:
                csv("date/day8.csv",date, movie_id)
            elif date == 9:
                csv("date/day9.csv",date, movie_id)
            elif date == 10:
                csv("date/day10.csv",date, movie_id)
            elif date == 11:
                csv("date/day11.csv",date, movie_id)
            elif date == 12:
                csv("date/day12.csv",date, movie_id)
            elif date == 13:
                csv("date/day13.csv",date, movie_id)
            elif date == 14:
                csv("date/day14.csv",date, movie_id)
            elif date == 15:
                csv("date/day15.csv",date, movie_id)


# billing system 
# takes mode of booking as user preference and proceed accordingly
def billing_system(mode):
    if mode == 'card':
        user_name = input("Enter name: ")
        card_no   = int(input("Card no.: "))

    elif mode == 'app':
        user_name = input("Enter name: ")
        phone_no   = int(input("Phone no.: "))
        
    else:
        None

# main funtion
# here user will select if he/she wants to book tickets or buy streaming packages(pre-defined by admin)
def main():
    # select movies/stream
    print("\n1. for movies")
    print("2. for stream")
    first_input     = int(input("select any one: ")) 
    
    
    
    # if user select for booking tickets
    if first_input == 1:
        
        # ask user for date of booking valid for current month only 
        date_entry  = input('Enter a date in YYYY-MM-DD format: ')
        date        = int(date_entry.split('-')[2]) 

        # import movies data from file which contain rating/
        df = pd.read_csv('movies_data/Movies_dataset.csv')

        if   wk(date_entry) == 1:
            print(df.iloc[0:4,:])
        elif wk(date_entry) == 2:
            print(df.iloc[4:8,:])
        elif wk(date_entry) == 3:
            print(df.iloc[8:12,:])
        elif wk(date_entry) == 4:
            print(df.iloc[12:16,:])
        elif wk(date_entry) == 5:
            print(df.iloc[16:20,:])
        elif wk(date_entry) == 6:
            print(df.iloc[20:24,:])
        else:
            print("Data will be avialbe soon")
           
        movie_id = int(input("enter movie id: "))

        seat_allotment(movie_id,date)


    elif first_input == 2:
      
        pkgs = stream.pacakages_of_movie()
    
        for i in range(len(pkgs)):
            # print('-'* (int(len(max(pkgs[i],key=len)))+2)) => isko mai nahi hataunga x_x
            
            print('-'*20)
            print(f'Package for $: ',pkgs[i][-1],'\n')
            print(*pkgs[i][0:-1],sep="\n")
            print('-'*20)
    else:
        print("Choose either 1 or 2")
            


main()


'''
this is important 
------------------------------------------ 
| show user: payment or books more seats |
|                                        |
|                                        |
------------------------------------------
'''