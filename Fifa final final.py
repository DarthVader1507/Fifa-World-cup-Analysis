from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
from prettytable import PrettyTable
mdf = pd.read_csv("Fifa_world_cup_matches(2).csv")  # Goals,Assists file
wdf = pd.read_csv("Fifa Worldcup 2022(2).csv")  # Results file
l = list(mdf.team1.unique())
l1 = list(wdf.Team.unique())
lc = l1.copy()
for i in range(len(l)):
    lc[i] = lc[i][:3]
for i in range(len(l1)):
    a = l1[i].lower()
    l[i] = a
    l[i] = l[i].upper()


def goalscored():
    a = input('Enter a team name(If the team has more than 1 word in its name,pls seperate the words by a space,for example:United States)\n')
    b = a.upper()
    ld = l1.copy()
    for i in range(len(ld)):
        ld[i] = ld[i].upper()
    while b not in ld:
        a = input("They did not qualify for the world cup,try again\n")
        b = a.upper()
    df = mdf[mdf.team1 == b]  # Extracts rows where a is team 1
    df1 = mdf[mdf.team2 == b]  # Extracts rows where a is team2
    s = 0
    s1 = 0
    # Adds all goals team a scored as home team
    s = sum(df.number_of_goals_team1)
    # Adds all goals team a scored as away team
    s1 = sum(df1.number_of_goals_team2)
    s += s1
    print(a, "scored", s, "goals")


def goal(lg):
    for i in l:
        dff = mdf[mdf.team1 == i]
        dff1 = mdf[mdf.team2 == i]
        ss = sum(dff.number_of_goals_team1)
        ss1 = sum(dff1.number_of_goals_team2)
        ss += ss1
        lg += [ss]  # Calculates all goals the team scored and adds it to list
    return (lg)


def win(lgw):
    w, ll, d = 0, 0, 0
    for i in l1:
        dff = wdf[wdf.Team == i]  # Team 1
        dff1 = wdf[wdf.Against == i]  # Team 2
        m_id = list(dff.Match_No.unique())
        for j in m_id:
            # In match x,how many goals team 1 scored
            temp_df = dff[dff.Match_No == j]
            # In match x,how many goals team 2 scored
            temp_df1 = dff1[dff1.Match_No == j]
            lwin = [sum(temp_df.Goal), sum(temp_df1.Goal)]
            if lwin[0] > lwin[1]:  # If team 1 scored more,win
                w += 1
            elif lwin[0] == lwin[1]:  # If equal goals scored,draw
                d += 1
            else:
                ll += 1
        lgw += [[w, d, ll]]
        w, d, ll = 0, 0, 0
    return (lgw)


def goala(lga):
    for i in l:
        dff = mdf[mdf.team1 == i]
        dff1 = mdf[mdf.team2 == i]
        ss = sum(dff.number_of_goals_team2)
        ss1 = sum(dff1.number_of_goals_team1)
        ss += ss1
        lga += [ss]  # Calculates all goals the team conceded and adds it to list
    return (lga)


def points(l):
    for i in range(len(l)):
        p = (l[i][0]*3)+(l[i][1])
        l[i] = l[i]+[p]
    return (l)
# Graph


def graph():
    a2 = input("Do you want a bar graph or linear graph\n")
    a2 = a2.lower()
    lgoals = goal([])
    if a2 == "bar":
        plt.bar(lc, lgoals)
        plt.xlabel("Team")
        plt.ylabel("Goals")
        plt.title("Goals scored")
        plt.show()
    elif a2 == "linear":
        plt.plot(lc, lgoals)
        plt.xlabel("Team")
        plt.ylabel("Goals")
        plt.title("Goals scored")
        plt.show()


def premier_league():
    print("This is how the world cup would have played out in the style of the premier league")
    list1 = goal([])
    list2 = goala([])
    w1 = win([])
    w1 = points(w1)
    le = l.copy()
    for i in range(len(le)):
        le[i] = le[i].title()
    for i in range(len(w1)):
        w1[i] = w1[i]+[le[i]]+[list1[i]]+[list2[i]]+[list1[i]-list2[i]]
    for i in range(len(w1)-1):
        for j in range(len(w1)-1-i):
            if w1[j][3] < w1[j+1][3]:
                t = w1[j]
                w1[j] = w1[j+1]
                w1[j+1] = t
            if w1[j][3] == w1[j+1][3]:
                if w1[j][7] < w1[j+1][7]:
                    t = w1[j]
                    w1[j] = w1[j+1]
                    w1[j+1] = t
                elif w1[j][7] == w1[j+1][7]:
                    if w1[j][5] < w1[j+1][5]:
                        t = w1[j]
                        w1[j] = w1[j+1]
                        w1[j+1] = t
    myTable = PrettyTable(["Position", "Team", "Wins", "Draws", "Losses",
                          "Points", "Goals scored", "Goals conceded", "Goal Difference"])
    c = 1
    for i in w1:
        myTable.add_row([c, i[4], i[0], i[1], i[2], i[3], i[5], i[6], i[7]])
        c += 1
    print(myTable)


def player_comparison():
    # Defining option list
    data = pd.read_csv("player_stats(1).csv")
    data1 = pd.read_csv("player_shooting(1).csv")
    data2 = pd.read_csv("player_defense(2).csv")
    a = input('Enter  team 1(If the team has more than 1 word in its name,pls seperate the words by a space,for example:United States)\n').title()
    while a not in l1:
        a = input("They did not qualify for the world cup,try again\n").title()
    b = input('Enter  team 2(If the team has more than 1 word in its name,pls seperate the words by a space,for example:United States)\n').title()
    while b not in l1:
        b = input("They did not qualify for the world cup,try again\n").title()
