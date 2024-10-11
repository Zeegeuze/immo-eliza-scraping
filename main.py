from scraper.scraping import *
from scraper.optimiser import *
import multiprocessing
import time

# As I can't easily get Selenium working on my separate Linux division, I'll skip this for now and will grab the data collected by a colleague

# accept_cookie()
# test = get_urls_from_page(1, 'huis')
# print(test)

start = time.perf_counter()

# Get all links
all_links = get_all_links()

# Create an empty dataframe
immo_df = create_df()
full_immo = pd.read_csv("data/immo.csv")

print(len(all_links))

# # Get all info
# # Normal speed: 45 sec for 100 entries -> 1h15 for all
# df = get_df(immo_df, all_links[:100])


# Optimising speed
# import sys
# Tried to have all the optimiser on a separate page, manage to get them there, but got troubles with the empty df
# sys.argv = ["scraper/optimiser.py", all_links, immo_df]
# exec('scraper/optimiser.py')

# exec(open('scraper/optimiser.py').read(), {"arg1": all_links})
# exec(open('scraper/optimiser.py').read())

# Put all separator below
df_1 = immo_df[:]

def part_1(df, urls):
    global df_1
    df_1 = get_df(df, urls)

df_2 = immo_df[:]

def part_2(df, urls):
    global df_2
    df_2 = get_df(df, urls)

df_3 = immo_df[:]

def part_3(df, urls):
    global df_3
    df_3 = get_df(df, urls)

df_4 = immo_df[:]

def part_4(df, urls):
    global df_4
    df_4 = get_df(df, urls)

df_5 = immo_df[:]

def part_5(df, urls):
    global df_5
    df_5 = get_df(df, urls)

df_6 = immo_df[:]

def part_6(df, urls):
    global df_6
    df_6 = get_df(df, urls)

df_7 = immo_df[:]

def part_7(df, urls):
    global df_7
    df_7 = get_df(df, urls)

df_8 = immo_df[:]

def part_8(df, urls):
    global df_8
    df_8 = get_df(df, urls)

df_9 = immo_df[:]

def part_9(df, urls):
    global df_9
    df_9 = get_df(df, urls)

df_10 = immo_df[:]

def part_10(df, urls):
    global df_10
    df_10 = get_df(df, urls)

df_11 = immo_df[:]

def part_11(df, urls):
    global df_11
    df_11 = get_df(df, urls)

df_12 = immo_df[:]

def part_12(df, urls):
    global df_12
    df_12 = get_df(df, urls)

df_13 = immo_df[:]

def part_13(df, urls):
    global df_13
    df_13 = get_df(df, urls)

df_14 = immo_df[:]

def part_14(df, urls):
    global df_14
    df_14 = get_df(df, urls)

df_15 = immo_df[:]

def part_15(df, urls):
    global df_15
    df_15 = get_df(df, urls)

df_16 = immo_df[:]

def part_16(df, urls):
    global df_16
    df_16 = get_df(df, urls)

df_17 = immo_df[:]

def part_17(df, urls):
    global df_17
    df_17 = get_df(df, urls)

df_18 = immo_df[:]

def part_18(df, urls):
    global df_18
    df_18 = get_df(df, urls)

df_19 = immo_df[:]

def part_19(df, urls):
    global df_19
    df_19 = get_df(df, urls)

df_20 = immo_df[:]

def part_20(df, urls):
    global df_20
    df_20 = get_df(df, urls)


if __name__ == '__main__':
    p_1 = multiprocessing.Process(name='p_1', target=part_1(df_1, all_links[15000:17500]))
    p_2 = multiprocessing.Process(name='p_2', target=part_2(df_2, all_links[17500:20000]))
    # p_3 = multiprocessing.Process(name='p_3', target=part_3(df_3, all_links[3000:3500]))
    # p_4 = multiprocessing.Process(name='p_4', target=part_4(df_4, all_links[150:200]))
    # p_5 = multiprocessing.Process(name='p_5', target=part_5(df_5, all_links[200:250]))
    # p_6 = multiprocessing.Process(name='p_6', target=part_6(df_6, all_links[250:300]))
    # p_7 = multiprocessing.Process(name='p_7', target=part_7(df_7, all_links[300:350]))
    # p_8 = multiprocessing.Process(name='p_8', target=part_8(df_8, all_links[350:400]))
    # p_9 = multiprocessing.Process(name='p_9', target=part_9(df_9, all_links[400:450]))
    # p_10 = multiprocessing.Process(name='p_10', target=part_10(df_10, all_links[450:500]))
    # p_11 = multiprocessing.Process(name='p_11', target=part_11(df_11, all_links[500:550]))
    # p_12 = multiprocessing.Process(name='p_12', target=part_12(df_12, all_links[550:600]))
    # p_13 = multiprocessing.Process(name='p_13', target=part_13(df_13, all_links[600:650]))
    # p_14 = multiprocessing.Process(name='p_14', target=part_14(df_14, all_links[650:700]))
    # p_15 = multiprocessing.Process(name='p_15', target=part_15(df_15, all_links[700:750]))
    # p_16 = multiprocessing.Process(name='p_16', target=part_16(df_16, all_links[750:800]))
    # p_17 = multiprocessing.Process(name='p_17', target=part_17(df_17, all_links[800:850]))
    # p_18 = multiprocessing.Process(name='p_18', target=part_18(df_18, all_links[850:900]))
    # p_19 = multiprocessing.Process(name='p_19', target=part_19(df_19, all_links[900:950]))
    # p_20 = multiprocessing.Process(name='p_20', target=part_20(df_20, all_links[950:1000]))

    p_1.start()
    p_2.start()
    # p_3.start()
    # p_4.start()
    # p_5.start()
    # p_6.start()
    # p_7.start()
    # p_8.start()
    # p_9.start()
    # p_10.start()
    # p_11.start()
    # p_12.start()
    # p_13.start()
    # p_14.start()
    # p_15.start()
    # p_16.start()
    # p_17.start()
    # p_18.start()
    # p_19.start()
    # p_20.start()

print("Starting new df")

full_immo = full_immo._append(df_1, ignore_index=True)
full_immo = full_immo._append(df_2, ignore_index=True)
# immo_df = immo_df._append(df_3, ignore_index=True)
# immo_df = immo_df._append(df_4, ignore_index=True)
# immo_df = immo_df._append(df_5, ignore_index=True)
# immo_df = immo_df._append(df_6, ignore_index=True)
# immo_df = immo_df._append(df_7, ignore_index=True)
# immo_df = immo_df._append(df_8, ignore_index=True)
# immo_df = immo_df._append(df_9, ignore_index=True)
# immo_df = immo_df._append(df_10, ignore_index=True)
# immo_df = immo_df._append(df_11, ignore_index=True)
# immo_df = immo_df._append(df_12, ignore_index=True)
# immo_df = immo_df._append(df_13, ignore_index=True)
# immo_df = immo_df._append(df_14, ignore_index=True)
# immo_df = immo_df._append(df_15, ignore_index=True)
# immo_df = immo_df._append(df_16, ignore_index=True)
# immo_df = immo_df._append(df_17, ignore_index=True)
# immo_df = immo_df._append(df_18, ignore_index=True)
# immo_df = immo_df._append(df_19, ignore_index=True)
# immo_df = immo_df._append(df_20, ignore_index=True)

print("done")

# Save to csv
save_to_csv(immo_df)
save_to_csv(full_immo)
