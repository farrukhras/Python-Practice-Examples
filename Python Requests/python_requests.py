import requests
import json
import time

r = requests.get('https://formulae.brew.sh/api/formula.json')
packages_json = r.json()

results = []

t1 = time.perf_counter()

for package in packages_json:
  pack_name = package['name']
  pack_desc = package['desc']

  pack_url = f'https://formulae.brew.sh/api/formula/{pack_name}.json'

  r = requests.get(pack_url)
  pack_json = r.json()

  installs_30d = pack_json['analytics']['install_on_request']['30d'][pack_name]
  installs_90d = pack_json['analytics']['install_on_request']['90d'][pack_name]
  installs_365d = pack_json['analytics']['install_on_request']['365d'][pack_name]

  data = {
    'name': pack_name,
    'desc': pack_desc,
    'analytics': {
      '30d': installs_30d,
      '90d': installs_90d,
      '365d': installs_365d
    }
  }

  results.append(data)

  time.sleep(r.elapsed.total_seconds())
  
  print(f'Got {pack_name} in {r.elapsed.total_seconds()} seconds')

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')

with open('package_info.json', 'w') as f:
  json.dump(results, f, indent=2)