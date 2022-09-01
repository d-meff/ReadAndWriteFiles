def main():
    infile = open('clients.txt', 'r')

    file_contents = infile.readlines()
    
    count = 1

    for client in file_contents:
        print(str(count) + ". " + client.rstrip('\n'))
        count += 1

main()