# a="Portugal"
    dx = data[data.team == a]
    l3 = ["Select a player from "+str(a)]
    for i in dx.player:
        l3 += [i]
    dx1 = data[data.team == b]
    l4 = ["Select a player from "+str(b)]
    for i in dx1.player:
        l4 += [i]
    tk = Tk()
    tk.title("Fifa stats")
    tk.geometry('800x200')
    st = StringVar(tk)
    st.set(l3[0])
    opt = OptionMenu(tk, st, *l3)
    opt.config(width=40, font=('Times New Roman', 17))
    opt.place(x=0, y=0)

# Label
    ls = Label(text="", font=('Times New Roman', 15), fg='black')
    ls.place(x=100, y=40)

    st1 = StringVar(tk)
    st1.set(l4[0])
    opt1 = OptionMenu(tk, st1, *l4)
    opt1.config(width=40, font=('Times New Roman', 17))
    opt1.place(x=400, y=0)
    ls1 = Label(text="", font=('Times New Roman', 15), fg='black')
    ls1.place(x=500, y=40)

    def name(*args):
        m = st.get()
        cc = data[data.player == m]
        g = data.loc[data['player'] == m, 'goals'].values[0]
        f = data.loc[data['player'] == m, 'assists'].values[0]
        h = data1.loc[data['player'] == m, 'shots'].values[0]
        l = data1.loc[data['player'] == m, 'shots_on_target'].values[0]
        y = data2.loc[data['player'] == m, 'tackles'].values[0]
        z = data2.loc[data['player'] == m, 'tackles_won'].values[0]
        ls.configure(text="Goals: {}\nAssists: {}\nTotal shots: {}\nShots on target: {}\nTackles: {}\nTackles won: {}".format(
            g, f, h, l, y, z))
    st.trace("w", name)

    def name1(*args):
        m1 = st1.get()
        dd = data[data.player == m1]
        g1 = data.loc[data['player'] == m1, 'goals'].values[0]
        f1 = data.loc[data['player'] == m1, 'assists'].values[0]
        h1 = data1.loc[data['player'] == m1, 'shots'].values[0]
        l1 = data1.loc[data['player'] == m1, 'shots_on_target'].values[0]
        y1 = data2.loc[data['player'] == m1, 'tackles'].values[0]
        z1 = data2.loc[data['player'] == m1, 'tackles_won'].values[0]
        ls1.configure(text="Goals: {}\nAssists: {}\nTotal shots: {}\nShots on target: {}\nTackles: {}\nTackles won: {}".format(
            g1, f1, h1, l1, y1, z1))
    st1.trace("w", name1)
    tk.mainloop()


def cards():
    m = pd.read_csv("Fifa Worldcup 2022(2).csv")
    aa = input(
        'Enter a team name to see how many yellow and red cards they got during the world cup\n').title()
    while aa not in l1:
        aa = input("They did not qualify for the world cup,try again\n").title()
    d = m[m.Team == aa]  # Extracts rows where a is Team playing
    s1, s2 = 0, 0
    for i in range(0, len(d)):
        s1 = sum(d.Yellow_Cards)
        s2 = sum(d.Red_Cards)
    print('number of yellow cards got by ', aa, ' is ', s1)
    print('number of red cards got by ', aa, ' is ', s2)


def casestudy():
    print("Case Study.Does possession really win matches?:")
    m = pd.read_csv("Fifa Worldcup 2022(2).csv")
    for i in range(0, 100):
        pass
    count = 0
    tl = list(m.Team.unique())
    cw = 0
    cd = 0
    cl = 0
    for i in tl:
        mp = m[m.Team == i]
        mp1 = m[m.Against == i]
        ll = list(mp.Match_No.unique())
        for j in ll:
            dd = mp[mp.Match_No == j]
            dd1 = mp1[mp1.Match_No == j]
            lpos = [sum(dd.Possession), sum(dd1.Possession)]
            lgo = [sum(dd.Goal), sum(dd1.Goal)]
            if lpos[1] > lpos[0]:
                if lgo[1] > lgo[0]:
                    cw += 1
                elif lgo[1] < lgo[0]:
                    cl += 1
                else:
                    cd += 1
            elif lpos[0] > lpos[1]:
                if lgo[0] > lgo[1]:
                    cw += 1
                elif lgo[0] < lgo[1]:
                    cl += 1
                else:
                    cd += 1
            else:
                pass
    print("Matches where team with more posession won is ", cw)
    print("Matches where team with more posession lost is ", cl)
    print("Matches with unequal possession which ended in a draw are", cd)
    if cw > cl:
        print("Hence proved,possesion wins matches")
    elif cw < cl:
        print("Hence proved,possesion does not win matches")


def menu():
    while True:
        a = int(input('''\nSelect an option whose contents you wish to display and enter the number of the option:
1)Find the number of goals scored by a team
2)Get a graph of the total goals scored by each country in the FIFA Tournament
3)Get a Premier League Table format of the teams participating in the World Cup
4)Get a comparision of two players from two different teams
5)Get a Fair Play score of a given team
6)Get a case study to find if possession really win matches?
7)Exit
\n'''))
        if a == 1:
            goalscored()
        elif a == 2:
            l = graph()
        elif a == 3:
            premier_league()
        elif a == 4:
            player_comparison()
        elif a == 5:
            cards()
        elif a == 6:
            casestudy()
        elif a == 7:
            break
        else:
            print('Invalid choice. Please Try again.')


menu()
