from utils import query

def best_seller():
    # SQL query
    query_str = """
        SELECT TeaterStykke.navnPaStykke AS Forestillingsnavn, 
               f.dato AS Spilldato, 
               COUNT(b.BillettID) AS AntallSolgteBilletter
        FROM Forestilling AS f
        INNER JOIN Teaterstykke ON f.navnPaStykke = Teaterstykke.navnPaStykke
        LEFT JOIN Billett AS b ON b.ForestillingID = f.ForestillingID
        GROUP BY f.dato, Teaterstykke.navnPaStykke
        ORDER BY AntallSolgteBilletter DESC
    """
    
    # Execute query using utils function
    plays = query(query_str)
    
    return plays

def print_best_sellers(plays):
    print("Best Selling Performances:")
    print("{:<30} {:<20} {:<10}".format("Forestilling", "Dato", "Antall solgte plasser"))
    print("-" * 60)
    for play in plays:
        forestillingsnavn = play[0]
        spilldato = play[1]
        antall_solgte_billetter = play[2]
        print("{:<30} {:<20} {:<10}".format(forestillingsnavn, spilldato, antall_solgte_billetter))

if __name__ == "__main__":
    # Retrieve data using best_seller function
    plays = best_seller()
    
    # Print the data structure
    print("Data structure of plays:", plays)

    # Print best-selling performances
    print_best_sellers(plays)
