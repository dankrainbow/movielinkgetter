from googlesearch import search

query = input("Movie name: ") ## ask what movie trying to search and save as variable called query
queryjoined = "intitleof:indexof? mkv " + query ## add the bit before the query so it only returns urls with direct movie download

with open('output.txt', 'a') as output:
        for i in search(queryjoined, tld="co.in", num=10, stop=10, pause=2): ## search for the top 10 results
            output.write(f"{i}\n") ## write link, add a new line
            print(f"1 link added to txt : {i}")
            output.close ## close the file
