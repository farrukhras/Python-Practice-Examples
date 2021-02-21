import json

def install_sort_30d(package): # sort by the last 30 days
  return package['analytics']['30d']

def install_sort_90d(package): # sort by the last 90 days
  return package['analytics']['90d']

def install_sort_365d(package): # sort by the last 365 days
  return package['analytics']['365d']

with open('package_info.json', 'r') as f:
  data = json.load(f)

data.sort(key=install_sort_30d, reverse=True) # package with most installs in the last 30d at the top
# data.sort(key=install_sort_90d, reverse=True) # package with most installs in the last 90d at the top
# data.sort(key=install_sort_365d, reverse=True) # package with most installs in the last 365d at the top

data_str = json.dumps(data, indent=2)