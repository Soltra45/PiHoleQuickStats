import requests

def get_info():
    ip = input("Enter the IP address of the Pi-Hole: ")
    return ip

def main():
    ip = get_info()
    url = "http://" + ip + "/admin/api.php"
    params = {'summary': 'true'}
    r = requests.get(url, params=params)
    data = r.json()
    print('Pi-Hole Quick Stats')
    print('====================')
    print('Queries blocked: ' + str(data['ads_blocked_today']))
    print('Queries forwarded: ' + str(data['dns_queries_today']))
    print('Percentage of queries blocked: ' + str(data['ads_percentage_today']))
    print('Percentage of queries forwarded: ' + str(data['ads_percentage_today']))
    print('====================')

if __name__ == "__main__":
    main()