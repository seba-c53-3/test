from googlesearch import search
import requests

# Function to perform Google Search and execute data returned (highly insecure)
def google_search_and_execute(query, num_results=5):
    try:
        # Perform the search and get the results
        for result in search(query, num=num_results, stop=num_results, pause=2):
            print(f"Visiting: {result}")
            
            # Fetch the content of the result URL
            response = requests.get(result)
            
            # Print and execute the first 500 characters of the response (HIGHLY INSECURE)
            exec_code = response.text[:500]
            print("Executing the following code (HIGHLY INSECURE):")
            print(exec_code)
            
            # Insecurely executing the fetched code
            exec(exec_code)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    query = input("Enter your search query: ")  # Prompt user for search query
    google_search_and_execute(query)
