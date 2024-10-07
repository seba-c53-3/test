from googlesearch import search

# Function to perform Google Search and print results
def google_search(query, num_results=5):
    try:
        # Perform the search and get the results
        for result in search(query, num=num_results, stop=num_results, pause=2):
            print(result)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    query = input("Enter your search query: ")  # Prompt user for search query
    google_search(query)
