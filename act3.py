import requests

def get_ip_info(ip_address=None):
    # If no IP address is provided, use the current device's IP
    if ip_address:
        api_url = f'https://ipapi.co/{ip_address}/json/'
    else:
        api_url = 'https://ipapi.co/json/'  # Default to the user's current public IP
    
    try:
        # Send a request to the API
        response = requests.get(api_url)
        data = response.json()

        # Check if the response contains an error
        if 'error' in data:
            print(f"Error: {data['reason']}")
            return
        
        # Get the IP address and other information
        ip_address = data.get('ip')
        version = data.get('version') 
        city = data.get('city')
        region = data.get('region')
        country_code = data.get('country_code')
        country = data.get('country_name')
        asn = data.get('asn')
        org = data.get('org')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        postal = data.get('postal')
        hostname = data.get('hostname')
        timezone = data.get('timezone')

        # Display all of the information
        print(f"IP Address: {ip_address}")
        print(f"Version: {version}")
        print(f"City: {city}")
        print(f"Region: {region}")
        print(f"Country: {country}")
        print(f"Country Code: {country_code}")
        print(f"ASN: {asn}")
        print(f"Organization: {org}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        print(f"Postal: {postal}")
        print(f"Hostname: {hostname}")
        print(f"Timezone: {timezone}")


    except Exception as e:
        print(f"Error fetching IP information: {e}")

if __name__ == "__main__":
    # Ask the user to input an IPv4 address or press Enter to use their own public IP
    ip_input = input("Enter an IPv4 address (or press Enter to use your own public IP): ")
    get_ip_info(ip_input)