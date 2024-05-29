import ipaddress

def validate_ip(ip):
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        try:
            if not 0 <= int(octet) <= 255:
                return False
        except ValueError:
            return False
    return True

def validate_subnet_mask(mask):
    octets = mask.split('.')
    
    if len(octets) != 4:
        return False
    
    binary_mask = ''.join([format(int(octet), '08b') for octet in octets])
    first_zero = False
    
    for bit in binary_mask:
        if bit == '0':
            first_zero = True
        elif first_zero and bit == '1':
            return False
    
    return True

def ip_to_binary(ip):
    return '.'.join([format(int(x), '08b') for x in ip.split('.')])

def main_interactive():
    ip = input("Enter an IP address: ")
    while not validate_ip(ip):
        print("Invalid IP address. Please try again.")
        ip = input("Enter an IP address: ")
    
    subnet_mask = input("Enter a subnet mask: ")
    while not validate_subnet_mask(subnet_mask):
        print("Invalid subnet mask. Please try again.")
        subnet_mask = input("Enter a subnet mask: ")
    
    print(f"IP Address: {ip}")
    print(f"Binary representation: {ip_to_binary(ip)}")
    print("Valid IP address")
    
    print(f"Subnet Mask: {subnet_mask}")
    print(f"Binary representation: {ip_to_binary(subnet_mask)}")
    print("Valid subnet mask")

def main_batch(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line in f_in:
            ip, subnet_mask = line.strip().split(',')
            if validate_ip(ip):
                f_out.write(f"IP Address: {ip}\n")
                f_out.write(f"Binary representation: {ip_to_binary(ip)}\n")
                f_out.write("Valid IP address\n")
            else:
                f_out.write(f"IP Address: {ip}\n")
                f_out.write("Invalid IP address\n")
            
            if validate_subnet_mask(subnet_mask):
                f_out.write(f"Subnet Mask: {subnet_mask}\n")
                f_out.write(f"Binary representation: {ip_to_binary(subnet_mask)}\n")
                f_out.write("Valid subnet mask\n")
            else:
                f_out.write(f"Subnet Mask: {subnet_mask}\n")
                f_out.write("Invalid subnet mask\n")

if __name__ == "__main__":
    mode = input("Choose mode (interactive/batch): ").lower()
    if mode == 'interactive':
        main_interactive()
    elif mode == 'batch':
        input_file = input("Enter input file name: ")
        output_file = input("Enter output file name: ")
        main_batch(input_file, output_file)
    else:
        print("Invalid mode. Please choose either 'interactive' or 'batch'.")

