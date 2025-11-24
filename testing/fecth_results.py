from srilanka_lottery import scrape_nlb_result, scrape_dlb_result

# Fetch NLB result by draw number
# nlb_result = scrape_nlb_result("Govisetha", 4263)
# print("NLB Result (Draw 2166):", nlb_result)

# # Fetch NLB result by date
# nlb_result_date = scrape_nlb_result("Handahana", "2025-11-22")
# print("NLB Result (2025-05-01):", nlb_result_date)

# Fetch DLB result by draw number
dlb_result = scrape_dlb_result("Ada Kotipathi", 2608)
print("DLB Result (Draw 2608):", dlb_result)

# # Fetch DLB result by date
dlb_result_date = scrape_dlb_result("Ada Kotipathi", "2025-05-01")
print("DLB Result (2025-05-01):", dlb_result_date)