from srilanka_lottery import scrape_dlb_lottery_names, scrape_nlb_active_lottery_names

# Scrape DLB lottery names
dlb_names = scrape_dlb_lottery_names()
print("DLB Lotteries:", dlb_names.get("DLB", dlb_names.get("error")))

# Scrape NLB active lottery names
nlb_names, session = scrape_nlb_active_lottery_names()
print("NLB Active Lotteries:", nlb_names.get("NLB_Active", nlb_names.get("error")))